import streamlit as st
import joblib
from api import get_coordinates, get_weather, get_air_quality
from disease_logic import predict_diseases

model = joblib.load("air_disease_model.pkl")

st.title("🌍 AI-Based Airborne Disease Prediction System")

city = st.text_input("Enter City Name")

if st.button("Predict"):
    lat, lon = get_coordinates(city)
    weather = get_weather(city)
    air = get_air_quality(lat, lon)

    features = [[air["pm25"], air["pm10"], air["aqi"], air["no2"],
                 air["so2"], air["o3"], weather["temp"], weather["humidity"]]]

    risk = model.predict(features)[0]

    risk_label = ["Low", "Medium", "High"][risk]
    diseases = predict_diseases(air["pm25"], air["pm10"], air["aqi"],
                                weather["temp"], weather["humidity"])

    st.subheader(f"📍 City: {city}")
    st.write("🌡 Temperature:", weather["temp"])
    st.write("💧 Humidity:", weather["humidity"])
    st.write("🌫 PM2.5:", air["pm25"])
    st.write("🌫 PM10:", air["pm10"])
    st.write("📊 AQI:", air["aqi"])

    st.subheader("⚠ Disease Risk Level")
    st.success(risk_label)

    st.subheader("🦠 Probable Airborne Diseases")
    for d in diseases:
        st.write("•", d)
