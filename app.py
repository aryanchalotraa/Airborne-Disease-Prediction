import streamlit as st
import datetime
from api import get_coordinates, get_weather, get_air_quality, get_city_from_coordinates
from disease_logic import predict_diseases
from streamlit_geolocation import streamlit_geolocation

st.set_page_config(page_title="Airborne Disease Predictor", layout="centered")
st.title("🌍 AI-Based Airborne Disease Prediction System")

# Get GPS location
location = streamlit_geolocation()
use_location = st.button("📍 Use My Current Location")

cities = [
    "Delhi","Mumbai","Kolkata","Chennai","Bengaluru","Hyderabad","Ahmedabad","Pune",
    "Jaipur","Chandigarh","Lucknow","Kanpur","Patna","Bhopal","Indore","Raipur",
    "Ranchi","Bhubaneswar","Guwahati","Shillong","Agartala","Imphal",
    "Jammu","Srinagar","Amritsar","Ludhiana","Noida","Ghaziabad","Gurugram",
    "Varanasi","Agra","Surat","Vadodara","Nagpur","Kochi","Puducherry"
]

# Initialize session state for city
if "city" not in st.session_state:
    st.session_state.city = cities[0]

# Dropdown synced with session state
selected_city = st.selectbox(
    "🏙 Select City",
    cities,
    index=cities.index(st.session_state.city) if st.session_state.city in cities else 0
)

# Decide location
if use_location and location and "latitude" in location:
    lat = location["latitude"]
    lon = location["longitude"]
    city = get_city_from_coordinates(lat, lon)

    # Sync dropdown with detected city
    st.session_state.city = city

    st.success(f"Detected City: {city}")
else:
    city = selected_city
    st.session_state.city = city
    lat, lon = get_coordinates(city)

if st.button("🔍 Predict"):
    weather = get_weather(city)
    air = get_air_quality(lat, lon)

    pm25 = air["pm25"]

    # WHO based risk
    if pm25 < 60:
        risk = "Low"
    elif pm25 < 120:
        risk = "Medium"
    else:
        risk = "High"

    diseases = predict_diseases(pm25, air["pm10"], air["aqi"], weather["temp"], weather["humidity"])

    st.subheader(f"📍 {city}")
    st.write("🌡 Temperature:", weather["temp"], "°C")
    st.write("💧 Humidity:", weather["humidity"], "%")
    st.write("🌫 PM2.5:", pm25)
    st.write("🌫 PM10:", air["pm10"])
    st.write("📊 AQI:", air["aqi"])

    st.subheader("⚠ Disease Risk Level")
    st.success(risk)

    st.subheader("🦠 Likely Airborne Diseases")
    for d in diseases:
        st.write("•", d)
