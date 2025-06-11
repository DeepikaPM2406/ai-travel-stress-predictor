from utils.weather import get_weather_by_city

weather, temp = get_weather_by_city("Dubai")  # Try other cities like Helsinki or New York

if weather:
    print(f"🌤 Weather in Dubai: {weather.title()} ({temp}°C)")
else:
    print("❌ Weather fetch failed.")
