
"""
🚀 AI-Driven Price Forecasting System - Enterprise Edition
MNC-Grade UI/UX with Premium Animations & Professional Design
Built for Puduvai Youth Fest 2026 AI Hackathon
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

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="PriceWise AI | Smart Travel Forecasting",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════════════════
# THEME CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
THEME = {
    "primary": "#6366f1",      # Indigo
    "secondary": "#8b5cf6",    # Purple
    "accent": "#06b6d4",       # Cyan
    "success": "#10b981",      # Emerald
    "warning": "#f59e0b",      # Amber
    "danger": "#ef4444",       # Red
    "dark": "#0f172a",         # Slate 900
    "light": "#f8fafc",        # Slate 50
    "card_bg": "rgba(255, 255, 255, 0.95)",
    "glass_bg": "rgba(255, 255, 255, 0.1)",
}

# ═══════════════════════════════════════════════════════════════════════════════
# MASTER CSS - MNC-GRADE STYLING
# ═══════════════════════════════════════════════════════════════════════════════
MASTER_CSS = """
<style>
    /* ═══════════════════════════════════════════════════════════════════════
       GOOGLE FONTS IMPORT
    ═══════════════════════════════════════════════════════════════════════ */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
    
    /* ═══════════════════════════════════════════════════════════════════════
       ROOT VARIABLES & GLOBAL STYLES
    ═══════════════════════════════════════════════════════════════════════ */
    :root {
        --primary: #6366f1;
        --primary-dark: #4f46e5;
        --secondary: #8b5cf6;
        --accent: #06b6d4;
        --success: #10b981;
        --warning: #f59e0b;
        --danger: #ef4444;
        --dark: #0f172a;
        --light: #f8fafc;
        --gray-100: #f1f5f9;
        --gray-200: #e2e8f0;
        --gray-300: #cbd5e1;
        --gray-400: #94a3b8;
        --gray-500: #64748b;
        --gray-600: #475569;
        --gray-700: #334155;
        --gray-800: #1e293b;
        --gradient-primary: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #06b6d4 100%);
        --gradient-dark: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
        --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1);
        --shadow-glow: 0 0 40px rgba(99, 102, 241, 0.3);
    }
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
    }
    
    /* Hide Streamlit defaults */
    #MainMenu, footer, header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* ═══════════════════════════════════════════════════════════════════════
       KEYFRAME ANIMATIONS
    ═══════════════════════════════════════════════════════════════════════ */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-40px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-40px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes fadeInRight {
        from { opacity: 0; transform: translateX(40px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes ripple {
        0% { transform: scale(0); opacity: 1; }
        100% { transform: scale(4); opacity: 0; }
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-15px); }
        60% { transform: translateY(-7px); }
    }
    
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    @keyframes typewriter {
        from { width: 0; }
        to { width: 100%; }
    }
    
    @keyframes blink {
        50% { border-color: transparent; }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 5px var(--primary), 0 0 10px var(--primary); }
        50% { box-shadow: 0 0 20px var(--primary), 0 0 30px var(--primary); }
    }
    
    @keyframes slideInFromBottom {
        0% { transform: translateY(100%); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes countUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
"""
st.markdown(MASTER_CSS, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# COMPONENT STYLES - PREMIUM UI ELEMENTS
# ═══════════════════════════════════════════════════════════════════════════════
COMPONENT_CSS = """
<style>
    /* ═══════════════════════════════════════════════════════════════════════
       HERO SECTION
    ═══════════════════════════════════════════════════════════════════════ */
    .hero-container {
        text-align: center;
        padding: 2rem 0 3rem;
        animation: fadeInDown 1s ease-out;
    }
    
    .hero-badge {
        display: inline-block;
        background: var(--gradient-primary);
        background-size: 200% 200%;
        animation: gradientFlow 3s ease infinite;
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 0.5px;
        margin-bottom: 1.5rem;
        box-shadow: var(--shadow-lg);
    }
    
    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        line-height: 1.1;
        letter-spacing: -2px;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: var(--gray-500);
        margin-top: 1rem;
        font-weight: 400;
        animation: fadeInUp 1s ease-out 0.3s both;
    }
    
    .hero-stats {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin-top: 2rem;
        animation: fadeInUp 1s ease-out 0.5s both;
    }
    
    .hero-stat {
        text-align: center;
    }
    
    .hero-stat-value {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary);
    }
    
    .hero-stat-label {
        font-size: 0.85rem;
        color: var(--gray-500);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* ═══════════════════════════════════════════════════════════════════════
       GLASSMORPHISM CARDS
    .glass-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: var(--shadow-xl);
        padding: 2rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInUp 0.8s ease-out;
    }
    
    .glass-card:hover {
        transform: translateY(-8px);
        box-shadow: var(--shadow-glow), var(--shadow-xl);
    }
    
    /* ═══════════════════════════════════════════════════════════════════════
       METRIC CARDS - NEUMORPHISM STYLE
    ═══════════════════════════════════════════════════════════════════════ */
    .metric-card {
        background: linear-gradient(145deg, #ffffff, #e6e6e6);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 5px 5px 15px #d1d1d1, -5px -5px 15px #ffffff;
        transition: all 0.3s ease;
        animation: scaleIn 0.6s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transition: left 0.5s ease;
    }
    
    .metric-card:hover::before {
        left: 100%;
    }
    
    .metric-card:hover {
        transform: scale(1.02);
        box-shadow: 8px 8px 20px #d1d1d1, -8px -8px 20px #ffffff;
    }
    
    .metric-icon {
        width: 50px;
        height: 50px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .metric-icon-primary { background: linear-gradient(135deg, #6366f1, #8b5cf6); }
    .metric-icon-success { background: linear-gradient(135deg, #10b981, #34d399); }
    .metric-icon-warning { background: linear-gradient(135deg, #f59e0b, #fbbf24); }
    .metric-icon-danger { background: linear-gradient(135deg, #ef4444, #f87171); }
    
    .metric-label {
        font-size: 0.8rem;
        color: var(--gray-500);
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: var(--dark);
        line-height: 1;
        animation: countUp 1s ease-out;
    }
    
    .metric-delta {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        padding: 0.3rem 0.8rem;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 0.8rem;
    }
    
    .delta-up { background: #dcfce7; color: #16a34a; }
    .delta-down { background: #fee2e2; color: #dc2626; }
    .delta-neutral { background: #fef3c7; color: #d97706; }
</style>
"""
st.markdown(COMPONENT_CSS, unsafe_allow_html=True)
    ═══════════════════════════════════════════════════════════════════════ */

# ═══════════════════════════════════════════════════════════════════════════════
# RECOMMENDATION & INTERACTIVE STYLES
# ═══════════════════════════════════════════════════════════════════════════════
RECOMMENDATION_CSS = """
<style>
    /* ═══════════════════════════════════════════════════════════════════════
       RECOMMENDATION CARDS - PREMIUM DESIGN
    ═══════════════════════════════════════════════════════════════════════ */
    .recommendation-container {
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        animation: scaleIn 0.8s ease-out;
    }
    
    .recommendation-card {
        padding: 2.5rem;
        text-align: center;
        position: relative;
        z-index: 1;
    }
    
    .recommendation-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: inherit;
        filter: blur(0);
        z-index: -1;
    }
    
    .rec-book-now {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 50%, #b91c1c 100%);
        box-shadow: 0 20px 40px rgba(239, 68, 68, 0.4);
        animation: glow 2s ease-in-out infinite;
    }
    
    .rec-wait {
        background: linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%);
        box-shadow: 0 20px 40px rgba(16, 185, 129, 0.4);
    }
    
    .rec-monitor {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 50%, #b45309 100%);
        box-shadow: 0 20px 40px rgba(245, 158, 11, 0.4);
    }
    
    .rec-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        animation: bounce 2s ease infinite;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
    }
    
    .rec-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2rem;
        font-weight: 800;
        color: white;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    
    .rec-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1rem;
        font-weight: 500;
    }
    
    .confidence-meter {
        margin-top: 1.5rem;
        padding: 1rem;
        background: rgba(255,255,255,0.15);
        border-radius: 16px;
        backdrop-filter: blur(10px);
    }
    
    .confidence-label {
        color: rgba(255,255,255,0.8);
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    .confidence-bar {
        height: 8px;
        background: rgba(255,255,255,0.2);
        border-radius: 4px;
        overflow: hidden;
    }
    
    .confidence-fill {
        height: 100%;
        background: white;
        border-radius: 4px;
        transition: width 1s ease-out;
        animation: shimmer 2s infinite;
    }
    
    .confidence-value {
        color: white;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 0.5rem;
    }
    
    /* ═══════════════════════════════════════════════════════════════════════
       AI THINKING ANIMATION
    ═══════════════════════════════════════════════════════════════════════ */
    .ai-thinking {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 3rem;
        animation: fadeIn 0.5s ease;
    }
    
    .ai-brain {
        font-size: 4rem;
        animation: float 2s ease-in-out infinite;
        margin-bottom: 1.5rem;
    }
    
    .ai-dots {
        display: flex;
        gap: 0.5rem;
    }
    
    .ai-dot {
        width: 12px;
        height: 12px;
        background: var(--primary);
        border-radius: 50%;
        animation: bounce 1.4s ease-in-out infinite;
    }
    
    .ai-dot:nth-child(1) { animation-delay: 0s; }
    .ai-dot:nth-child(2) { animation-delay: 0.2s; }
    .ai-dot:nth-child(3) { animation-delay: 0.4s; }
    
    .ai-text {
        margin-top: 1rem;
        color: var(--gray-500);
        font-size: 1rem;
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* ═══════════════════════════════════════════════════════════════════════
       SKELETON LOADING
    ═══════════════════════════════════════════════════════════════════════ */
    .skeleton {
        background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
        background-size: 1000px 100%;
        animation: shimmer 2s infinite;
        border-radius: 8px;
    }
    
    .skeleton-text { height: 20px; margin-bottom: 10px; }
    .skeleton-title { height: 40px; width: 60%; margin-bottom: 20px; }
    .skeleton-card { height: 200px; border-radius: 20px; }
</style>
"""
st.markdown(RECOMMENDATION_CSS, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR & NAVIGATION STYLES
# ═══════════════════════════════════════════════════════════════════════════════
SIDEBAR_CSS = """
<style>
    /* ═══════════════════════════════════════════════════════════════════════
       PREMIUM SIDEBAR
    ═══════════════════════════════════════════════════════════════════════ */
    [data-testid="stSidebar"] {
        background: var(--gradient-dark);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 2rem;
    }
    
    .sidebar-header {
        text-align: center;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .sidebar-logo {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        animation: float 3s ease-in-out infinite;
    }
    
    .sidebar-brand {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .sidebar-tagline {
        color: var(--gray-400);
        font-size: 0.8rem;
        margin-top: 0.3rem;
    }
    
    .sidebar-section {
        padding: 1rem 1.5rem;
        margin: 0.5rem 1rem;
        background: rgba(255,255,255,0.05);
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .sidebar-section-title {
        color: var(--gray-400);
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    [data-testid="stSidebar"] label {
        color: #e2e8f0 !important;
        font-weight: 500;
    }
    
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 12px;
        color: white;
    }
    
    [data-testid="stSidebar"] .stSlider > div > div > div {
        background: var(--primary);
    }
    
    /* ═══════════════════════════════════════════════════════════════════════
       INSIGHT CARDS
    ═══════════════════════════════════════════════════════════════════════ */
    .insight-card {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 16px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        animation: fadeInLeft 0.6s ease-out;
        transition: all 0.3s ease;
    }
    
    .insight-card:hover {
        transform: translateX(5px);
        border-color: var(--primary);
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.2);
    }
    
    .insight-icon {
        font-size: 1.5rem;
        flex-shrink: 0;
    }
    
    .insight-content {
        flex: 1;
    }
    
    .insight-title {
        font-weight: 600;
        color: var(--dark);
        font-size: 0.95rem;
        margin-bottom: 0.3rem;
    }
    
    .insight-text {
        color: var(--gray-500);
        font-size: 0.85rem;
        line-height: 1.5;
    }
    
    /* ═══════════════════════════════════════════════════════════════════════
       FEATURE CARDS
    ═══════════════════════════════════════════════════════════════════════ */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: var(--shadow-md);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid var(--gray-100);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: var(--gradient-primary);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover::after {
        transform: scaleX(1);
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: var(--shadow-xl);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .feature-title {
        font-weight: 700;
        color: var(--dark);
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: var(--gray-500);
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    /* ═══════════════════════════════════════════════════════════════════════
       TABS STYLING
    ═══════════════════════════════════════════════════════════════════════ */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background: var(--gray-100);
        border-radius: 16px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 12px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        color: var(--gray-500);
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: white;
        color: var(--primary);
        box-shadow: var(--shadow-md);
    }
    
    /* ═══════════════════════════════════════════════════════════════════════
       FOOTER
    ═══════════════════════════════════════════════════════════════════════ */
    .footer {
        text-align: center;
        padding: 3rem 2rem;
        margin-top: 4rem;
        background: var(--gradient-dark);
        border-radius: 24px 24px 0 0;
        animation: slideInFromBottom 1s ease-out;
    }
    
    .footer-brand {
        font-family: 'Poppins', sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .footer-tagline {
        color: var(--gray-400);
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    
    .footer-tech {
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
        margin-bottom: 2rem;
    }
    
    .footer-tech-item {
        color: var(--gray-400);
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .footer-credits {
        color: var(--gray-500);
        font-size: 0.85rem;
        padding-top: 2rem;
        border-top: 1px solid rgba(255,255,255,0.1);
    }
</style>
"""
st.markdown(SIDEBAR_CSS, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PERFORMANCE OPTIMIZED DATA LOADING
# ═══════════════════════════════════════════════════════════════════════════════
@st.cache_data(ttl=3600, show_spinner=False)
def load_data():
    """Load and cache historical data for optimal performance"""
    try:
        hotel_data = pd.read_csv('data/hotel_prices.csv')
        flight_data = pd.read_csv('data/flight_prices.csv')
        hotel_data['date'] = pd.to_datetime(hotel_data['date'])
        flight_data['date'] = pd.to_datetime(flight_data['date'])
        return hotel_data, flight_data
    except FileNotFoundError:
        return None, None

@st.cache_resource(show_spinner=False)
def load_models():
    """Load and cache ML models"""
    try:
        hotel_model = PriceForecastingModel('hotel')
        hotel_model.load_model('models/hotel_model.pkl')
        flight_model = PriceForecastingModel('flight')
        flight_model.load_model('models/flight_model.pkl')
        return hotel_model, flight_model
    except FileNotFoundError:
        return None, None

# ═══════════════════════════════════════════════════════════════════════════════
# PREMIUM CHART FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════
def create_premium_forecast_chart(dates, prices, current_price, title):
    """Create MNC-grade animated forecast chart"""
    
    fig = go.Figure()
    
    # Gradient area fill
    fig.add_trace(go.Scatter(
        x=dates, y=prices,
        fill='tozeroy',
        fillcolor='rgba(99, 102, 241, 0.1)',
        line=dict(width=0),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Main forecast line
    fig.add_trace(go.Scatter(
        x=dates, y=prices,
        mode='lines+markers',
        name='Predicted Price',
        line=dict(
            color='#6366f1',
            width=4,
            shape='spline',
            smoothing=1.3
        ),
        marker=dict(
            size=12,
            color='#6366f1',
            line=dict(width=3, color='white'),
            symbol='circle'
        ),
        hovertemplate='<b>%{x|%b %d, %Y}</b><br>💰 $%{y:.2f}<extra></extra>'
    ))
    
    # Current price reference
    if current_price:
        fig.add_hline(
            y=current_price,
            line_dash="dash",
            line_color="#ef4444",
            line_width=2,
            annotation_text=f"Current: ${current_price:.2f}",
            annotation_position="right",
            annotation_font=dict(size=12, color="#ef4444", family="Inter")
        )
    
    # Min/Max markers
    min_idx = prices.index(min(prices)) if isinstance(prices, list) else np.argmin(prices)
    max_idx = prices.index(max(prices)) if isinstance(prices, list) else np.argmax(prices)
    
    fig.add_annotation(
        x=dates[min_idx], y=min(prices),
        text=f"Lowest<br>${min(prices):.0f}",
        showarrow=True, arrowhead=2, arrowcolor="#10b981",
        font=dict(color="#10b981", size=11),
        bgcolor="white", bordercolor="#10b981", borderwidth=1
    )
    
    fig.add_annotation(
        x=dates[max_idx], y=max(prices),
        text=f"Highest<br>${max(prices):.0f}",
        showarrow=True, arrowhead=2, arrowcolor="#ef4444",
        font=dict(color="#ef4444", size=11),
        bgcolor="white", bordercolor="#ef4444", borderwidth=1
    )
    
    fig.update_layout(
        title=dict(
            text=f"<b>{title}</b>",
            font=dict(size=20, color='#0f172a', family='Poppins'),
            x=0.5
        ),
        xaxis=dict(
            title="Date",
            showgrid=True,
            gridcolor='rgba(0,0,0,0.05)',
            tickfont=dict(size=11, family='Inter'),
            title_font=dict(size=13, family='Inter')
        ),
        yaxis=dict(
            title="Price (USD)",
            showgrid=True,
            gridcolor='rgba(0,0,0,0.05)',
            tickfont=dict(size=11, family='Inter'),
            title_font=dict(size=13, family='Inter'),
            tickprefix="$"
        ),
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=450,
        margin=dict(l=60, r=40, t=80, b=60),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=12)
        )
    )
    
    # Add animation
    fig.update_traces(
        selector=dict(mode='lines+markers'),
    )
    
    return fig

def create_historical_chart(data, title):
    """Create premium historical price chart"""
    
    fig = go.Figure()
    
    # Area fill with gradient effect
    fig.add_trace(go.Scatter(
        x=data['date'], y=data['price'],
        fill='tozeroy',
        fillcolor='rgba(139, 92, 246, 0.15)',
        line=dict(color='#8b5cf6', width=3, shape='spline'),
        name='Historical Price',
        hovertemplate='<b>%{x|%b %d, %Y}</b><br>💰 $%{y:.2f}<extra></extra>'
    ))
    
    # Moving average
    ma_7 = data['price'].rolling(window=7).mean()
    fig.add_trace(go.Scatter(
        x=data['date'], y=ma_7,
        mode='lines',
        name='7-Day Average',
        line=dict(color='#06b6d4', width=2, dash='dot'),
        hovertemplate='<b>%{x|%b %d}</b><br>📊 Avg: $%{y:.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(text=f"<b>{title}</b>", font=dict(size=18, family='Poppins'), x=0.5),
        xaxis=dict(title="Date", showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
        yaxis=dict(title="Price (USD)", showgrid=True, gridcolor='rgba(0,0,0,0.05)', tickprefix="$"),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400,
        margin=dict(l=60, r=30, t=60, b=50),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def create_day_analysis_chart(data):
    """Create day-of-week price analysis chart"""
    
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_avg = data.groupby('day_of_week')['price'].mean().reindex(day_order)
    
    colors = ['#6366f1' if i < 5 else '#8b5cf6' for i in range(7)]
    
    fig = go.Figure(data=[
        go.Bar(
            x=day_avg.index,
            y=day_avg.values,
            marker=dict(
                color=colors,
                line=dict(width=0),
                cornerradius=8
            ),
            text=[f'${v:.0f}' for v in day_avg.values],
            textposition='outside',
            textfont=dict(size=12, family='Inter', color='#64748b'),
            hovertemplate='<b>%{x}</b><br>Average: $%{y:.2f}<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title=dict(text="<b>Price by Day of Week</b>", font=dict(size=16, family='Poppins'), x=0.5),
        xaxis=dict(title="", tickfont=dict(size=11)),
        yaxis=dict(title="Average Price", tickprefix="$", showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=350,
        margin=dict(l=60, r=30, t=60, b=50),
        bargap=0.3
    )
    
    return fig

def create_season_chart(data):
    """Create seasonal price analysis chart"""
    
    season_avg = data.groupby('season')['price'].agg(['mean', 'min', 'max']).reset_index()
    season_order = ['Spring', 'Summer', 'Fall', 'Winter']
    season_avg['season'] = pd.Categorical(season_avg['season'], categories=season_order, ordered=True)
    season_avg = season_avg.sort_values('season')
    
    colors = {'Spring': '#10b981', 'Summer': '#f59e0b', 'Fall': '#8b5cf6', 'Winter': '#06b6d4'}
    
    fig = go.Figure()
    
    for _, row in season_avg.iterrows():
        fig.add_trace(go.Bar(
            x=[row['season']],
            y=[row['mean']],
            name=row['season'],
            marker_color=colors[row['season']],
            text=f"${row['mean']:.0f}",
            textposition='outside',
            hovertemplate=f"<b>{row['season']}</b><br>Avg: ${row['mean']:.0f}<br>Min: ${row['min']:.0f}<br>Max: ${row['max']:.0f}<extra></extra>"
        ))
    
    fig.update_layout(
        title=dict(text="<b>Seasonal Price Trends</b>", font=dict(size=16, family='Poppins'), x=0.5),
        xaxis=dict(title=""),
        yaxis=dict(title="Average Price", tickprefix="$", showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=350,
        showlegend=False,
        bargap=0.4
    )
    
    return fig

# ═══════════════════════════════════════════════════════════════════════════════
# HTML COMPONENT GENERATORS
# ═══════════════════════════════════════════════════════════════════════════════
def render_hero():
    """Render premium hero section"""
    return """
    <div class="hero-container">
        <div class="hero-badge">🚀 AI-Powered Price Intelligence</div>
        <h1 class="hero-title">PriceWise AI</h1>
        <p class="hero-subtitle">Enterprise-grade price forecasting for smarter travel decisions</p>
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="hero-stat-value">76.6%</div>
                <div class="hero-stat-label">Accuracy</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-value">2,192</div>
                <div class="hero-stat-label">Data Points</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-value">&lt;1s</div>
                <div class="hero-stat-label">Response</div>
            </div>
        </div>
    </div>
    """

def render_metric_card(icon, label, value, delta=None, delta_type="neutral", icon_class="primary"):
    """Render premium metric card"""
    delta_html = ""
    if delta:
        delta_class = f"delta-{'up' if delta_type == 'up' else 'down' if delta_type == 'down' else 'neutral'}"
        arrow = "↑" if delta_type == "up" else "↓" if delta_type == "down" else "→"
        delta_html = f'<div class="metric-delta {delta_class}">{arrow} {delta}</div>'
    
    return f"""
    <div class="metric-card">
        <div class="metric-icon metric-icon-{icon_class}">{icon}</div>
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """

def render_recommendation(rec_type, confidence, reason):
    """Render premium recommendation card"""
    configs = {
        "book": {"class": "rec-book-now", "icon": "🔥", "title": "BOOK NOW", "subtitle": "Prices are rising!"},
        "wait": {"class": "rec-wait", "icon": "⏳", "title": "WAIT", "subtitle": "Prices will drop!"},
        "monitor": {"class": "rec-monitor", "icon": "👀", "title": "MONITOR", "subtitle": "Prices are stable"}
    }
    
    config = configs.get(rec_type, configs["monitor"])
    conf_percent = {"High": 85, "Medium": 65, "Low": 45}.get(confidence, 65)
    
    return f"""
    <div class="recommendation-container">
        <div class="recommendation-card {config['class']}">
            <div class="rec-icon">{config['icon']}</div>
            <div class="rec-title">{config['title']}</div>
            <div class="rec-subtitle">{config['subtitle']}</div>
            <div class="confidence-meter">
                <div class="confidence-label">AI Confidence Level</div>
                <div class="confidence-bar">
                    <div class="confidence-fill" style="width: {conf_percent}%;"></div>
                </div>
                <div class="confidence-value">{confidence} ({conf_percent}%)</div>
            </div>
        </div>
    </div>
    """

def render_ai_thinking():
    """Render AI thinking animation"""
    return """
    <div class="ai-thinking">
        <div class="ai-brain">🧠</div>
        <div class="ai-dots">
            <div class="ai-dot"></div>
            <div class="ai-dot"></div>
            <div class="ai-dot"></div>
        </div>
        <div class="ai-text">Analyzing price trends...</div>
    </div>
    """

def render_insight_card(icon, title, text):
    """Render insight card"""
    return f"""
    <div class="insight-card">
        <div class="insight-icon">{icon}</div>
        <div class="insight-content">
            <div class="insight-title">{title}</div>
            <div class="insight-text">{text}</div>
        </div>
    </div>
    """

def render_feature_card(icon, title, desc):
    """Render feature card"""
    return f"""
    <div class="feature-card">
        <span class="feature-icon">{icon}</span>
        <div class="feature-title">{title}</div>
        <div class="feature-desc">{desc}</div>
    </div>
    """

def render_why_prediction(factors):
    """Render AI explainability section"""
    html = """
    <div class="glass-card" style="margin-top: 1.5rem;">
        <h4 style="margin: 0 0 1rem 0; color: #0f172a; font-family: 'Poppins', sans-serif;">
            🤖 Why This Prediction?
        </h4>
        <p style="color: #64748b; font-size: 0.9rem; margin-bottom: 1rem;">
            Our AI analyzed multiple factors to generate this recommendation:
        </p>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
    """
    
    for factor in factors:
        impact_color = "#10b981" if factor['impact'] == 'positive' else "#ef4444" if factor['impact'] == 'negative' else "#f59e0b"
        html += f"""
        <div style="display: flex; align-items: center; gap: 0.8rem; padding: 0.8rem; background: #f8fafc; border-radius: 12px;">
            <span style="font-size: 1.5rem;">{factor['icon']}</span>
            <div>
                <div style="font-weight: 600; color: #0f172a; font-size: 0.9rem;">{factor['name']}</div>
                <div style="color: {impact_color}; font-size: 0.8rem; font-weight: 500;">{factor['value']}</div>
            </div>
        </div>
        """
    
    html += "</div></div>"
    return html

def render_footer():
    """Render premium footer"""
    return """
    <div class="footer">
        <div class="footer-brand">🌐 PriceWise AI</div>
        <div class="footer-tagline">Enterprise-grade price intelligence for smarter travel</div>
        <div class="footer-tech">
            <span class="footer-tech-item">🐍 Python</span>
            <span class="footer-tech-item">🤖 Scikit-learn</span>
            <span class="footer-tech-item">📊 Plotly</span>
            <span class="footer-tech-item">🎨 Streamlit</span>
            <span class="footer-tech-item">📈 Pandas</span>
        </div>
        <div class="footer-credits">
            🏆 Built for Puduvai Youth Fest 2026 AI Hackathon<br>
            <span style="font-size: 0.75rem; color: #94a3b8;">Empowering travelers with AI-driven insights</span>
        </div>
    </div>
    """

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════
def render_sidebar():
    """Render premium sidebar"""
    with st.sidebar:
        # Brand header
        st.markdown("""
        <div class="sidebar-header">
            <div class="sidebar-logo">🌐</div>
            <div class="sidebar-brand">PriceWise AI</div>
            <div class="sidebar-tagline">Smart Travel Forecasting</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Service Selection
        st.markdown('<div class="sidebar-section-title">🎯 SERVICE TYPE</div>', unsafe_allow_html=True)
        service_type = st.selectbox(
            "Select Service",
            ["🏨 Hotel", "✈️ Flight"],
            label_visibility="collapsed"
        )
        
        st.markdown("")
        
        # Date Selection
        st.markdown('<div class="sidebar-section-title">📅 TRAVEL DATE</div>', unsafe_allow_html=True)
        min_date = datetime.now().date()
        max_date = min_date + timedelta(days=365)
        selected_date = st.date_input(
            "Select Date",
            value=min_date + timedelta(days=7),
            min_value=min_date,
            max_value=max_date,
            label_visibility="collapsed"
        )
        
        st.markdown("")
        
        # Forecast Period
        st.markdown('<div class="sidebar-section-title">🔮 FORECAST PERIOD</div>', unsafe_allow_html=True)
        prediction_days = st.slider(
            "Days ahead",
            min_value=3,
            max_value=30,
            value=7,
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Model Stats
        st.markdown("""
        <div style="padding: 1rem; background: rgba(99, 102, 241, 0.1); border-radius: 12px; margin: 1rem 0;">
            <div style="color: #a5b4fc; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">
                📊 Model Performance
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="color: #94a3b8; font-size: 0.85rem;">Accuracy</span>
                <span style="color: #10b981; font-weight: 600;">76.6%</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="color: #94a3b8; font-size: 0.85rem;">Avg Error</span>
                <span style="color: #06b6d4; font-weight: 600;">$12.68</span>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <span style="color: #94a3b8; font-size: 0.85rem;">Data Points</span>
                <span style="color: #8b5cf6; font-weight: 600;">2,192</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        return service_type, selected_date, prediction_days

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN APPLICATION
# ═══════════════════════════════════════════════════════════════════════════════
def main():
    """Main application entry point"""
    
    # Load data and models
    hotel_data, flight_data = load_data()
    hotel_model, flight_model = load_models()
    
    if hotel_data is None or hotel_model is None:
        st.error("⚠️ System initialization failed. Please run setup first.")
        st.code("python data_generator.py\npython model.py", language="bash")
        st.stop()
    
    # Render sidebar and get selections
    service_type, selected_date, prediction_days = render_sidebar()
    
    # Hero Section
    st.markdown(render_hero(), unsafe_allow_html=True)
    
    # Select appropriate data and model
    if "Hotel" in service_type:
        data = hotel_data
        model = hotel_model
        service_name = "Hotel"
        service_icon = "🏨"
    else:
        data = flight_data
        model = flight_model
        service_name = "Flight"
        service_icon = "✈️"
    
    # Create prediction data
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
        
        # Determine recommendation type
        if recommendation_data['price_change_percent'] > 5:
            rec_type = "book"
        elif recommendation_data['price_change_percent'] < -5:
            rec_type = "wait"
        else:
            rec_type = "monitor"
        
        # ═══════════════════════════════════════════════════════════════════
        # MAIN CONTENT TABS
        # ═══════════════════════════════════════════════════════════════════
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Forecast",
            "📈 Analytics", 
            "🤖 AI Insights",
            "💡 Tips"
        ])
        
        # ═══════════════════════════════════════════════════════════════════
        # TAB 1: FORECAST
        # ═══════════════════════════════════════════════════════════════════
        with tab1:
            # Metrics Row
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                delta_type = "up" if recommendation_data['price_change_percent'] > 0 else "down"
                st.markdown(render_metric_card(
                    "💰", "Current Price", f"${current_price:.2f}",
                    f"{abs(recommendation_data['price_change_percent']):.1f}%",
                    delta_type, "primary"
                ), unsafe_allow_html=True)
            
            with col2:
                st.markdown(render_metric_card(
                    "📊", "Predicted Avg", f"${recommendation_data['predicted_avg_price']:.2f}",
                    icon_class="secondary"
                ), unsafe_allow_html=True)
            
            with col3:
                st.markdown(render_metric_card(
                    "📉", "Lowest Expected", f"${min(future_prices):.2f}",
                    icon_class="success"
                ), unsafe_allow_html=True)
            
            with col4:
                st.markdown(render_metric_card(
                    "📈", "Highest Expected", f"${max(future_prices):.2f}",
                    icon_class="danger"
                ), unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Main content
            chart_col, rec_col = st.columns([2, 1])
            
            with chart_col:
                all_dates = [current_date] + future_dates
                all_prices = [current_price] + list(future_prices)
                
                forecast_chart = create_premium_forecast_chart(
                    all_dates, all_prices, current_price,
                    f"{service_icon} {service_name} Price Forecast ({prediction_days} Days)"
                )
                st.plotly_chart(forecast_chart, use_container_width=True)
            
            with rec_col:
                st.markdown(render_recommendation(
                    rec_type,
                    recommendation_data['confidence'],
                    recommendation_data['reason']
                ), unsafe_allow_html=True)
                
                # Savings indicator
                if rec_type == "wait":
                    savings = current_price - recommendation_data['predicted_avg_price']
                    st.success(f"💰 Potential Savings: **${savings:.2f}**")
                elif rec_type == "book":
                    extra = recommendation_data['predicted_avg_price'] - current_price
                    st.warning(f"⚠️ Book now to save: **${extra:.2f}**")

        # ═══════════════════════════════════════════════════════════════════
        # TAB 2: ANALYTICS
        # ═══════════════════════════════════════════════════════════════════
        with tab2:
            st.markdown("### 📈 Historical Price Analysis")
            
            # Historical chart
            recent_data = data.tail(90).copy()
            hist_chart = create_historical_chart(recent_data, f"{service_name} Prices (Last 90 Days)")
            st.plotly_chart(hist_chart, use_container_width=True)
            
            # Analysis charts
            col1, col2 = st.columns(2)
            
            with col1:
                day_chart = create_day_analysis_chart(data)
                st.plotly_chart(day_chart, use_container_width=True)
            
            with col2:
                season_chart = create_season_chart(data)
                st.plotly_chart(season_chart, use_container_width=True)
            
            # Statistics
            st.markdown("### 📊 Price Statistics")
            
            stats_cols = st.columns(4)
            price_stats = data['price'].describe()
            
            stats_data = [
                ("📊", "Average", f"${price_stats['mean']:.2f}", "primary"),
                ("📉", "Minimum", f"${price_stats['min']:.2f}", "success"),
                ("📈", "Maximum", f"${price_stats['max']:.2f}", "danger"),
                ("📐", "Std Dev", f"${price_stats['std']:.2f}", "warning")
            ]
            
            for col, (icon, label, value, icon_class) in zip(stats_cols, stats_data):
                with col:
                    st.markdown(render_metric_card(icon, label, value, icon_class=icon_class), unsafe_allow_html=True)
        
        # ═══════════════════════════════════════════════════════════════════
        # TAB 3: AI INSIGHTS
        # ═══════════════════════════════════════════════════════════════════
        with tab3:
            st.markdown("### 🤖 AI-Powered Insights")
            
            # Why this prediction
            weekend_avg = data[data['is_weekend'] == 1]['price'].mean()
            weekday_avg = data[data['is_weekend'] == 0]['price'].mean()
            weekend_diff = ((weekend_avg - weekday_avg) / weekday_avg) * 100
            
            factors = [
                {"icon": "📅", "name": "Day Type", "value": f"{'Weekend' if current_date.weekday() >= 5 else 'Weekday'} pricing", "impact": "neutral"},
                {"icon": "🌡️", "name": "Season", "value": f"{model._get_season(current_date.month)} demand", "impact": "positive" if current_date.month in [6,7,8,12] else "neutral"},
                {"icon": "📈", "name": "Trend", "value": f"{recommendation_data['price_change_percent']:.1f}% expected change", "impact": "negative" if recommendation_data['price_change_percent'] > 0 else "positive"},
                {"icon": "⏰", "name": "Timing", "value": f"{prediction_days} days forecast window", "impact": "neutral"}
            ]
            
            st.markdown(render_why_prediction(factors), unsafe_allow_html=True)
            
            # Dynamic insights
            st.markdown("### 💡 Smart Insights")
            
            insights = []
            
            if weekend_diff > 10:
                insights.append(("💰", "Weekend Premium", f"Weekends are {weekend_diff:.0f}% more expensive. Consider weekday travel for savings!"))
            
            season_avg = data.groupby('season')['price'].mean()
            cheapest_season = season_avg.idxmin()
            insights.append(("🌸", "Best Season", f"{cheapest_season} offers the lowest average prices at ${season_avg[cheapest_season]:.0f}"))
            
            avg_price = data['price'].mean()
            if current_price < avg_price * 0.9:
                insights.append(("🎯", "Great Deal!", f"Current price is {((avg_price - current_price)/avg_price)*100:.0f}% below average - excellent value!"))
            elif current_price > avg_price * 1.1:
                insights.append(("⚠️", "Above Average", f"Current price is {((current_price - avg_price)/avg_price)*100:.0f}% above average"))
            
            if recommendation_data['price_change_percent'] > 5:
                insights.append(("📈", "Rising Trend", "Prices are trending upward - booking soon is recommended"))
            elif recommendation_data['price_change_percent'] < -5:
                insights.append(("📉", "Falling Trend", "Prices are trending downward - waiting could save you money"))
            
            for icon, title, text in insights:
                st.markdown(render_insight_card(icon, title, text), unsafe_allow_html=True)

        # ═══════════════════════════════════════════════════════════════════
        # TAB 4: TIPS
        # ═══════════════════════════════════════════════════════════════════
        with tab4:
            st.markdown("### 🎓 Smart Booking Tips")
            
            tips_col1, tips_col2, tips_col3 = st.columns(3)
            
            with tips_col1:
                st.markdown(render_feature_card(
                    "📅",
                    "Best Booking Time",
                    "Book hotels 2-3 weeks ahead, flights 6-8 weeks for optimal prices"
                ), unsafe_allow_html=True)
            
            with tips_col2:
                st.markdown(render_feature_card(
                    "🔄",
                    "Be Flexible",
                    "Flexible dates can save up to 30% on your bookings"
                ), unsafe_allow_html=True)
            
            with tips_col3:
                st.markdown(render_feature_card(
                    "🔔",
                    "Set Alerts",
                    "Use price alerts to catch sudden drops automatically"
                ), unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            tips_col4, tips_col5, tips_col6 = st.columns(3)
            
            with tips_col4:
                st.markdown(render_feature_card(
                    "📊",
                    "Compare Options",
                    "Always compare multiple dates and providers"
                ), unsafe_allow_html=True)
            
            with tips_col5:
                st.markdown(render_feature_card(
                    "🌙",
                    "Off-Peak Travel",
                    "Midweek flights and stays are typically cheaper"
                ), unsafe_allow_html=True)
            
            with tips_col6:
                st.markdown(render_feature_card(
                    "🎯",
                    "Book Direct",
                    "Sometimes booking direct offers better cancellation policies"
                ), unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # How it works
            st.markdown("### 🤖 How Our AI Works")
            
            how_cols = st.columns(4)
            
            steps = [
                ("1️⃣", "Data Collection", "Analyze 2+ years of historical price patterns"),
                ("2️⃣", "Feature Analysis", "Extract seasonal, weekly, and demand trends"),
                ("3️⃣", "ML Prediction", "Apply Linear Regression forecasting model"),
                ("4️⃣", "Smart Advice", "Generate actionable booking recommendations")
            ]
            
            for col, (num, title, desc) in zip(how_cols, steps):
                with col:
                    st.markdown(render_feature_card(num, title, desc), unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Social Impact
            st.markdown("### 🌍 Social Impact")
            
            impact_col1, impact_col2 = st.columns(2)
            
            with impact_col1:
                st.markdown("""
                <div class="glass-card">
                    <h4 style="color: #0f172a; margin-bottom: 1rem;">💚 How We Help</h4>
                    <ul style="color: #64748b; line-height: 2;">
                        <li><strong>Cost-Efficient Travel:</strong> Save 10-20% on bookings</li>
                        <li><strong>Democratized AI:</strong> Enterprise tools for everyone</li>
                        <li><strong>Smart Decisions:</strong> Data-driven travel planning</li>
                        <li><strong>Sustainable Tourism:</strong> Optimized travel reduces waste</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with impact_col2:
                st.markdown("""
                <div class="glass-card">
                    <h4 style="color: #0f172a; margin-bottom: 1rem;">🎯 Our Mission</h4>
                    <p style="color: #64748b; line-height: 1.8;">
                        We believe everyone deserves access to intelligent travel planning tools. 
                        Our AI-powered platform democratizes price intelligence, helping travelers 
                        make informed decisions and save money on their journeys.
                    </p>
                    <p style="color: #6366f1; font-weight: 600; margin-top: 1rem;">
                        #impact4globalgoals 🌐
                    </p>
                </div>
                """, unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"⚠️ Prediction error: {str(e)}")
        st.info("Please ensure all data and models are properly loaded.")
    
    # Footer
    st.markdown(render_footer(), unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# APPLICATION ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    main()