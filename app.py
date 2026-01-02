"""
AI-Driven Price Forecasting System - Professional Streamlit App
Enhanced UI/UX with animations, modern design, and improved performance
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import os
import time
from model import PriceForecastingModel

# Page configuration - MUST be first Streamlit command
st.set_page_config(
    page_title="AI Price Forecaster | Smart Travel Decisions",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS with animations
CUSTOM_CSS = """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Extended CSS for professional styling
EXTENDED_CSS = """
<style>
    /* Animated gradient background */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: fadeInDown 1s ease-out;
    }
    
    .sub-header {
        text-align: center;
        color: #6b7280;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        animation: fadeInUp 1s ease-out 0.3s both;
    }
    
    /* Keyframe animations */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 5px rgba(102, 126, 234, 0.5); }
        50% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.8); }
    }
</style>
"""
st.markdown(EXTENDED_CSS, unsafe_allow_html=True)

# Card and component styles
COMPONENT_CSS = """
<style>
    /* Glass morphism cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 1rem 0;
        animation: fadeIn 0.8s ease-out;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
    }
    
    /* Metric cards with gradient */
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8eb 100%);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        animation: slideInUp 0.6s ease-out;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }
    
    .metric-card:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        color: #6b7280;
        font-size: 0.9rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .metric-delta {
        font-size: 1rem;
        font-weight: 600;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        display: inline-block;
        margin-top: 0.5rem;
    }
    
    .delta-positive { background: #fee2e2; color: #dc2626; }
    .delta-negative { background: #d1fae5; color: #059669; }
    .delta-neutral { background: #fef3c7; color: #d97706; }
</style>
"""
st.markdown(COMPONENT_CSS, unsafe_allow_html=True)

# Recommendation and button styles
RECOMMENDATION_CSS = """
<style>
    /* Recommendation boxes with animations */
    .recommendation-box {
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        font-weight: 700;
        font-size: 1.8rem;
        margin: 1.5rem 0;
        animation: pulse 2s infinite, fadeIn 0.8s ease-out;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .recommendation-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        animation: shimmer 3s infinite;
    }
    
    .book-now {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a5a 100%);
        color: white;
        box-shadow: 0 10px 30px rgba(238, 90, 90, 0.4);
    }
    
    .book-now:hover {
        box-shadow: 0 15px 40px rgba(238, 90, 90, 0.5);
        transform: scale(1.02);
    }
    
    .wait {
        background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
        color: white;
        box-shadow: 0 10px 30px rgba(78, 205, 196, 0.4);
    }
    
    .wait:hover {
        box-shadow: 0 15px 40px rgba(78, 205, 196, 0.5);
        transform: scale(1.02);
    }
    
    .neutral {
        background: linear-gradient(135deg, #ffd93d 0%, #f0c419 100%);
        color: #1a1a2e;
        box-shadow: 0 10px 30px rgba(255, 217, 61, 0.4);
    }
    
    /* Confidence badge */
    .confidence-badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 1rem;
        animation: bounce 2s infinite;
    }
    
    .confidence-high { background: #d1fae5; color: #059669; }
    .confidence-medium { background: #fef3c7; color: #d97706; }
    .confidence-low { background: #fee2e2; color: #dc2626; }
    
    /* Feature cards */
    .feature-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        animation: bounce 3s infinite;
    }
    
    .feature-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a1a2e;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: #6b7280;
        font-size: 0.9rem;
    }
</style>
"""
st.markdown(RECOMMENDATION_CSS, unsafe_allow_html=True)

