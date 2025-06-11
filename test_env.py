import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
print("✅ API Key loaded:", api_key if api_key else "❌ Not found")
