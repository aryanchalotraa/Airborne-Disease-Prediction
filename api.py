import requests

API_KEY = ""

def get_coordinates(city):
    city = city.strip()
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},IN&limit=1&appid={API_KEY}"
    data = requests.get(url).json()
    if not isinstance(data, list) or len(data) == 0:
        raise Exception("City not found")
    return data[0]["lat"], data[0]["lon"]

def get_city_from_coordinates(lat, lon):
    url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={API_KEY}"
    try:
        data = requests.get(url).json()
    except:
        return "Delhi"

    if not isinstance(data, list) or len(data) == 0:
        return "Delhi"

    return data[0].get("name", "Delhi")

def get_weather(city):
    city = city.strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
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
