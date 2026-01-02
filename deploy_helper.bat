@echo off
echo ========================================
echo AI Price Forecasting - Deployment Helper
echo ========================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed!
    echo.
    echo Please run: install_git.bat
    echo Or download from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo Git is installed!
git --version
echo.

REM Check if Git is configured
git config user.name >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Git is not configured yet.
    echo.
    set /p username="Enter your name: "
    set /p email="Enter your email: "
    git config --global user.name "%username%"
    git config --global user.email "%email%"
    echo.
    echo Git configured successfully!
)

echo.
echo Current Git Configuration:
git config user.name
git config user.email
echo.

REM Check if already initialized
if exist .git (
    echo Git repository already initialized.
    echo.
    echo Current status:
    git status
    echo.
    echo To push changes:
    echo   git add .
    echo   git commit -m "Your message"
    echo   git push
    echo.
) else (
    echo Initializing Git repository...
    git init
    echo.
    echo Adding files...
    git add .
    echo.
    echo Creating initial commit...
    git commit -m "Initial commit: AI Price Forecasting System"
    echo.
    echo ========================================
    echo NEXT STEPS:
    echo ========================================
    echo.
    echo 1. Create a GitHub repository:
    echo    Go to: https://github.com/new
    echo    Name: ai-price-forecasting
    echo    Make it PUBLIC
    echo.
    echo 2. Connect to GitHub (replace YOUR_USERNAME):
    echo    git remote add origin https://github.com/YOUR_USERNAME/ai-price-forecasting.git
    echo.
    echo 3. Push to GitHub:
    echo    git branch -M main
    echo    git push -u origin main
    echo.
    echo 4. Deploy to Streamlit Cloud:
    echo    Go to: https://share.streamlit.io/
    echo    Sign in with GitHub
    echo    Click "New app"
    echo    Select your repository
    echo    Deploy!
    echo.
)

echo.
echo Opening deployment guide...
start DEPLOY_NOW.md

pause