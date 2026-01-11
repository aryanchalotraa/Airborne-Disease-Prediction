import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

data = pd.read_csv("air_quality_health_impact_data.csv")

cols = ["PM2_5","PM10","AQI","NO2","SO2","O3","Temperature","Humidity","HealthImpactClass"]
data = data[cols]

le = LabelEncoder()
data["HealthImpactClass"] = le.fit_transform(data["HealthImpactClass"])

X = data.drop("HealthImpactClass", axis=1)
y = data["HealthImpactClass"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

joblib.dump(model, "air_disease_model.pkl")
print("Model trained and saved")
