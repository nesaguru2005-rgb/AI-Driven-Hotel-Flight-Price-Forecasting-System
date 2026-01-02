"""
AI-Driven Price Forecasting System - ML Model
Implements Linear Regression and Time Series forecasting for price prediction
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

class PriceForecastingModel:
    """ML Model for predicting hotel and flight prices"""
    
    def __init__(self, model_type='hotel'):
        self.model_type = model_type
        self.model = LinearRegression()
        self.label_encoders = {}
        self.feature_columns = []
        self.is_trained = False
        
    def prepare_features(self, df):
        """Prepare features for machine learning"""
        
        # Create a copy to avoid modifying original data
        data = df.copy()
        
        # Convert date to datetime if it's not already
        if 'date' in data.columns:
            data['date'] = pd.to_datetime(data['date'])
            
            # Extract date features
            data['year'] = data['date'].dt.year
            data['month'] = data['date'].dt.month
            data['day'] = data['date'].dt.day
            data['day_of_year'] = data['date'].dt.dayofyear
            data['week_of_year'] = data['date'].dt.isocalendar().week
        
        # Encode categorical variables
        categorical_columns = ['day_of_week', 'season']
        
        for col in categorical_columns:
            if col in data.columns:
                if col not in self.label_encoders:
                    self.label_encoders[col] = LabelEncoder()
                    data[f'{col}_encoded'] = self.label_encoders[col].fit_transform(data[col])
                else:
                    # Handle unseen categories during prediction
                    try:
                        data[f'{col}_encoded'] = self.label_encoders[col].transform(data[col])
                    except ValueError:
                        # If unseen category, use most frequent category
                        most_frequent = self.label_encoders[col].classes_[0]
                        data[col] = data[col].fillna(most_frequent)
                        data[f'{col}_encoded'] = self.label_encoders[col].transform(data[col])
        
        # Select features for training
        feature_columns = [
            'month', 'day', 'day_of_year', 'week_of_year',
            'is_weekend', 'demand_score', 'day_of_week_encoded', 'season_encoded'
        ]
        
        # Add model-specific features
        if self.model_type == 'flight' and 'advance_booking_days' in data.columns:
            feature_columns.append('advance_booking_days')
        
        # Filter only existing columns
        feature_columns = [col for col in feature_columns if col in data.columns]
        self.feature_columns = feature_columns
        
        return data[feature_columns]
    
    def train(self, df):
        """Train the price forecasting model"""
        
        print(f"🤖 Training {self.model_type} price forecasting model...")
        
        # Prepare features
        X = self.prepare_features(df)
        y = df['price']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, shuffle=True
        )
        
        # Train model
        self.model.fit(X_train, y_train)
        
        # Make predictions
        y_pred_train = self.model.predict(X_train)
        y_pred_test = self.model.predict(X_test)
        
        # Calculate metrics
        train_mae = mean_absolute_error(y_train, y_pred_train)
        test_mae = mean_absolute_error(y_test, y_pred_test)
        train_r2 = r2_score(y_train, y_pred_train)
        test_r2 = r2_score(y_test, y_pred_test)
        
        print(f"📊 Model Performance:")
        print(f"   Training MAE: ${train_mae:.2f}")
        print(f"   Testing MAE: ${test_mae:.2f}")
        print(f"   Training R²: {train_r2:.3f}")
        print(f"   Testing R²: {test_r2:.3f}")
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'feature': self.feature_columns,
            'importance': abs(self.model.coef_)
        }).sort_values('importance', ascending=False)
        
        print(f"\n🔍 Top Features:")
        for _, row in feature_importance.head(5).iterrows():
            print(f"   {row['feature']}: {row['importance']:.2f}")
        
        self.is_trained = True
        return {
            'train_mae': train_mae,
            'test_mae': test_mae,
            'train_r2': train_r2,
            'test_r2': test_r2,
            'feature_importance': feature_importance
        }
    
    def predict(self, df):
        """Make price predictions"""
        
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        
        X = self.prepare_features(df)
        predictions = self.model.predict(X)
        
        return predictions
    
    def predict_future_trend(self, current_date, days_ahead=7):
        """Predict price trend for future dates"""
        
        future_dates = []
        for i in range(1, days_ahead + 1):
            future_date = current_date + timedelta(days=i)
            future_dates.append(future_date)
        
        # Create future data with estimated features
        future_data = []
        for date in future_dates:
            # Estimate demand score (simplified)
            base_demand = 100
            weekend_boost = 10 if date.weekday() >= 5 else 0
            seasonal_boost = 15 if date.month in [6, 7, 8, 12] else 0
            demand_score = base_demand + weekend_boost + seasonal_boost + np.random.uniform(-5, 5)
            
            future_data.append({
                'date': date,
                'day_of_week': date.strftime('%A'),
                'month': date.month,
                'is_weekend': 1 if date.weekday() >= 5 else 0,
                'season': self._get_season(date.month),
                'demand_score': demand_score,
                'advance_booking_days': 30 if self.model_type == 'flight' else None
            })
        
        future_df = pd.DataFrame(future_data)
        predictions = self.predict(future_df)
        
        return future_dates, predictions
    
    def get_recommendation(self, current_price, future_prices):
        """Generate booking recommendation based on price trend"""
        
        avg_future_price = np.mean(future_prices)
        price_change_percent = ((avg_future_price - current_price) / current_price) * 100
        
        if price_change_percent > 5:
            recommendation = "📈 BOOK NOW"
            reason = f"Prices expected to increase by {price_change_percent:.1f}%"
            confidence = "High" if price_change_percent > 10 else "Medium"
        elif price_change_percent < -5:
            recommendation = "⏳ WAIT"
            reason = f"Prices expected to decrease by {abs(price_change_percent):.1f}%"
            confidence = "High" if price_change_percent < -10 else "Medium"
        else:
            recommendation = "🤔 NEUTRAL"
            reason = f"Prices expected to remain stable ({price_change_percent:.1f}% change)"
            confidence = "Medium"
        
        return {
            'recommendation': recommendation,
            'reason': reason,
            'confidence': confidence,
            'price_change_percent': price_change_percent,
            'current_price': current_price,
            'predicted_avg_price': avg_future_price
        }
    
    def _get_season(self, month):
        """Convert month to season"""
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Fall'
    
    def save_model(self, filepath):
        """Save trained model to file"""
        model_data = {
            'model': self.model,
            'label_encoders': self.label_encoders,
            'feature_columns': self.feature_columns,
            'model_type': self.model_type,
            'is_trained': self.is_trained
        }
        joblib.dump(model_data, filepath)
        print(f"💾 Model saved to {filepath}")
    
    def load_model(self, filepath):
        """Load trained model from file"""
        model_data = joblib.load(filepath)
        self.model = model_data['model']
        self.label_encoders = model_data['label_encoders']
        self.feature_columns = model_data['feature_columns']
        self.model_type = model_data['model_type']
        self.is_trained = model_data['is_trained']
        print(f"📂 Model loaded from {filepath}")

def train_models():
    """Train both hotel and flight models"""
    
    print("🚀 Starting model training process...")
    
    # Create models directory
    os.makedirs('models', exist_ok=True)
    
    # Train hotel model
    print("\n🏨 Training Hotel Price Model")
    hotel_data = pd.read_csv('data/hotel_prices.csv')
    hotel_model = PriceForecastingModel('hotel')
    hotel_metrics = hotel_model.train(hotel_data)
    hotel_model.save_model('models/hotel_model.pkl')
    
    # Train flight model
    print("\n✈️ Training Flight Price Model")
    flight_data = pd.read_csv('data/flight_prices.csv')
    flight_model = PriceForecastingModel('flight')
    flight_metrics = flight_model.train(flight_data)
    flight_model.save_model('models/flight_model.pkl')
    
    print("\n🎉 Model training completed successfully!")
    
    return hotel_metrics, flight_metrics

def main():
    """Main function to train models"""
    
    # Check if data exists
    if not os.path.exists('data/hotel_prices.csv') or not os.path.exists('data/flight_prices.csv'):
        print("❌ Data files not found. Please run data_generator.py first.")
        return
    
    # Train models
    hotel_metrics, flight_metrics = train_models()
    
    # Display summary
    print("\n📊 Training Summary:")
    print(f"Hotel Model - Test MAE: ${hotel_metrics['test_mae']:.2f}, R²: {hotel_metrics['test_r2']:.3f}")
    print(f"Flight Model - Test MAE: ${flight_metrics['test_mae']:.2f}, R²: {flight_metrics['test_r2']:.3f}")

if __name__ == "__main__":
    main()