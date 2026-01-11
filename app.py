import streamlit as st
import joblib
from api import get_coordinates, get_weather, get_air_quality
from disease_logic import predict_diseases

# Load trained AI model
model = joblib.load("air_disease_model.pkl")

st.set_page_config(page_title="Airborne Disease Predictor", layout="centered")
st.title("🌍 AI-Based Airborne Disease Prediction System")

st.markdown("Predict **airborne disease risk and respiratory infections** using real-time air quality and weather data.")

# City dropdown list
cities = [
    "Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru", "Hyderabad", "Ahmedabad", "Pune",
    "Jaipur", "Chandigarh", "Lucknow", "Kanpur", "Patna", "Bhopal", "Indore", "Raipur",
    "Ranchi", "Bhubaneswar", "Guwahati", "Shillong", "Agartala", "Imphal", "Aizawl",
    "Kohima", "Itanagar", "Gangtok", "Siliguri", "Darjeeling",
    "Jammu", "Srinagar", "Leh", "Amritsar", "Ludhiana", "Jalandhar",
    "Dehradun", "Haridwar", "Roorkee", "Shimla", "Dharamshala", "Manali",
    "Noida", "Greater Noida", "Ghaziabad", "Gurugram", "Faridabad",
    "Meerut", "Moradabad", "Bareilly", "Aligarh", "Agra", "Mathura",
    "Varanasi", "Prayagraj", "Ayodhya", "Gorakhpur",
    "Gaya", "Bhagalpur", "Muzaffarpur",
    "Jamshedpur", "Dhanbad", "Bokaro",
    "Durg", "Bhilai", "Korba",
    "Udaipur", "Ajmer", "Kota", "Bikaner", "Jodhpur",
    "Surat", "Vadodara", "Rajkot", "Bhavnagar",
    "Nashik", "Aurangabad", "Nagpur", "Amravati",
    "Vijayawada", "Visakhapatnam", "Guntur", "Nellore",
    "Coimbatore", "Madurai", "Salem", "Trichy", "Erode",
    "Kochi", "Thiruvananthapuram", "Kozhikode",
    "Puducherry"
]

city = st.selectbox("🏙 Select City", cities)

if st.button("🔍 Predict"):
    try:
        # Fetch live data
        lat, lon = get_coordinates(city)
        weather = get_weather(city)
        air = get_air_quality(lat, lon)

        # Prepare ML input
        features = [[
            air["pm25"], air["pm10"], air["aqi"],
            air["no2"], air["so2"], air["o3"],
            weather["temp"], weather["humidity"]
        ]]

        # Predict risk
        risk = model.predict(features)[0]
        risk_label = ["Low", "Medium", "High"][risk]

        # Predict diseases
        diseases = predict_diseases(
            air["pm25"], air["pm10"], air["aqi"],
            weather["temp"], weather["humidity"]
        )

        # Display results
        st.subheader(f"📍 {city}")
        st.write(f"🌡 Temperature: {weather['temp']} °C")
        st.write(f"💧 Humidity: {weather['humidity']} %")
        st.write(f"🌫 PM2.5: {air['pm25']}")
        st.write(f"🌫 PM10: {air['pm10']}")
        st.write(f"📊 AQI: {air['aqi']}")

        st.subheader("⚠ Disease Risk Level")
        if risk_label == "High":
            st.error(risk_label)
        elif risk_label == "Medium":
            st.warning(risk_label)
        else:
            st.success(risk_label)

        st.subheader("🦠 Probable Airborne Diseases")
        for d in diseases:
            st.write("•", d)

    except:
        st.error("Unable to fetch data for this city. Please try another.")