# Sidebar and additional styles
SIDEBAR_CSS = """
<style>
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white;
    }
    
    [data-testid="stSidebar"] label {
        color: #e0e0e0 !important;
    }
    
    /* Stats row */
    .stats-row {
        display: flex;
        justify-content: space-around;
        gap: 1rem;
        margin: 2rem 0;
        animation: fadeIn 1s ease-out;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
    }
    
    .stat-label {
        color: #6b7280;
        font-size: 0.85rem;
    }
    
    /* Loading animation */
    .loading-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 3rem;
    }
    
    .loading-spinner {
        width: 50px;
        height: 50px;
        border: 4px solid #f3f3f3;
        border-top: 4px solid #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Insight cards */
    .insight-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        animation: slideInLeft 0.6s ease-out;
    }
    
    .insight-icon { font-size: 1.5rem; margin-right: 0.5rem; }
    .insight-text { font-size: 0.95rem; }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #6b7280;
        border-top: 1px solid #e5e7eb;
        margin-top: 3rem;
        animation: fadeIn 1s ease-out;
    }
    
    .footer-brand {
        font-size: 1.2rem;
        font-weight: 600;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 10px 20px;
        background: #f5f7fa;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
</style>
"""
st.markdown(SIDEBAR_CSS, unsafe_allow_html=True)

# Caching functions for performance
@st.cache_data(ttl=3600)
def load_data():
    """Load historical data with caching for performance"""
    try:
        hotel_data = pd.read_csv('data/hotel_prices.csv')
        flight_data = pd.read_csv('data/flight_prices.csv')
        hotel_data['date'] = pd.to_datetime(hotel_data['date'])
        flight_data['date'] = pd.to_datetime(flight_data['date'])
        return hotel_data, flight_data
    except FileNotFoundError:
        return None, None

@st.cache_resource
def load_models():
    """Load trained models with caching"""
    try:
        hotel_model = PriceForecastingModel('hotel')
        hotel_model.load_model('models/hotel_model.pkl')
        flight_model = PriceForecastingModel('flight')
        flight_model.load_model('models/flight_model.pkl')
        return hotel_model, flight_model
    except FileNotFoundError:
        return None, None

