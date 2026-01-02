"""
AI-Driven Price Forecasting System - Data Generator
Creates realistic sample datasets for hotel and flight prices
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_hotel_data():
    """Generate realistic hotel price data with seasonal patterns"""
    
    # Set random seed for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # Generate dates for 2 years of data
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    hotel_data = []
    
    for date in dates:
        # Base price with seasonal variation
        base_price = 100
        
        # Seasonal factors
        month = date.month
        if month in [12, 1, 2]:  # Winter peak
            seasonal_factor = 1.4
        elif month in [6, 7, 8]:  # Summer peak
            seasonal_factor = 1.6
        elif month in [3, 4, 5, 9, 10, 11]:  # Shoulder season
            seasonal_factor = 1.2
        
        # Weekend premium
        weekend_factor = 1.3 if date.weekday() >= 5 else 1.0
        
        # Holiday premium (simplified)
        holiday_factor = 1.5 if date.day == 25 and date.month == 12 else 1.0
        
        # Random demand factor
        demand_factor = np.random.uniform(0.8, 1.2)
        
        # Calculate final price
        price = base_price * seasonal_factor * weekend_factor * holiday_factor * demand_factor
        
        # Add some noise
        price += np.random.normal(0, 10)
        price = max(50, round(price, 2))  # Minimum price of $50
        
        hotel_data.append({
            'date': date,
            'price': price,
            'day_of_week': date.strftime('%A'),
            'month': date.month,
            'is_weekend': 1 if date.weekday() >= 5 else 0,
            'season': get_season(date.month),
            'demand_score': round(demand_factor * 100, 1)
        })
    
    return pd.DataFrame(hotel_data)

def generate_flight_data():
    """Generate realistic flight price data with booking patterns"""
    
    np.random.seed(42)
    random.seed(42)
    
    # Generate dates for 2 years
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    flight_data = []
    
    for date in dates:
        # Base price
        base_price = 300
        
        # Seasonal factors
        month = date.month
        if month in [12, 1, 7, 8]:  # Peak travel months
            seasonal_factor = 1.5
        elif month in [2, 3, 9, 10, 11]:  # Shoulder season
            seasonal_factor = 1.2
        else:  # Off-peak
            seasonal_factor = 0.9
        
        # Day of week factor (Tuesday/Wednesday cheaper)
        day_of_week = date.weekday()
        if day_of_week in [1, 2]:  # Tuesday, Wednesday
            day_factor = 0.85
        elif day_of_week in [4, 6]:  # Friday, Sunday
            day_factor = 1.3
        else:
            day_factor = 1.0
        
        # Advance booking factor (simplified)
        advance_factor = np.random.uniform(0.7, 1.4)
        
        # Random market factor
        market_factor = np.random.uniform(0.9, 1.1)
        
        # Calculate final price
        price = base_price * seasonal_factor * day_factor * advance_factor * market_factor
        
        # Add noise
        price += np.random.normal(0, 20)
        price = max(150, round(price, 2))  # Minimum price of $150
        
        flight_data.append({
            'date': date,
            'price': price,
            'day_of_week': date.strftime('%A'),
            'month': date.month,
            'is_weekend': 1 if date.weekday() >= 5 else 0,
            'season': get_season(date.month),
            'advance_booking_days': random.randint(1, 90),
            'demand_score': round(market_factor * 100, 1)
        })
    
    return pd.DataFrame(flight_data)

def get_season(month):
    """Convert month to season"""
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

def main():
    """Generate and save datasets"""
    print("🔄 Generating sample datasets...")
    
    # Create data directory
    import os
    os.makedirs('data', exist_ok=True)
    
    # Generate hotel data
    print("📊 Creating hotel price dataset...")
    hotel_df = generate_hotel_data()
    hotel_df.to_csv('data/hotel_prices.csv', index=False)
    print(f"✅ Hotel dataset created: {len(hotel_df)} records")
    
    # Generate flight data
    print("✈️ Creating flight price dataset...")
    flight_df = generate_flight_data()
    flight_df.to_csv('data/flight_prices.csv', index=False)
    print(f"✅ Flight dataset created: {len(flight_df)} records")
    
    # Display sample data
    print("\n📋 Sample Hotel Data:")
    print(hotel_df.head())
    print(f"\nHotel Price Range: ${hotel_df['price'].min():.2f} - ${hotel_df['price'].max():.2f}")
    
    print("\n📋 Sample Flight Data:")
    print(flight_df.head())
    print(f"\nFlight Price Range: ${flight_df['price'].min():.2f} - ${flight_df['price'].max():.2f}")
    
    print("\n🎉 Data generation completed successfully!")

if __name__ == "__main__":
    main()