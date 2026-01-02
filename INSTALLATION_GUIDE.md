# 🚀 Installation Guide - AI Price Forecasting System

## Prerequisites Setup

### Step 1: Install Python
Since Python is not detected on your system, you need to install it first:

#### Option A: Microsoft Store (Recommended for Windows)
1. Open Microsoft Store
2. Search for "Python 3.11" or "Python 3.12"
3. Click "Install"
4. Wait for installation to complete

#### Option B: Official Python Website
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or 3.12 for Windows
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH" during installation
5. Complete the installation

#### Option C: Using Chocolatey (if you have it)
```powershell
choco install python
```

### Step 2: Verify Python Installation
Open a new PowerShell/Command Prompt and run:
```powershell
python --version
```
or
```powershell
py --version
```

You should see something like: `Python 3.11.x` or `Python 3.12.x`

## Project Setup

### Step 3: Install Required Packages
```powershell
pip install pandas numpy matplotlib seaborn scikit-learn streamlit plotly joblib
```

Or use the requirements file:
```powershell
pip install -r requirements.txt
```

### Step 4: Generate Sample Data
```powershell
python data_generator.py
```

### Step 5: Train ML Models
```powershell
python model.py
```

### Step 6: Run the Application
```powershell
streamlit run app.py
```

## Quick Setup (All-in-One)
Once Python is installed, run:
```powershell
python setup.py
```

## Demo Mode (For Hackathon)
```powershell
python run_demo.py
```

## Troubleshooting

### If "python" command not found:
- Try using `py` instead of `python`
- Restart your terminal after Python installation
- Check if Python is in your PATH environment variable

### If packages fail to install:
- Update pip: `python -m pip install --upgrade pip`
- Use: `python -m pip install -r requirements.txt`

### If Streamlit doesn't start:
- Check if port 8501 is available
- Try: `python -m streamlit run app.py`

## File Structure After Setup
```
AI-hackathon/
├── app.py                    # Main Streamlit app
├── model.py                  # ML model code
├── data_generator.py         # Data generation
├── setup.py                  # Automated setup
├── run_demo.py              # Demo runner
├── requirements.txt          # Dependencies
├── data/
│   ├── hotel_prices.csv     # Generated hotel data
│   └── flight_prices.csv    # Generated flight data
├── models/
│   ├── hotel_model.pkl      # Trained hotel model
│   └── flight_model.pkl     # Trained flight model
└── presentation/
    └── hackathon_slides.md   # Presentation content
```

## Next Steps
1. Install Python following Step 1
2. Run the setup commands
3. Test the application
4. Prepare for your hackathon presentation!

## Support
If you encounter any issues:
1. Check that Python is properly installed
2. Ensure all packages are installed
3. Verify all files are present
4. Try running commands one by one instead of using setup.py