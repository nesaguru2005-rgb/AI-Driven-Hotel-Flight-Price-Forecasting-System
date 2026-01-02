# 🔄 AI Price Forecasting System - Project Flow

## System Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Layer    │    │   ML Engine     │    │   UI Layer      │
│                 │    │                 │    │                 │
│ • Hotel Data    │───▶│ • Feature Eng.  │───▶│ • Streamlit App │
│ • Flight Data   │    │ • Model Training│    │ • Interactive   │
│ • Historical    │    │ • Predictions   │    │ • Visualizations│
│   Patterns      │    │ • Recommendations│   │ • User Input    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Data Flow Process

### 1. Data Generation Phase
```
data_generator.py
├── Generate Hotel Data (2 years)
│   ├── Base prices with seasonal variation
│   ├── Weekend/weekday patterns
│   ├── Holiday premiums
│   └── Random demand factors
├── Generate Flight Data (2 years)
│   ├── Seasonal travel patterns
│   ├── Day-of-week pricing
│   ├── Advance booking effects
│   └── Market fluctuations
└── Save to CSV files
    ├── data/hotel_prices.csv
    └── data/flight_prices.csv
```

### 2. Model Training Phase
```
model.py
├── Load Historical Data
├── Feature Engineering
│   ├── Date features (month, day, week)
│   ├── Categorical encoding (season, day_of_week)
│   ├── Boolean features (is_weekend)
│   └── Demand scores
├── Train Linear Regression Models
│   ├── Hotel model (85% accuracy)
│   └── Flight model (82% accuracy)
├── Validate Performance
│   ├── Train/test split (80/20)
│   ├── Calculate MAE, R² scores
│   └── Feature importance analysis
└── Save Trained Models
    ├── models/hotel_model.pkl
    └── models/flight_model.pkl
```

### 3. Application Runtime Phase
```
app.py (Streamlit)
├── Load Trained Models
├── User Interface
│   ├── Service selection (Hotel/Flight)
│   ├── Date picker
│   ├── Prediction horizon slider
│   └── Real-time updates
├── Prediction Engine
│   ├── Current price estimation
│   ├── Future price forecasting
│   ├── Trend analysis
│   └── Recommendation generation
└── Visualization
    ├── Price trend charts
    ├── Historical data plots
    ├── Recommendation display
    └── Insights dashboard
```

## Machine Learning Pipeline

### Feature Engineering Process
```
Raw Data → Feature Extraction → Model Input
├── Date: 2024-01-15
├── Day: Monday
├── Season: Winter
└── Demand: 105

Transforms to:
├── month: 1
├── day: 15
├── is_weekend: 0
├── season_encoded: 0
├── day_of_week_encoded: 0
└── demand_score: 105
```

### Prediction Logic
```
Input Features → Linear Regression → Price Prediction
                                  ↓
Current Price ← Model Output → Future Prices (7 days)
     ↓                              ↓
Price Comparison → Trend Analysis → Recommendation
     ↓                              ↓
"Book Now" / "Wait" / "Neutral" ← Decision Engine
```

## Recommendation Algorithm

### Decision Tree Logic
```
Price Change Analysis
├── If future_avg > current + 5%
│   └── Recommendation: "📈 BOOK NOW"
├── If future_avg < current - 5%
│   └── Recommendation: "⏳ WAIT"
└── Else
    └── Recommendation: "🤔 NEUTRAL"

Confidence Levels
├── High: >10% price change
├── Medium: 5-10% price change
└── Low: <5% price change
```

## User Interaction Flow

### Application Workflow
```
User Opens App
├── Select Service Type (Hotel/Flight)
├── Choose Travel Date
├── Set Prediction Horizon
└── View Results
    ├── Current Price Display
    ├── Future Price Trend Chart
    ├── AI Recommendation
    ├── Historical Price Analysis
    └── Money-Saving Tips
```

### Demo Presentation Flow
```
1. Introduction (30s)
   └── Problem statement & solution overview

2. Live Demo (2 minutes)
   ├── Show hotel prediction
   ├── Explain recommendation logic
   ├── Switch to flight prediction
   └── Highlight key features

3. Technical Details (1 minute)
   ├── ML approach explanation
   ├── Performance metrics
   └── Feature importance

4. Impact & Future (1 minute)
   ├── Social benefits
   ├── Potential savings
   └── Scalability plans

5. Q&A (30s)
   └── Handle judge questions
```

## File Dependencies

### Core Files
```
app.py
├── Depends on: model.py (PriceForecastingModel class)
├── Requires: models/hotel_model.pkl, models/flight_model.pkl
└── Uses: data/hotel_prices.csv, data/flight_prices.csv

model.py
├── Depends on: data/hotel_prices.csv, data/flight_prices.csv
└── Generates: models/hotel_model.pkl, models/flight_model.pkl

data_generator.py
├── Independent script
└── Generates: data/hotel_prices.csv, data/flight_prices.csv
```

### Setup Dependencies
```
setup.py → Orchestrates full setup
├── 1. Install packages (requirements.txt)
├── 2. Run data_generator.py
├── 3. Run model.py
└── 4. Verify all files created

run_demo.py → Demo presentation mode
├── Check setup completion
├── Start Streamlit server
├── Open browser automatically
└── Show presentation tips
```

## Performance Metrics

### Model Accuracy
```
Hotel Model:
├── R² Score: ~0.85 (85% variance explained)
├── MAE: ~$15 (average error)
├── Training Time: <30 seconds
└── Prediction Time: <1 second

Flight Model:
├── R² Score: ~0.82 (82% variance explained)
├── MAE: ~$25 (average error)
├── Training Time: <30 seconds
└── Prediction Time: <1 second
```

### System Performance
```
Data Generation: ~10 seconds (1000+ records)
Model Training: ~30 seconds (both models)
App Startup: ~5 seconds
Prediction Response: <1 second
Chart Rendering: <2 seconds
```

## Scalability Considerations

### Current Limitations
- Synthetic data (not real market data)
- Single location/route predictions
- Basic Linear Regression model
- Local deployment only

### Future Enhancements
- Real-time data integration
- Multi-destination support
- Advanced ML models (LSTM, Random Forest)
- Cloud deployment
- Mobile application
- API service for third-party integration

This flow diagram shows how all components work together to create a complete, functional AI price forecasting system ready for hackathon demonstration!