# AI-Driven Hotel/Flight Price Forecasting System
## Puduvai Youth Fest 2026 - Hackathon Project

### 🎯 Project Overview
An intelligent system that predicts future hotel and flight prices using machine learning to help travelers make cost-effective booking decisions.

### 🚀 Features
- **Price Prediction**: ML-powered forecasting using historical data
- **Trend Analysis**: Visual price trend graphs
- **Smart Recommendations**: "Book Now" or "Wait" suggestions
- **Interactive UI**: Clean Streamlit web application
- **Real-time Insights**: Instant price analysis

### 🛠️ Tech Stack
- **Language**: Python
- **ML Libraries**: scikit-learn, pandas, numpy
- **Visualization**: matplotlib, seaborn
- **UI Framework**: Streamlit
- **Model**: Linear Regression & Time Series Analysis

### 📁 Project Structure
```
price-forecasting-system/
├── app.py                 # Main Streamlit application
├── model.py              # ML model implementation
├── data_generator.py     # Sample data creation
├── requirements.txt      # Dependencies
├── data/
│   ├── hotel_prices.csv  # Hotel price dataset
│   └── flight_prices.csv # Flight price dataset
├── models/
│   ├── hotel_model.pkl   # Trained hotel model
│   └── flight_model.pkl  # Trained flight model
└── presentation/
    └── hackathon_slides.md # PPT content
```

### 🏃‍♂️ Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Generate sample data: `python data_generator.py`
3. Train models: `python model.py`
4. Run app: `streamlit run app.py`

### 🌍 Social Impact
- **Cost-Efficient Travel**: Helps users save money on bookings
- **AI for Social Good**: Democratizes travel planning
- **Smart Decision-Making**: Data-driven travel choices
- **Sustainable Tourism**: Optimized travel planning reduces waste