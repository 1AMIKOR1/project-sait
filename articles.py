# -*- coding: utf-8 -*-
"""Данные статей сайта ПервыйБайт.

Статьи хранятся в виде словаря, ключ — slug (латиницей), значение — метаданные и HTML-контент.
БД не используется: чтобы добавить статью, достаточно дописать запись в ARTICLES.
"""

CATEGORIES = {
    "devices": {
        "slug": "devices",
        "title": "Устройства",
        "subtitle": "Смартфоны, ноутбуки и гаджеты",
        "description": "Что выбрать, на что смотреть и чего избегать. Без маркетинга — простыми словами.",
        "icon": "smartphone",
    },
    "apps": {
        "slug": "apps",
        "title": "Приложения",
        "subtitle": "Мессенджеры, облака и полезный софт",
        "description": "Разбираем, какие приложения реально пригодятся каждый день.",
        "icon": "layout-grid",
    },
    "ai": {
        "slug": "ai",
        "title": "ИИ и будущее",
        "subtitle": "Нейросети простыми словами",
        "description": "Как пользоваться искусственным интеллектом и чего опасаться.",
        "icon": "sparkles",
    },
    "security": {
        "slug": "security",
        "title": "Интернет и безопасность",
        "subtitle": "Защитите свои данные",
        "description": "Пароли, VPN, двухфакторная аутентификация — всё по полочкам.",
        "icon": "shield",
    },
}


def _p(text):
    return f"<p>{text}</p>"


def _h(text):
    return f"<h2>{text}</h2>"


def _quote(text):
    return f'<blockquote>{text}</blockquote>'


CHATGPT_BODY = (
    _p("Нейросети-собеседники прочно вошли в нашу жизнь. ChatGPT, Claude, Gemini и десятки других сервисов "
       "готовы ответить почти на любой вопрос. Но удобство приходит с подвохами, о которых стоит знать заранее.")
    + _h("Что такое нейросеть-собеседник")
    + _p("Это программа, обученная на огромном количестве текстов из интернета. Она умеет продолжать вашу мысль так, "
         "чтобы ответ был похож на человеческий. Она не «знает» — она угадывает наиболее вероятный следующий кусок текста.")
    + _h("Где её удобно применять")
    + _p("Объяснить сложный термин простыми словами, написать черновик письма, перевести текст, "
         "придумать идею для подарка или составить список покупок. Везде, где результат потом легко проверить.")
    + _quote("Главное правило: никогда не доверяйте нейросети там, где ошибка может стоить денег, здоровья или репутации.")
    + _h("Чего стоит избегать")
    + _p("Не спрашивайте у нейросети медицинских и юридических советов. Не передавайте ей пароли, номера карт "
         "и личные документы. И помните: красивый уверенный ответ ещё не значит правильный.")
)


STUB_BODY = (
    _p("Это демонстрационная статья сайта ПервыйБайт. Здесь будет полный текст обзора — "
       "простым языком, без лишнего маркетинга и заумных терминов.")
    + _h("Главное в двух словах")
    + _p("Мы расскажем, на что обратить внимание, какие подводные камни встречаются чаще всего "
         "и как не переплатить за ненужные функции.")
    + _h("Наш совет")
    + _p("Если вы только начинаете разбираться в теме — не спешите. Прочитайте пару материалов, "
         "сравните мнения и только после этого принимайте решение.")
)


