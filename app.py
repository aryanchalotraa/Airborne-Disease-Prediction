import streamlit as st
import requests
from disease_logic import predict_disease_risk

API_KEY = "def170ff2ceeefcf8dc003e413dd12b1"

# -----------------------------
# Get Latitude & Longitude
# -----------------------------
def get_lat_lon(city):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    data = requests.get(url).json()
    return data[0]["lat"], data[0]["lon"]

# -----------------------------
# Weather Data
# -----------------------------
def get_weather(city):
    lat, lon = get_lat_lon(city)
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "rainfall": data.get("rain", {}).get("1h", 0),
        "pressure": data["main"]["pressure"]
    }

# -----------------------------
# Air Quality Data
# -----------------------------
def get_air_quality(city):
    lat, lon = get_lat_lon(city)
    url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    data = requests.get(url).json()["list"][0]

    return {
        "aqi": data["main"]["aqi"] * 50,
        "pm25": data["components"]["pm2_5"],
        "pm10": data["components"]["pm10"]
    }

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Environmental Disease Predictor", layout="centered")
st.title("🌍 Environmental Disease Prediction System")

cities = ["Delhi", "Jammu", "Mumbai", "Kolkata", "Chandigarh", "Shimla"]
city = st.selectbox("Select City", cities)

if st.button("Predict"):
    air_data = get_air_quality(city)
    weather_data = get_weather(city)

    result = predict_disease_risk(air_data, weather_data)

    st.markdown("---")
    st.subheader("🌍 Environmental Conditions")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🌡 Weather")
        st.metric("Temperature (°C)", f"{weather_data['temperature']}")
        st.metric("Humidity (%)", f"{weather_data['humidity']}")
        st.metric("Pressure (hPa)", f"{weather_data['pressure']}")

    with col2:
        st.markdown("### 🌬 Air Quality")
        st.metric("AQI", f"{air_data['aqi']}")
        st.metric("PM2.5 (µg/m³)", f"{air_data['pm25']:.1f}")
        st.metric("PM10 (µg/m³)", f"{air_data['pm10']:.1f}")

    st.markdown("---")
    st.subheader("🩺 Health Risk")

    if result["risk_level"] == "High":
        st.error("🚨 High Risk Area")
    elif result["risk_level"] == "Medium":
        st.warning("⚠️ Medium Risk Area")
    else:
        st.success("✅ Low Risk Area")

    st.markdown("### 🔬 Most Likely Diseases")
    for d in result["predicted_diseases"]:
        st.markdown(f"- **{d}**")
