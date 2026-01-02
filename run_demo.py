"""
AI-Driven Price Forecasting System - Demo Runner
Quick demo script for hackathon presentation
"""

import subprocess
import sys
import webbrowser
import time
import os

def check_setup():
    """Check if system is properly set up"""
    required_files = [
        "data/hotel_prices.csv",
        "data/flight_prices.csv", 
        "models/hotel_model.pkl",
        "models/flight_model.pkl"
    ]
    
    missing = [f for f in required_files if not os.path.exists(f)]
    
    if missing:
        print("❌ Setup incomplete. Missing files:")
        for f in missing:
            print(f"   - {f}")
        print("\n🔧 Run setup first: python setup.py")
        return False
    
    return True

def start_streamlit():
    """Start the Streamlit application"""
    print("🚀 Starting AI Price Forecasting Demo...")
    print("⏳ Please wait while the application loads...")
    
    try:
        # Start Streamlit in background
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.headless", "true",
            "--server.port", "8501"
        ])
        
        # Wait a moment for server to start
        time.sleep(3)
        
        # Open browser
        print("🌐 Opening browser...")
        webbrowser.open("http://localhost:8501")
        
        print("\n" + "=" * 50)
        print("🎉 Demo is now running!")
        print("📱 URL: http://localhost:8501")
        print("⌨️  Press Ctrl+C to stop the demo")
        print("=" * 50)
        
        # Keep running until interrupted
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Stopping demo...")
            process.terminate()
            print("✅ Demo stopped successfully!")
            
    except Exception as e:
        print(f"❌ Error starting demo: {e}")
        print("💡 Try running manually: streamlit run app.py")

def show_demo_tips():
    """Show tips for demo presentation"""
    print("\n🎯 DEMO PRESENTATION TIPS:")
    print("=" * 40)
    print("1. 🏨 Start with Hotel prediction")
    print("2. 📅 Select a date 1-2 weeks ahead")
    print("3. 📊 Show the price trend chart")
    print("4. 💡 Explain the recommendation")
    print("5. ✈️  Switch to Flight prediction")
    print("6. 🔄 Try different dates to show variety")
    print("7. 📈 Highlight the historical trends")
    print("8. 🧠 Mention AI insights section")
    print("\n💬 KEY TALKING POINTS:")
    print("- 'Our AI analyzes patterns to predict prices'")
    print("- 'Clear recommendations: Book Now or Wait'")
    print("- 'Can save travelers 10-20% on bookings'")
    print("- 'Built with Linear Regression for reliability'")
    print("=" * 40)

def main():
    """Main demo function"""
    print("🤖 AI Price Forecasting System - Demo Mode")
    print("🏆 Puduvai Youth Fest 2026 Hackathon")
    print("=" * 50)
    
    # Check if setup is complete
    if not check_setup():
        return
    
    # Show demo tips
    show_demo_tips()
    
    # Ask if ready to start
    input("\n⏸️  Press Enter when ready to start demo...")
    
    # Start the demo
    start_streamlit()

if __name__ == "__main__":
    main()