ARTICLES = {
    "chatgpt-guide": {
        "slug": "chatgpt-guide",
        "title": "ChatGPT и аналоги: как пользоваться и где осторожничать",
        "excerpt": "Разбираемся, чем полезны нейросети-собеседники и почему им нельзя доверять всё подряд.",
        "category": "ai",
        "date": "8 апреля 2026",
        "read_time": "7 минут чтения",
        "image": "chatgpt.jpeg",
        "hero_image": "article-chatgpt-hero.jpeg",
        "body": CHATGPT_BODY,
    },
    "first-laptop": {
        "slug": "first-laptop",
        "title": "Как выбрать первый ноутбук: на что смотреть новичку",
        "excerpt": "Процессор, память, экран, вес — простой чек-лист, чтобы не переплатить за лишнее.",
        "category": "devices",
        "date": "5 апреля 2026",
        "read_time": "6 минут чтения",
        "image": "laptop.jpeg",
        "hero_image": "laptop.jpeg",
        "body": STUB_BODY,
    },
    "smartphone-2026": {
        "slug": "smartphone-2026",
        "title": "Смартфон 2026: какие функции реально нужны, а какие — маркетинг",
        "excerpt": "Какие функции стоят денег, а какие — просто маркетинг.",
        "category": "devices",
        "date": "3 апреля 2026",
        "read_time": "5 минут чтения",
        "image": "smartphone.jpeg",
        "hero_image": "smartphone.jpeg",
        "body": STUB_BODY,
    },
    "wireless-earbuds": {
        "slug": "wireless-earbuds",
        "title": "Беспроводные наушники: плюсы, минусы и подводные камни",
        "excerpt": "Чем удобны, на что обратить внимание перед покупкой.",
        "category": "devices",
        "date": "1 апреля 2026",
        "read_time": "4 минуты чтения",
        "image": "earbuds.jpeg",
        "hero_image": "earbuds.jpeg",
        "body": STUB_BODY,
    },
    "smart-watches": {
        "slug": "smart-watches",
        "title": "Умные часы: зачем они нужны и кому подойдут",
        "excerpt": "Фитнес, уведомления, оплата — разбираем по полочкам.",
        "category": "devices",
        "date": "28 марта 2026",
        "read_time": "5 минут чтения",
        "image": "smartwatch.jpeg",
        "hero_image": "smartwatch.jpeg",
        "body": STUB_BODY,
    },
    "messengers": {
        "slug": "messengers",
        "title": "Мессенджеры: чем отличаются Telegram, WhatsApp и Signal",
        "excerpt": "Сравнение трёх главных мессенджеров глазами обычного пользователя.",
        "category": "apps",
        "date": "25 марта 2026",
        "read_time": "6 минут чтения",
        "image": "messengers.jpeg",
        "hero_image": "messengers.jpeg",
        "body": STUB_BODY,
    },
    "cloud-storage": {
        "slug": "cloud-storage",
        "title": "Облачные хранилища: где безопаснее держать файлы",
        "excerpt": "Google Drive, Dropbox, Яндекс.Диск — куда положить файлы.",
        "category": "apps",
        "date": "22 марта 2026",
        "read_time": "5 минут чтения",
        "image": "cloud.jpeg",
        "hero_image": "cloud.jpeg",
        "body": STUB_BODY,
    },
    "free-alternatives": {
        "slug": "free-alternatives",
        "title": "Бесплатные альтернативы платным программам",
        "excerpt": "Подборка инструментов, за которые не нужно платить ни рубля.",
        "category": "apps",
        "date": "19 марта 2026",
        "read_time": "7 минут чтения",
        "image": "free-software.jpeg",
        "hero_image": "free-software.jpeg",
        "body": STUB_BODY,
    },
    "what-is-neural-network": {
        "slug": "what-is-neural-network",
        "title": "Что такое нейросети простыми словами",
        "excerpt": "Без формул и заумных терминов — только суть.",
        "category": "ai",
        "date": "16 марта 2026",
        "read_time": "6 минут чтения",
        "image": "neural-networks.jpeg",
        "hero_image": "neural-networks.jpeg",
        "body": STUB_BODY,
    },
    "ai-image-gen": {
        "slug": "ai-image-gen",
        "title": "Генерация изображений ИИ: обзор для начинающих",
        "excerpt": "Какие сервисы попробовать и с чего начать.",
        "category": "ai",
        "date": "13 марта 2026",
        "read_time": "5 минут чтения",
        "image": "ai-art.jpeg",
        "hero_image": "ai-art.jpeg",
        "body": STUB_BODY,
    },
    "strong-passwords": {
        "slug": "strong-passwords",
        "title": "Как придумать надёжный пароль и не забыть его",
        "excerpt": "Менеджеры паролей, фразы вместо слов и привычки, которые спасут ваши аккаунты.",
        "category": "security",
        "date": "10 марта 2026",
        "read_time": "5 минут чтения",
        "image": "password.jpeg",
        "hero_image": "password.jpeg",
        "body": STUB_BODY,
    },
    "vpn-explained": {
        "slug": "vpn-explained",
        "title": "Что такое VPN и нужен ли он обычному пользователю",
        "excerpt": "Простое объяснение и честные сценарии использования.",
        "category": "security",
        "date": "7 марта 2026",
        "read_time": "6 минут чтения",
        "image": "vpn.jpeg",
        "hero_image": "vpn.jpeg",
        "body": STUB_BODY,
    },
    "two-factor-auth": {
        "slug": "two-factor-auth",
        "title": "Двухфакторная аутентификация: зачем включать везде",
        "excerpt": "Как защитить аккаунты, даже если пароль украли.",
        "category": "security",
        "date": "4 марта 2026",
        "read_time": "4 минуты чтения",
        "image": "2fa.jpeg",
        "hero_image": "2fa.jpeg",
        "body": STUB_BODY,
    },
}


def all_articles():
    """Возвращает список всех статей в исходном порядке (от свежих к старым)."""
    return list(ARTICLES.values())


def get_article(slug):
    return ARTICLES.get(slug)


def by_category(category_slug):
    return [a for a in ARTICLES.values() if a["category"] == category_slug]


def latest(n=3):
    return list(ARTICLES.values())[:n]


def related(current_slug, n=3):
    current = ARTICLES.get(current_slug)
    if not current:
        return []
    same_cat = [a for a in ARTICLES.values() if a["category"] == current["category"] and a["slug"] != current_slug]
    others = [a for a in ARTICLES.values() if a["category"] != current["category"]]
    return (same_cat + others)[:n]
