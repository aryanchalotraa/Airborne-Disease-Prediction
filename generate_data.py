import pandas as pd
import random

data = []

for _ in range(1000):
    pm25 = random.uniform(10, 250)
    pm10 = random.uniform(20, 300)
    aqi = random.uniform(50, 250)
    temperature = random.uniform(5, 45)
    humidity = random.uniform(20, 90)
    wind_speed = random.uniform(0, 10)
    rainfall = random.uniform(0, 20)
    pressure = random.uniform(980, 1030)

    data.append([
        pm25, pm10, aqi, temperature, humidity,
        wind_speed, rainfall, pressure
    ])

df = pd.DataFrame(data, columns=[
    "pm25","pm10","aqi","temperature","humidity",
    "wind_speed","rainfall","pressure"
])

df.to_csv("disease_data.csv", index=False)
print("disease_data.csv created")
