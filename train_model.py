import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("disease_data.csv")

def create_risk(row):
    if row["pm25"] > 120 or row["aqi"] > 180:
        return "High"
    elif row["pm25"] > 60:
        return "Medium"
    else:
        return "Low"

df["risk"] = df.apply(create_risk, axis=1)

X = df[[
    "pm25", "pm10", "aqi",
    "temperature", "humidity",
    "wind_speed", "rainfall",
    "pressure"
]]

y = df["risk"]

model = RandomForestClassifier(n_estimators=200)
model.fit(X, y)

joblib.dump(model, "air_disease_model.pkl")
print("Model trained successfully")
