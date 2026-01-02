"""
AI-Driven Price Forecasting System - Streamlit App
Interactive web application for hotel and flight price predictions
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import os
from model import PriceForecastingModel

# Page configuration
st.set_page_config(
    page_title="AI Price Forecasting System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .recommendation-box {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        font-weight: bold;
        text-align: center;
        font-size: 1.2rem;
    }
    .book-now {
        background-color: #ff6b6b;
        color: white;
    }
    .wait {
        background-color: #4ecdc4;
        color: white;
    }
    .neutral {
        background-color: #ffd93d;
        color: black;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load historical data"""
    try:
        hotel_data = pd.read_csv('data/hotel_prices.csv')
        flight_data = pd.read_csv('data/flight_prices.csv')
        return hotel_data, flight_data
    except FileNotFoundError:
        st.error("❌ Data files not found. Please run data_generator.py first.")
        return None, None

@st.cache_resource
def load_models():
    """Load trained models"""
    try:
        hotel_model = PriceForecastingModel('hotel')
        hotel_model.load_model('models/hotel_model.pkl')
        
        flight_model = PriceForecastingModel('flight')
        flight_model.load_model('models/flight_model.pkl')
        
        return hotel_model, flight_model
    except FileNotFoundError:
        st.error("❌ Model files not found. Please run model.py first.")
        return None, None

def create_price_chart(dates, prices, title, current_price=None):
    """Create interactive price chart"""
    
    fig = go.Figure()
    
    # Add price line
    fig.add_trace(go.Scatter(
        x=dates,
        y=prices,
        mode='lines+markers',
        name='Price',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=6)
    ))
    
    # Add current price line if provided
    if current_price is not None:
        fig.add_hline(
            y=current_price,
            line_dash="dash",
            line_color="red",
            annotation_text=f"Current: ${current_price:.2f}"
        )
    
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Price ($)",
        hovermode='x unified',
        showlegend=True,
        height=400
    )
    
    return fig

def get_recommendation_style(recommendation):
    """Get CSS class for recommendation"""
    if "BOOK NOW" in recommendation:
        return "book-now"
    elif "WAIT" in recommendation:
        return "wait"
    else:
        return "neutral"

