@echo off
echo ========================================
echo Git Installation Helper
echo ========================================
echo.
echo Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Git is already installed!
    git --version
    echo.
    echo You can proceed with deployment.
    pause
    exit /b 0
)

echo.
echo Git is NOT installed.
echo.
echo Opening Git download page in your browser...
echo.
echo Please:
echo 1. Download Git for Windows
echo 2. Run the installer
echo 3. Use default settings (just click Next)
echo 4. Restart this script after installation
echo.
pause

start https://git-scm.com/download/win

echo.
echo After installing Git, close this window and run this script again.
pause