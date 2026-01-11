def predict_diseases(pm25, pm10, aqi, temp, humidity):
    diseases = []

    if pm25 > 150 or aqi > 4:
        diseases += ["Asthma", "COPD"]
    if pm10 > 150:
        diseases.append("Bronchitis")
    if humidity > 70 and temp < 18:
        diseases += ["Influenza", "Pneumonia"]
    if pm25 > 200:
        diseases.append("Tuberculosis Risk")
    if pm25 > 80:
        diseases.append("Allergic Respiratory Infection")

    return list(set(diseases))
