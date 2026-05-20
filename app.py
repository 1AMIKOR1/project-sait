# -*- coding: utf-8 -*-
"""Flask application for the site with simple user authentication."""

import os
import sqlite3
from datetime import datetime, timedelta, timezone
from functools import wraps

from flask import (
    Flask,
    abort,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from articles import (
    CATEGORIES,
    all_articles,
    by_category,
    get_article,
    latest,
    related,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-change-me")
app.config["DATABASE"] = os.path.join(app.instance_path, "users.sqlite3")
MOSCOW_TZ = timezone(timedelta(hours=3), name="\u041c\u0421\u041a")
UTC_TZ = timezone.utc


def get_db():
    if "db" not in g:
        os.makedirs(app.instance_path, exist_ok=True)
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


def init_db():
    with app.app_context():
        db = get_db()
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        db.commit()


@app.teardown_appcontext
def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.before_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
        return

    g.user = get_db().execute(
        "SELECT id, username, email, created_at FROM users WHERE id = ?",
        (user_id,),
    ).fetchone()


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash("Войдите в аккаунт, чтобы открыть эту страницу.", "warning")
            return redirect(url_for("login", next=request.path))
        return view(**kwargs)

    return wrapped_view


def safe_next_url(default_endpoint="profile"):
    next_url = request.args.get("next")
    if next_url and next_url.startswith("/") and not next_url.startswith("//"):
        return next_url
    return url_for(default_endpoint)


@app.template_filter("msk_datetime")
def msk_datetime(value):
    if not value:
        return ""

    try:
        dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return value

    msk_value = dt.replace(tzinfo=UTC_TZ).astimezone(MOSCOW_TZ)
    return f"{msk_value.strftime('%d.%m.%Y %H:%M:%S')} \u041c\u0421\u041a"


@app.context_processor
def inject_globals():
    return {
        "categories": CATEGORIES,
        "current_user": g.get("user"),
        "site_name": "ПервыйБайт",
    }


@app.route("/")
def index():
    return render_template(
        "index.html",
        latest_articles=latest(3),
        all=all_articles(),
    )


@app.route("/category/<slug>/")
def category(slug):
    category_data = CATEGORIES.get(slug)
    if not category_data:
        abort(404)
    return render_template(
        "category.html",
        category=category_data,
        articles=by_category(slug),
    )


@app.route("/article/<slug>/")
def article(slug):
    art = get_article(slug)
    if not art:
        abort(404)
    return render_template(
        "article.html",
        article=art,
        category=CATEGORIES[art["category"]],
        related_articles=related(slug, 3),
    )


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/register/", methods=("GET", "POST"))
def register():
    if g.user is not None:
        return redirect(url_for("profile"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        password_confirm = request.form.get("password_confirm", "")
        error = None

        if len(username) < 3:
            error = "Имя пользователя должно быть не короче 3 символов."
        elif "@" not in email or "." not in email:
            error = "Введите корректный email."
        elif len(password) < 6:
            error = "Пароль должен быть не короче 6 символов."
        elif password != password_confirm:
            error = "Пароли не совпадают."

        if error is None:
            db = get_db()
            try:
                cursor = db.execute(
                    """
                    INSERT INTO users (username, email, password_hash)
                    VALUES (?, ?, ?)
                    """,
                    (username, email, generate_password_hash(password)),
                )
                db.commit()
            except sqlite3.IntegrityError:
                error = "Пользователь с таким именем или email уже существует."
            else:
                session.clear()
                session["user_id"] = cursor.lastrowid
                flash("Аккаунт создан. Вы вошли на сайт.", "success")
                return redirect(url_for("profile"))

        flash(error, "error")

    return render_template("register.html")


@app.route("/login/", methods=("GET", "POST"))
def login():
    if g.user is not None:
        return redirect(url_for("profile"))

    if request.method == "POST":
        login_value = request.form.get("login", "").strip()
        password = request.form.get("password", "")
        user = get_db().execute(
            """
            SELECT * FROM users
            WHERE username = ? OR email = ?
            """,
            (login_value, login_value.lower()),
        ).fetchone()

        if user is None or not check_password_hash(user["password_hash"], password):
            flash("Неверный логин или пароль.", "error")
        else:
            session.clear()
            session["user_id"] = user["id"]
            flash("Вы вошли на сайт.", "success")
            return redirect(safe_next_url())

    return render_template("login.html")


@app.route("/logout/")
def logout():
    session.clear()
    flash("Вы вышли из аккаунта.", "success")
    return redirect(url_for("index"))


@app.route("/profile/")
@login_required
def profile():
    return render_template("profile.html")


@app.route("/profile/change-password/", methods=("POST",))
@login_required
def change_password():
    current_password = request.form.get("current_password", "")
    new_password = request.form.get("new_password", "")
    new_password_confirm = request.form.get("new_password_confirm", "")
    user = get_db().execute(
        "SELECT password_hash FROM users WHERE id = ?",
        (g.user["id"],),
    ).fetchone()

    if user is None:
        session.clear()
        flash("Аккаунт не найден. Войдите заново.", "error")
        return redirect(url_for("login"))

    if not check_password_hash(user["password_hash"], current_password):
        flash("Текущий пароль введен неверно.", "error")
    elif len(new_password) < 6:
        flash("Новый пароль должен быть не короче 6 символов.", "error")
    elif new_password != new_password_confirm:
        flash("Новые пароли не совпадают.", "error")
    elif check_password_hash(user["password_hash"], new_password):
        flash("Новый пароль должен отличаться от текущего.", "error")
    else:
        get_db().execute(
            "UPDATE users SET password_hash = ? WHERE id = ?",
            (generate_password_hash(new_password), g.user["id"]),
        )
        get_db().commit()
        flash("Пароль изменен.", "success")

    return redirect(url_for("profile"))


init_db()


if __name__ == "__main__":
    app.run(debug=True)