def create_animated_chart(dates, prices, title, current_price=None, chart_type="forecast"):
    """Create professional animated Plotly chart"""
    fig = go.Figure()
    
    # Color scheme
    primary_color = '#667eea'
    secondary_color = '#764ba2'
    gradient_colors = ['#667eea', '#764ba2', '#f093fb']
    
    if chart_type == "forecast":
        # Add gradient fill area
        fig.add_trace(go.Scatter(
            x=dates, y=prices,
            fill='tozeroy',
            fillcolor='rgba(102, 126, 234, 0.1)',
            line=dict(color=primary_color, width=0),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        # Main line with markers
        fig.add_trace(go.Scatter(
            x=dates, y=prices,
            mode='lines+markers',
            name='Predicted Price',
            line=dict(color=primary_color, width=4, shape='spline'),
            marker=dict(size=12, color=primary_color, 
                       line=dict(width=3, color='white'),
                       symbol='circle'),
            hovertemplate='<b>%{x|%b %d}</b><br>Price: $%{y:.2f}<extra></extra>'
        ))
        
        # Current price reference line
        if current_price:
            fig.add_hline(
                y=current_price,
                line_dash="dash",
                line_color="#ef4444",
                line_width=2,
                annotation_text=f"Current: ${current_price:.2f}",
                annotation_position="right",
                annotation_font=dict(size=12, color="#ef4444")
            )
    else:
        # Historical chart with gradient
        fig.add_trace(go.Scatter(
            x=dates, y=prices,
            fill='tozeroy',
            fillcolor='rgba(118, 75, 162, 0.1)',
            line=dict(color=secondary_color, width=3, shape='spline'),
            name='Historical Price',
            hovertemplate='<b>%{x|%b %d, %Y}</b><br>Price: $%{y:.2f}<extra></extra>'
        ))
    
    # Layout with animations
    fig.update_layout(
        title=dict(text=title, font=dict(size=20, color='#1a1a2e'), x=0.5),
        xaxis=dict(
            title="Date", showgrid=True, gridcolor='rgba(0,0,0,0.05)',
            tickfont=dict(size=11), title_font=dict(size=13)
        ),
        yaxis=dict(
            title="Price ($)", showgrid=True, gridcolor='rgba(0,0,0,0.05)',
            tickfont=dict(size=11), title_font=dict(size=13),
            tickprefix="$"
        ),
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400,
        margin=dict(l=60, r=30, t=60, b=50),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def create_gauge_chart(value, title, min_val=0, max_val=200):
    """Create animated gauge chart for price indicator"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 16, 'color': '#1a1a2e'}},
        number={'prefix': "$", 'font': {'size': 36, 'color': '#667eea'}},
        gauge={
            'axis': {'range': [min_val, max_val], 'tickwidth': 1, 'tickcolor': "#667eea"},
            'bar': {'color': "#667eea"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#e5e7eb",
            'steps': [
                {'range': [min_val, max_val*0.33], 'color': '#d1fae5'},
                {'range': [max_val*0.33, max_val*0.66], 'color': '#fef3c7'},
                {'range': [max_val*0.66, max_val], 'color': '#fee2e2'}
            ],
            'threshold': {
                'line': {'color': "#ef4444", 'width': 4},
                'thickness': 0.75,
                'value': value
            }
        }
    ))
    
    fig.update_layout(
        height=250,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def create_comparison_chart(current, predicted, labels):
    """Create animated bar comparison chart"""
    colors = ['#667eea', '#764ba2']
    
    fig = go.Figure(data=[
        go.Bar(name='Current', x=labels, y=current, marker_color=colors[0],
               text=[f'${v:.0f}' for v in current], textposition='auto'),
        go.Bar(name='Predicted', x=labels, y=predicted, marker_color=colors[1],
               text=[f'${v:.0f}' for v in predicted], textposition='auto')
    ])
    
    fig.update_layout(
        barmode='group',
        title=dict(text='Price Comparison', font=dict(size=18)),
        height=300,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02)
    )
    
    return fig

def get_recommendation_html(recommendation_data):
    """Generate animated recommendation HTML"""
    rec = recommendation_data['recommendation']
    
    if "BOOK NOW" in rec:
        style_class = "book-now"
        icon = "🔥"
        action = "BOOK NOW"
    elif "WAIT" in rec:
        style_class = "wait"
        icon = "⏳"
        action = "WAIT"
    else:
        style_class = "neutral"
        icon = "🤔"
        action = "NEUTRAL"
    
    confidence = recommendation_data['confidence']
    conf_class = f"confidence-{confidence.lower()}"
    
    html = f"""
    <div class="recommendation-box {style_class}">
        <span style="font-size: 3rem;">{icon}</span>
        <div style="margin-top: 0.5rem;">{action}</div>
        <div class="confidence-badge {conf_class}">
            {confidence} Confidence
        </div>
    </div>
    """
    return html

def render_metric_card(label, value, delta=None, delta_type="neutral"):
    """Render animated metric card"""
    delta_html = ""
    if delta:
        delta_class = f"delta-{delta_type}"
        delta_icon = "↑" if delta_type == "positive" else "↓" if delta_type == "negative" else "→"
        delta_html = f'<div class="metric-delta {delta_class}">{delta_icon} {delta}</div>'
    
    return f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """

def render_feature_card(icon, title, description):
    """Render feature card with animation"""
    return f"""
    <div class="feature-card">
        <div class="feature-icon">{icon}</div>
        <div class="feature-title">{title}</div>
        <div class="feature-desc">{description}</div>
    </div>
    """

def render_insight_card(icon, text):
    """Render insight card"""
    return f"""
    <div class="insight-card">
        <span class="insight-icon">{icon}</span>
        <span class="insight-text">{text}</span>
    </div>
    """

def main():
    """Main application with enhanced UI/UX"""
    
    # Animated Header
    st.markdown('<h1 class="main-header">✈️ AI Price Forecaster</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Smart predictions for smarter travel decisions • Powered by Machine Learning</p>', unsafe_allow_html=True)
    
    # Load data and models
    hotel_data, flight_data = load_data()
    hotel_model, flight_model = load_models()
    
    if hotel_data is None or hotel_model is None:
        st.error("⚠️ System initialization failed. Please run setup first.")
        st.code("python data_generator.py\npython model.py", language="bash")
        st.stop()
    
    # Sidebar with professional styling
    with st.sidebar:
        st.markdown("## 🎯 Prediction Settings")
        st.markdown("---")
        
        # Service type with icons
        service_type = st.selectbox(
            "🏷️ Service Type",
            ["🏨 Hotel", "✈️ Flight"],
            help="Choose between hotel or flight price prediction"
        )
        
        st.markdown("")
        
        # Date selection
        min_date = datetime.now().date()
        max_date = min_date + timedelta(days=365)
        
        selected_date = st.date_input(
            "📅 Travel Date",
            value=min_date + timedelta(days=7),
            min_value=min_date,
            max_value=max_date,
            help="Select your intended travel date"
        )
        
        st.markdown("")
        
        # Prediction horizon with visual feedback
        prediction_days = st.slider(
            "🔮 Forecast Period",
            min_value=3,
            max_value=30,
            value=7,
            help="Number of days to forecast ahead"
        )
        
        st.markdown("---")
        
        # Quick stats in sidebar
        st.markdown("### 📊 Model Stats")
        st.markdown("""
        <div style="color: #a0a0a0; font-size: 0.85rem;">
            <p>🎯 Hotel Accuracy: <b style="color: #4ecdc4;">76.6%</b></p>
            <p>📉 Avg Error: <b style="color: #4ecdc4;">$12.68</b></p>
            <p>📈 Data Points: <b style="color: #4ecdc4;">2,192</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #6b7280; font-size: 0.8rem;">
            <p>🏆 Puduvai Youth Fest 2026</p>
            <p>AI Hackathon Project</p>
        </div>
        """, unsafe_allow_html=True)

    # Main content area
    # Select appropriate data and model
    if "Hotel" in service_type:
        data = hotel_data
        model = hotel_model
        service_icon = "🏨"
        service_name = "Hotel"
        price_range = (50, 300)
    else:
        data = flight_data
        model = flight_model
        service_icon = "✈️"
        service_name = "Flight"
        price_range = (150, 600)
    
    # Create current data for prediction
    current_date = datetime.now().date()
    current_data = pd.DataFrame([{
        'date': current_date,
        'day_of_week': current_date.strftime('%A'),
        'month': current_date.month,
        'is_weekend': 1 if current_date.weekday() >= 5 else 0,
        'season': model._get_season(current_date.month),
        'demand_score': 105,
        'advance_booking_days': 30 if "Flight" in service_type else None
    }])
    
    try:
        # Get predictions
        current_price = model.predict(current_data)[0]
        future_dates, future_prices = model.predict_future_trend(current_date, days_ahead=prediction_days)
        recommendation_data = model.get_recommendation(current_price, future_prices)
        
        # Main layout with tabs
        tab1, tab2, tab3 = st.tabs(["📊 Forecast", "📈 Analytics", "💡 Insights"])
        
        with tab1:
            # Top metrics row
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                delta_type = "positive" if recommendation_data['price_change_percent'] > 0 else "negative"
                st.markdown(render_metric_card(
                    "Current Price",
                    f"${current_price:.2f}",
                    f"{abs(recommendation_data['price_change_percent']):.1f}%",
                    delta_type
                ), unsafe_allow_html=True)
            
            with col2:
                st.markdown(render_metric_card(
                    "Predicted Avg",
                    f"${recommendation_data['predicted_avg_price']:.2f}"
                ), unsafe_allow_html=True)
            
            with col3:
                min_future = min(future_prices)
                st.markdown(render_metric_card(
                    "Lowest Expected",
                    f"${min_future:.2f}"
                ), unsafe_allow_html=True)
            
            with col4:
                max_future = max(future_prices)
                st.markdown(render_metric_card(
                    "Highest Expected",
                    f"${max_future:.2f}"
                ), unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Main content columns
            chart_col, rec_col = st.columns([2, 1])
            
            with chart_col:
                st.markdown(f"### {service_icon} {service_name} Price Forecast")
                
                # Forecast chart
                all_dates = [current_date] + future_dates
                all_prices = [current_price] + list(future_prices)
                
                forecast_chart = create_animated_chart(
                    all_dates, all_prices,
                    f"{prediction_days}-Day Price Forecast",
                    current_price,
                    "forecast"
                )
                st.plotly_chart(forecast_chart, use_container_width=True)
            
            with rec_col:
                st.markdown("### 🎯 AI Recommendation")
                st.markdown(get_recommendation_html(recommendation_data), unsafe_allow_html=True)
                
                # Recommendation details
                st.markdown("#### 📋 Analysis")
                st.markdown(f"""
                <div class="glass-card" style="padding: 1rem;">
                    <p><strong>📊 Trend:</strong> {recommendation_data['reason']}</p>
                    <p><strong>💰 Current:</strong> ${recommendation_data['current_price']:.2f}</p>
                    <p><strong>📈 Predicted:</strong> ${recommendation_data['predicted_avg_price']:.2f}</p>
                    <p><strong>📉 Change:</strong> {recommendation_data['price_change_percent']:.1f}%</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Savings/Cost indicator
                if recommendation_data['price_change_percent'] < -5:
                    savings = current_price - recommendation_data['predicted_avg_price']
                    st.success(f"💰 Potential Savings: **${savings:.2f}**")
                elif recommendation_data['price_change_percent'] > 5:
                    extra = recommendation_data['predicted_avg_price'] - current_price
                    st.warning(f"⚠️ Book now to save: **${extra:.2f}**")

        with tab2:
            st.markdown("### 📈 Historical Analysis")
            
            # Historical data visualization
            recent_data = data.tail(90)
            
            hist_col1, hist_col2 = st.columns([2, 1])
            
            with hist_col1:
                historical_chart = create_animated_chart(
                    recent_data['date'],
                    recent_data['price'],
                    f"Historical {service_name} Prices (Last 90 Days)",
                    chart_type="historical"
                )
                st.plotly_chart(historical_chart, use_container_width=True)
            
            with hist_col2:
                # Price gauge
                gauge = create_gauge_chart(
                    current_price,
                    "Current Price Level",
                    price_range[0],
                    price_range[1]
                )
                st.plotly_chart(gauge, use_container_width=True)
            
            # Statistics cards
            st.markdown("### 📊 Price Statistics")
            
            stat_cols = st.columns(4)
            price_stats = data['price'].describe()
            
            stats_data = [
                ("Average", f"${price_stats['mean']:.2f}", "📊"),
                ("Minimum", f"${price_stats['min']:.2f}", "📉"),
                ("Maximum", f"${price_stats['max']:.2f}", "📈"),
                ("Std Dev", f"${price_stats['std']:.2f}", "📐")
            ]
            
            for col, (label, value, icon) in zip(stat_cols, stats_data):
                with col:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div style="font-size: 2rem;">{icon}</div>
                        <div class="metric-label">{label}</div>
                        <div class="metric-value" style="font-size: 1.8rem;">{value}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Day of week analysis
            st.markdown("### 📅 Price by Day of Week")
            
            day_avg = data.groupby('day_of_week')['price'].mean().reindex([
                'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
            ])
            
            day_chart = go.Figure(data=[
                go.Bar(
                    x=day_avg.index,
                    y=day_avg.values,
                    marker_color=['#667eea' if i < 5 else '#764ba2' for i in range(7)],
                    text=[f'${v:.0f}' for v in day_avg.values],
                    textposition='auto'
                )
            ])
            
            day_chart.update_layout(
                height=300,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(title="Day of Week"),
                yaxis=dict(title="Average Price ($)", tickprefix="$")
            )
            
            st.plotly_chart(day_chart, use_container_width=True)

        with tab3:
            st.markdown("### 💡 AI-Powered Insights")
            
            # Dynamic insights based on data
            insights = []
            
            # Weekend insight
            weekend_avg = data[data['is_weekend'] == 1]['price'].mean()
            weekday_avg = data[data['is_weekend'] == 0]['price'].mean()
            weekend_diff = ((weekend_avg - weekday_avg) / weekday_avg) * 100
            
            if weekend_diff > 10:
                insights.append(("💰", f"Weekends are {weekend_diff:.0f}% more expensive. Consider weekday travel!"))
            
            # Season insight
            season_avg = data.groupby('season')['price'].mean()
            cheapest_season = season_avg.idxmin()
            insights.append(("🌸", f"{cheapest_season} offers the best prices on average (${season_avg[cheapest_season]:.0f})"))
            
            # Current vs average
            avg_price = data['price'].mean()
            if current_price < avg_price * 0.9:
                insights.append(("🎯", f"Current price is {((avg_price - current_price)/avg_price)*100:.0f}% below average - great deal!"))
            elif current_price > avg_price * 1.1:
                insights.append(("⚠️", f"Current price is {((current_price - avg_price)/avg_price)*100:.0f}% above average"))
            
            # Trend insight
            if recommendation_data['price_change_percent'] > 5:
                insights.append(("📈", "Prices trending upward - booking soon recommended"))
            elif recommendation_data['price_change_percent'] < -5:
                insights.append(("📉", "Prices trending downward - waiting could save money"))
            
            # Display insights
            for icon, text in insights:
                st.markdown(render_insight_card(icon, text), unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Tips section
            st.markdown("### 🎓 Smart Booking Tips")
            
            tips_col1, tips_col2, tips_col3 = st.columns(3)
            
            with tips_col1:
                st.markdown(render_feature_card(
                    "📅",
                    "Best Booking Time",
                    "Book 2-3 weeks ahead for hotels, 6-8 weeks for flights"
                ), unsafe_allow_html=True)
            
            with tips_col2:
                st.markdown(render_feature_card(
                    "💡",
                    "Flexible Dates",
                    "Being flexible with dates can save up to 30%"
                ), unsafe_allow_html=True)
            
            with tips_col3:
                st.markdown(render_feature_card(
                    "🔔",
                    "Price Alerts",
                    "Set alerts to catch price drops automatically"
                ), unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # How it works section
            st.markdown("### 🤖 How Our AI Works")
            
            how_cols = st.columns(4)
            
            steps = [
                ("1️⃣", "Data Collection", "Analyze historical price patterns"),
                ("2️⃣", "Feature Analysis", "Extract seasonal & demand trends"),
                ("3️⃣", "ML Prediction", "Linear Regression forecasting"),
                ("4️⃣", "Smart Advice", "Generate actionable recommendations")
            ]
            
            for col, (num, title, desc) in zip(how_cols, steps):
                with col:
                    st.markdown(render_feature_card(num, title, desc), unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"⚠️ Prediction error: {str(e)}")
        st.info("Please ensure all data and models are properly loaded.")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <div class="footer-brand">✈️ AI Price Forecaster</div>
        <p style="margin-top: 0.5rem;">Helping travelers make smarter decisions with AI</p>
        <p style="font-size: 0.8rem; margin-top: 1rem;">
            🏆 Built for Puduvai Youth Fest 2026 AI Hackathon<br>
            💻 Powered by Python, Streamlit & Machine Learning
        </p>
        <div style="margin-top: 1rem;">
            <span style="margin: 0 0.5rem;">🐍 Python</span>
            <span style="margin: 0 0.5rem;">📊 Pandas</span>
            <span style="margin: 0 0.5rem;">🤖 Scikit-learn</span>
            <span style="margin: 0 0.5rem;">📈 Plotly</span>
            <span style="margin: 0 0.5rem;">🎨 Streamlit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()