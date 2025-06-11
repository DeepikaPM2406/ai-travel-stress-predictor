import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather_by_city(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['main']
            temp = data['main']['temp']
            return weather.lower(), round(temp)
        else:
            return None, None
    except Exception:
        return None, None

def classify_temperature(temp):
    if temp is None:
        return "unknown"
    elif temp < 10:
        return "cold"
    elif 10 <= temp < 20:
        return "cool"
    elif 20 <= temp < 30:
        return "pleasant"
    else:
        return "hot"
