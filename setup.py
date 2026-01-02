"""
AI-Driven Price Forecasting System - Setup Script
Automated setup for the complete hackathon project
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please install manually:")
        print("pip install -r requirements.txt")
        return False
    return True

def generate_data():
    """Generate sample datasets"""
    print("📊 Generating sample datasets...")
    try:
        subprocess.check_call([sys.executable, "data_generator.py"])
        print("✅ Sample data generated successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to generate data")
        return False
    return True

def train_models():
    """Train ML models"""
    print("🤖 Training machine learning models...")
    try:
        subprocess.check_call([sys.executable, "model.py"])
        print("✅ Models trained successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to train models")
        return False
    return True

def check_files():
    """Check if all required files exist"""
    required_files = [
        "app.py",
        "model.py", 
        "data_generator.py",
        "requirements.txt",
        "data/hotel_prices.csv",
        "data/flight_prices.csv",
        "models/hotel_model.pkl",
        "models/flight_model.pkl"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    
    print("✅ All required files present!")
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up AI Price Forecasting System...")
    print("=" * 50)
    
    # Step 1: Install packages
    if not install_requirements():
        return
    
    # Step 2: Generate data
    if not generate_data():
        return
    
    # Step 3: Train models
    if not train_models():
        return
    
    # Step 4: Check all files
    if not check_files():
        return
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n📋 Next Steps:")
    print("1. Run the app: streamlit run app.py")
    print("2. Open browser to: http://localhost:8501")
    print("3. Start making predictions!")
    print("\n💡 For presentation:")
    print("- Review: presentation/hackathon_slides.md")
    print("- Practice the demo script")
    print("- Prepare for questions")
    print("\n🏆 Good luck with your hackathon!")

if __name__ == "__main__":
    main()