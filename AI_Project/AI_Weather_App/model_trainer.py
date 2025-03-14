from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

def train_model(data):
    """Train model and handle missing values."""
    data = data.fillna(method='ffill').dropna()  # Fix NaN issue

    if data.empty:
        return None

    X = data[['temperature_2m_min']]
    y = data['temperature_2m_max']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, 'weather_model.pkl')  # Save model
    return model
