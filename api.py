import requests

API_KEY = "def170ff2ceeefcf8dc003e413dd12b1"

def get_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    data = requests.get(url).json()
    return data[0]["lat"], data[0]["lon"]

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()
    return {
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"]
    }

def get_air_quality(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    data = requests.get(url).json()["list"][0]
    return {
        "pm25": data["components"]["pm2_5"],
        "pm10": data["components"]["pm10"],
        "no2": data["components"]["no2"],
        "so2": data["components"]["so2"],
        "co": data["components"]["co"],
        "o3": data["components"]["o3"],
        "aqi": data["main"]["aqi"]
    }
