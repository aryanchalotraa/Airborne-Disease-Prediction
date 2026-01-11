import streamlit as st
import datetime

from api import get_coordinates, get_weather, get_air_quality
from disease_logic import predict_diseases
from influenza import predict_influenza

# -------------------------------
# STREAMLIT CONFIG
# -------------------------------
st.set_page_config(
    page_title="HealthSense AI",
    layout="centered"
)

st.title("🌍 HealthSense AI")
st.subheader("Climate-Driven Health Risk Prediction System")

st.markdown(
    """
This system predicts **regional health risks** based on  
🌦 weather conditions, 🌫 air quality, and 🧠 epidemiological patterns.

⚠️ *This is NOT a diagnostic system.*
"""
)

# -------------------------------
# CITY SELECTION
# -------------------------------
cities = [
    "Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru",
    "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Chandigarh",
    "Jammu", "Srinagar", "Amritsar", "Ludhiana", "Dehradun"
]

city = st.selectbox("🏙 Select City", cities)

# -------------------------------
# PREDICTION BUTTON
# -------------------------------
if st.button("🔍 Predict Health Risk"):

    try:
        # -------------------------------
        # FETCH LIVE DATA
        # -------------------------------
        lat, lon = get_coordinates(city)
        weather = get_weather(city)
        air = get_air_quality(lat, lon)

        current_month = datetime.datetime.now().month

        # -------------------------------
        # INFLUENZA RISK (SEASONAL MODEL)
        # -------------------------------
        flu_risk = predict_influenza(
            month=current_month,
            temperature=weather["temp"],
            humidity=weather["humidity"]
        )

        # -------------------------------
        # OTHER CLIMATE / AIR RISKS
        # -------------------------------
        other_risks = predict_diseases(
            pm25=air["pm25"],
            pm10=air["pm10"],
            aqi=air["aqi"],
            temp=weather["temp"],
            humidity=weather["humidity"],
            month=current_month
        )

        # -------------------------------
        # DISPLAY RESULTS
        # -------------------------------
        st.subheader(f"📍 {city}")

        st.markdown("### 🌦 Current Environmental Conditions")
        st.write(f"🌡 Temperature: {weather['temp']} °C")
        st.write(f"💧 Humidity: {weather['humidity']} %")
        st.write(f"🌫 PM2.5: {air['pm25']}")
        st.write(f"🌫 PM10: {air['pm10']}")
        st.write(f"📊 AQI Index: {air['aqi']}")

        # -------------------------------
        # INFLUENZA RESULT
        # -------------------------------
        st.markdown("### 😷 Seasonal Influenza Risk (Monthly)")
        if flu_risk == "High":
            st.error(flu_risk)
        elif flu_risk == "Medium":
            st.warning(flu_risk)
        else:
            st.success(flu_risk)

        # -------------------------------
        # OTHER HEALTH RISKS
        # -------------------------------
        st.markdown("### ⚠ Other Climate-Driven Health Risks")
        if other_risks:
            for risk in other_risks:
                st.write("•", risk)
        else:
            st.success("No major climate-related health risks detected")

        # -------------------------------
        # EXPLANATION (VERY IMPORTANT)
        # -------------------------------
        st.markdown("### 📌 Why these risks?")
        st.write("• High air pollution increases respiratory stress")
        st.write("• Cold temperatures and high humidity increase influenza spread")
        st.write("• Extreme heat can cause dehydration and heat exhaustion")
        st.write("• High humidity increases skin infection risk")

        st.caption(
            "⚠ This system predicts **regional health risk patterns** only. "
            "It does not diagnose individuals or replace medical professionals."
        )

    except Exception as e:
        st.error("Unable to fetch data for this city. Please try another.")
        st.write("Debug info:", e)
