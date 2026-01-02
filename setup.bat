@echo off
echo ========================================
echo AI Price Forecasting System Setup
echo Puduvai Youth Fest 2026 Hackathon
echo ========================================

echo.
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    echo Please install Python first:
    echo 1. Go to https://www.python.org/downloads/
    echo 2. Download Python 3.11 or 3.12
    echo 3. Install with "Add to PATH" checked
    echo 4. Restart this script
    pause
    exit /b 1
)

echo Python found! Continuing setup...

echo.
echo Installing required packages...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install packages
    pause
    exit /b 1
)

echo.
echo Generating sample data...
python data_generator.py
if %errorlevel% neq 0 (
    echo ERROR: Failed to generate data
    pause
    exit /b 1
)

echo.
echo Training ML models...
python model.py
if %errorlevel% neq 0 (
    echo ERROR: Failed to train models
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo To run the application:
echo   streamlit run app.py
echo.
echo To run demo mode:
echo   python run_demo.py
echo.
echo Your browser will open automatically.
echo Press any key to start the demo now...
pause >nul

echo Starting demo...
python run_demo.py