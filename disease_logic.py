def predict_diseases(pm25, pm10, aqi, temp, humidity):
    diseases = []

    if pm25 > 40:
        diseases += ["Allergic Rhinitis", "Mild Asthma"]

    if pm25 > 100:
        diseases += ["Asthma", "COPD"]

    if pm10 > 120:
        diseases.append("Bronchitis")

    if humidity > 65 and temp < 18:
        diseases += ["Influenza", "Pneumonia"]

    if pm25 > 200:
        diseases.append("Tuberculosis Risk")

    return list(set(diseases))
