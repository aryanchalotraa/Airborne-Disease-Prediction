import joblib

model = joblib.load("air_disease_model.pkl")

def combine_features(air_data, weather_data):
    return [
        air_data.get("pm25", 0),
        air_data.get("pm10", 0),
        air_data.get("aqi", 0),
        weather_data.get("temperature", 0),
        weather_data.get("humidity", 0),
        weather_data.get("wind_speed", 0),
        weather_data.get("rainfall", 0),
        weather_data.get("pressure", 1013)
    ]

def map_specific_diseases(air_data, weather_data):
    disease_scores = {}

    # Pollution-based diseases
    if air_data["pm25"] > 100 or air_data["pm10"] > 150:
        disease_scores["Asthma"] = 3
        disease_scores["Bronchitis"] = 3
        disease_scores["COPD"] = 3
        disease_scores["Lung Infection"] = 2

    # Weather-based diseases
    if weather_data["temperature"] < 15 and weather_data["humidity"] > 60:
        disease_scores["Influenza"] = 3
        disease_scores["Pneumonia"] = 3
        disease_scores["Viral Infection"] = 2

    # Sort by severity and return top 3
    top = sorted(disease_scores, key=disease_scores.get, reverse=True)
    return top[:3]

def predict_disease_risk(air_data, weather_data):
    features = combine_features(air_data, weather_data)
    risk = model.predict([features])[0]
    diseases = map_specific_diseases(air_data, weather_data)

    return {
        "risk_level": risk,
        "predicted_diseases": diseases
    }
