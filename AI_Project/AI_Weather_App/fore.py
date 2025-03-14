import requests
import pandas as pd
from datetime import datetime, timedelta

# 🌍 Function to get latitude/longitude from city name
def get_coordinates(city):
    GEO_URL = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    response = requests.get(GEO_URL).json()
    
    if "results" in response:
        return response["results"][0]["latitude"], response["results"][0]["longitude"]
    return None, None

# 📅 Function to fetch 7-Day Weather Forecast
def get_forecast(city):
    lat, lon = get_coordinates(city)
    if lat is None or lon is None:
        return "⚠️ Invalid City Name! Try Again."

    WEATHER_URL = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto"
    response = requests.get(WEATHER_URL).json()

    forecast_data = []
    for i in range(7):
        date = response["daily"]["time"][i]
        max_temp = response["daily"]["temperature_2m_max"][i]
        min_temp = response["daily"]["temperature_2m_min"][i]
        rain = response["daily"]["precipitation_sum"][i]

        # Weather Conditions
        if max_temp >= 30:
            weather_icon, condition = "🔥", "Hot"
        elif max_temp >= 20:
            weather_icon, condition = "🌤️", "Sunny"
        elif max_temp >= 10:
            weather_icon, condition = "⛅", "Cloudy"
        else:
            weather_icon, condition = "❄️", "Cold"

        rain_icon = "🌧️ Rainy" if rain > 5 else "🌞 Dry"

        forecast_data.append({
            "date": date, "max_temp": max_temp, "min_temp": min_temp,
            "icon": weather_icon, "condition": condition, "rain": rain_icon
        })

    return forecast_data

# 📊 Function to fetch Past 30 Days Weather Data
def get_past_weather(city):
    lat, lon = get_coordinates(city)
    if lat is None or lon is None:
        return pd.DataFrame()

    today = datetime.today()
    start_date = (today - timedelta(days=30)).strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")

    PAST_WEATHER_URL = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto"
    response = requests.get(PAST_WEATHER_URL).json()

    df = pd.DataFrame({
        "Date": response["daily"]["time"],
        "Max Temp (°C)": response["daily"]["temperature_2m_max"],
        "Min Temp (°C)": response["daily"]["temperature_2m_min"],
        "Rain (mm)": response["daily"]["precipitation_sum"]
    })

    return df
