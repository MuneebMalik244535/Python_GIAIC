import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from data_loader import fetch_past_weather  # ✅ Past weather data fetch karne ke liye

def train_model(city_name):
    """Fetch past weather data and train model with missing value handling."""
    data = fetch_past_weather(city_name)  # ✅ Get past weather data

    if data.empty:
        print("⚠️ No past weather data found! Cannot train model.")
        return None

    # ✅ Fix NaN (missing values) using forward fill & drop remaining NaNs
    data = data.fillna(method='ffill').dropna()

    if data.empty:
        print("❌ Data is still empty after removing NaN values!")
        return None

    # ✅ Train model using real past data
    X = data[['temperature_2m_min']]
    y = data['temperature_2m_max']

    model = LinearRegression()
    model.fit(X, y)

    # ✅ Save Model
    joblib.dump(model, 'weather_model.pkl')
    print(f"✅ Model trained & saved successfully for {city_name}!")

# 🔥 Train model for a city
train_model("Lahore")
