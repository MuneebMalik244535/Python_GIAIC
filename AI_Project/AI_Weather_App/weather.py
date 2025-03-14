import requests

def get_current_weather(city_name):
    """Fetch current weather data using city name."""
    API_KEY = "your_api_key_here"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["description"].title(),
            "wind": data["wind"]["speed"],
            "humidity": data["main"]["humidity"]
        }

        # Assigning Weather Icons
        if "cloud" in weather["condition"].lower():
            weather["icon"] = "☁"
        elif "rain" in weather["condition"].lower():
            weather["icon"] = "🌧"
        elif "clear" in weather["condition"].lower():
            weather["icon"] = "☀"
        else:
            weather["icon"] = "⛅"

        return weather
    else:
        return None
