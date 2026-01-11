def predict_diseases(pm25, pm10, aqi, temp, humidity):
    # Extreme pollution
    if pm25 > 200:
        diseases = ["Tuberculosis Risk", "COPD", "Asthma"]
        if pm10 > 150:
            diseases.append("Bronchitis")
        return diseases

    # High pollution
    if pm25 > 100:
        diseases = ["Asthma", "COPD"]
        if pm10 > 120:
            diseases.append("Bronchitis")

    # Moderate pollution
    elif pm25 > 40:
        diseases = ["Allergic Rhinitis", "Mild Asthma"]

    # Low pollution
    else:
        diseases = []

    # Weather-based infections
    if humidity > 65 and temp < 18:
        diseases += ["Influenza", "Pneumonia"]

    return list(set(diseases))
