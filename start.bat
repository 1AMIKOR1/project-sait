@echo off
chcp 65001 >nul 2>&1
title FirstByte - launch

echo.
echo  ========================================
echo   FirstByte - launching site
echo  ========================================
echo.

:: --- Check Python ---
py --version >nul 2>&1
if %errorlevel% equ 0 goto :found_py

python --version >nul 2>&1
if %errorlevel% equ 0 goto :found_python

goto :no_python

:found_py
echo [OK] Python found:
py --version
set PY=py
goto :install_deps

:found_python
echo [OK] Python found:
python --version
set PY=python
goto :install_deps

:no_python
echo [!!] Python not found. Installing...
echo.

set INSTALLER=%TEMP%\python-installer.exe
echo Downloading Python 3.12...
powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.7/python-3.12.7-amd64.exe' -OutFile '%INSTALLER%'"

if not exist "%INSTALLER%" goto :download_failed

echo Installing Python...
"%INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_pip=1
del "%INSTALLER%" >nul 2>&1

set "PATH=%LocalAppData%\Programs\Python\Python312;%LocalAppData%\Programs\Python\Python312\Scripts;%PATH%"

py --version >nul 2>&1
if %errorlevel% equ 0 (
    set PY=py
    goto :install_deps
)
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set PY=python
    goto :install_deps
)

echo [ERROR] Python installed but not found in PATH.
echo Restart this script or open a new terminal.
pause
exit /b 1

:download_failed
echo [ERROR] Failed to download Python installer.
echo Install manually: https://www.python.org/downloads/
pause
exit /b 1

:: --- Install dependencies ---
:install_deps
echo.
echo Installing dependencies...
%PY% -m pip install -r "%~dp0requirements.txt" --quiet 2>nul
echo [OK] Dependencies ready.
echo.
echo  ========================================
echo   Site: http://127.0.0.1:5000
echo   Press Ctrl+C to stop
echo  ========================================
echo.

cd /d "%~dp0"
%PY% app.py
pause