def main():
    """Main application"""
    
    # Header
    st.markdown('<h1 class="main-header">🤖 AI Price Forecasting System</h1>', unsafe_allow_html=True)
    st.markdown("### Predict hotel and flight prices with AI • Make smarter booking decisions")
    
    # Load data and models
    hotel_data, flight_data = load_data()
    hotel_model, flight_model = load_models()
    
    if hotel_data is None or hotel_model is None:
        st.stop()
    
    # Sidebar
    st.sidebar.header("🎯 Prediction Settings")
    
    # Service type selection
    service_type = st.sidebar.selectbox(
        "Select Service Type",
        ["🏨 Hotel", "✈️ Flight"],
        help="Choose between hotel or flight price prediction"
    )
    
    # Date selection
    min_date = datetime.now().date()
    max_date = min_date + timedelta(days=365)
    
    selected_date = st.sidebar.date_input(
        "Select Travel Date",
        value=min_date + timedelta(days=7),
        min_value=min_date,
        max_value=max_date,
        help="Choose your intended travel date"
    )
    
    # Prediction horizon
    prediction_days = st.sidebar.slider(
        "Prediction Horizon (days)",
        min_value=3,
        max_value=30,
        value=7,
        help="How many days ahead to predict"
    )
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header(f"📊 {service_type.split()[1]} Price Analysis")
        
        # Select appropriate data and model
        if "Hotel" in service_type:
            data = hotel_data
            model = hotel_model
            service_icon = "🏨"
        else:
            data = flight_data
            model = flight_model
            service_icon = "✈️"
        
        # Get current price (simulate current market price)
        current_date = datetime.now().date()
        
        # Create sample current data
        current_data = pd.DataFrame([{
            'date': current_date,
            'day_of_week': current_date.strftime('%A'),
            'month': current_date.month,
            'is_weekend': 1 if current_date.weekday() >= 5 else 0,
            'season': model._get_season(current_date.month),
            'demand_score': 105,  # Slightly above average
            'advance_booking_days': 30 if "Flight" in service_type else None
        }])
        
        try:
            current_price = model.predict(current_data)[0]
            
            # Predict future prices
            future_dates, future_prices = model.predict_future_trend(
                current_date, days_ahead=prediction_days
            )
            
            # Get recommendation
            recommendation_data = model.get_recommendation(current_price, future_prices)
            
            # Display current price
            st.metric(
                label=f"Current {service_type.split()[1]} Price",
                value=f"${current_price:.2f}",
                delta=f"{recommendation_data['price_change_percent']:.1f}% expected change"
            )
            
            # Create price trend chart
            all_dates = [current_date] + future_dates
            all_prices = [current_price] + list(future_prices)
            
            chart = create_price_chart(
                all_dates, 
                all_prices, 
                f"{service_type.split()[1]} Price Trend Forecast",
                current_price
            )
            st.plotly_chart(chart, use_container_width=True)
            
            # Historical price chart
            st.subheader("📈 Historical Price Trends")
            
            # Show last 90 days of historical data
            data['date'] = pd.to_datetime(data['date'])
            recent_data = data.tail(90)
            
            historical_chart = create_price_chart(
                recent_data['date'],
                recent_data['price'],
                f"Historical {service_type.split()[1]} Prices (Last 90 Days)"
            )
            st.plotly_chart(historical_chart, use_container_width=True)
            
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
            st.stop()
    
    with col2:
        st.header("🎯 AI Recommendation")
        
        # Recommendation box
        rec_style = get_recommendation_style(recommendation_data['recommendation'])
        st.markdown(f"""
        <div class="recommendation-box {rec_style}">
            {recommendation_data['recommendation']}
        </div>
        """, unsafe_allow_html=True)
        
        # Recommendation details
        st.markdown("**📋 Analysis Details:**")
        st.write(f"• {recommendation_data['reason']}")
        st.write(f"• Confidence: {recommendation_data['confidence']}")
        st.write(f"• Current Price: ${recommendation_data['current_price']:.2f}")
        st.write(f"• Predicted Avg: ${recommendation_data['predicted_avg_price']:.2f}")
        
        # Price statistics
        st.markdown("**📊 Price Statistics:**")
        price_stats = data['price'].describe()
        st.write(f"• Average: ${price_stats['mean']:.2f}")
        st.write(f"• Minimum: ${price_stats['min']:.2f}")
        st.write(f"• Maximum: ${price_stats['max']:.2f}")
        st.write(f"• Std Dev: ${price_stats['std']:.2f}")
        
        # Savings potential
        if recommendation_data['price_change_percent'] < -5:
            potential_savings = current_price - recommendation_data['predicted_avg_price']
            st.success(f"💰 Potential Savings: ${potential_savings:.2f}")
        elif recommendation_data['price_change_percent'] > 5:
            potential_cost = recommendation_data['predicted_avg_price'] - current_price
            st.warning(f"⚠️ Potential Extra Cost: ${potential_cost:.2f}")
    
    # Additional insights
    st.header("🧠 AI Insights & Tips")
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.markdown("**🎯 Best Booking Times**")
        if "Hotel" in service_type:
            st.write("• Book 2-3 weeks in advance")
            st.write("• Avoid peak seasons (summer/winter)")
            st.write("• Consider weekday stays")
        else:
            st.write("• Book 6-8 weeks in advance")
            st.write("• Fly Tuesday/Wednesday")
            st.write("• Avoid holiday periods")
    
    with col4:
        st.markdown("**📈 Price Factors**")
        st.write("• Seasonal demand")
        st.write("• Day of the week")
        st.write("• Advance booking time")
        st.write("• Market conditions")
    
    with col5:
        st.markdown("**💡 Money-Saving Tips**")
        st.write("• Use price alerts")
        st.write("• Be flexible with dates")
        st.write("• Compare multiple options")
        st.write("• Book during off-peak times")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🤖 Powered by AI & Machine Learning | Built for Puduvai Youth Fest 2026</p>
        <p>💡 Helping travelers make smarter booking decisions with data-driven insights</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()