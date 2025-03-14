import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_past_weather(city_name):
    """Fetch past weather data using city name (Not Latitude/Longitude)"""
    
    # Convert City Name to Latitude/Longitude
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    geo_response = requests.get(geo_url).json()

    if "results" not in geo_response:
        return pd.DataFrame()  # Return empty if no results found

    latitude = geo_response["results"][0]["latitude"]
    longitude = geo_response["results"][0]["longitude"]

    # Get Past Weather Data
    today = datetime.today()
    start_date = (today - timedelta(days=60)).strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")

    weather_url = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    response = requests.get(weather_url).json()

    df = pd.DataFrame({
        'date': response['daily']['time'],
        'temperature_2m_max': response['daily']['temperature_2m_max'],
        'temperature_2m_min': response['daily']['temperature_2m_min']
    })
    
    return df
