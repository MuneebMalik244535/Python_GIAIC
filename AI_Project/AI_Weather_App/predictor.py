import joblib
import numpy as np

def predict_temperature(temp_min):
    """Load trained model & predict next week's max temperature."""
    model = joblib.load('weather_model.pkl')  # Load model
    temp_max = model.predict(np.array([[temp_min]]))[0]
    return round(temp_max, 2)
