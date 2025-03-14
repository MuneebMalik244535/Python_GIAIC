import joblib
import numpy as np
from data_loader import fetch_past_weather

def predict_next_week_temp(city_name):
    """Predict next week's max temperature using past weather data."""
    model = joblib.load('weather_model.pkl')  # ✅ Load trained model
    past_data = fetch_past_weather(city_name)  # ✅ Get past weather data

    if past_data.empty:
        return "⚠️ No past weather data available!"

    last_min_temp = past_data['temperature_2m_min'].iloc[-1]  # ✅ Get latest min temp
    predicted_max_temp = model.predict(np.array([[last_min_temp]]))[0]

    return round(predicted_max_temp, 2)

# 🔥 Example usage:
# print(predict_next_week_temp("Lahore"))
