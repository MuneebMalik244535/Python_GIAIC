import streamlit as st
from weather import get_current_weather
from fore import get_forecast, get_past_weather
from predictor import predict_temperature

# 🌤 Set Page Configuration
st.set_page_config(page_title="AI Weather App", page_icon="🌍", layout="wide")

# 🎨 Title & Description
st.markdown("""
    <h1 style="text-align: center; color: #4A90E2;">🌍 AI-Based Weather App</h1>
    <p style="text-align: center; font-size: 18px;">Check current weather, 7-day forecast, and past 30 days data with AI predictions.</p>
    <hr>
""", unsafe_allow_html=True)

# 🏙 User Input for City Name
city_name = st.text_input("🏙 Enter City Name:", placeholder="e.g. Lahore, New York, Tokyo")

if st.button("🔍 Get Weather & Forecast"):
    if city_name:
        # 🌍 Fetch Current Weather
        weather = get_current_weather(city_name)
        if weather:
            st.subheader(f"📍 Current Weather in {city_name}")
            st.write(f"🌡 Temperature: **{weather['temp']}°C**")
            st.write(f"☁ Condition: **{weather['condition']} {weather['icon']}**")
            st.write(f"💨 Wind Speed: **{weather['wind']} m/s**")
            st.write(f"💧 Humidity: **{weather['humidity']}%**")

        # 📅 Fetch 7-Day Forecast
        forecast_data = get_forecast(city_name)
        if isinstance(forecast_data, list):  
            st.subheader("📅 7-Day Weather Forecast")
            cols = st.columns(len(forecast_data))
            for col, day in zip(cols, forecast_data):
                col.markdown(f"""
                    <div style="text-align: center; background-color: #f8f9fa; padding: 10px; border-radius: 10px;">
                        <h3 style="color: #007bff;">📅 {day['date']}</h3>
                        <h1>{day['icon']}</h1>
                        <h3>{day['condition']}</h3>
                        <p style="font-size: 20px;">🌡 Max: {day['max_temp']}°C</p>
                        <p style="font-size: 20px;">❄ Min: {day['min_temp']}°C</p>
                        <p style="font-size: 18px;">{day['rain']}</p>
                    </div>
                """, unsafe_allow_html=True)

        # 📊 Fetch Past 30 Days Weather
        past_data = get_past_weather(city_name)
        if not past_data.empty:
            st.subheader("📊 Past 30 Days Weather Data")
            st.dataframe(past_data)

    else:
        st.warning("⚠️ Please enter a valid city name.")

# 🔮 AI-Based Prediction Section
st.header("🔮 Predict Next Week's Temperature")
temp_min = st.number_input("Enter Expected Min Temp (°C)", value=10.0)

if st.button("Predict Temperature"):
    temp_max = predict_temperature(temp_min)
    st.success(f"🌡 Predicted Max Temperature for Next Week: {temp_max}°C")
