# agents/packing_assistant.py
"""
GoBabyGo Smart Packing Assistant
Generates dynamic packing lists based on multiple factors
"""

from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Destination:
    name: str
    country: str
    admin: str
    population: int
    type: str
    display: str
    source: str = 'database'

def get_weather_info(destination: Destination) -> Dict[str, str]:
    """Get weather and temperature information for destination"""
    climate_data = {
        'Dubai': {'temp': '35-40°C', 'climate': 'Hot & Humid', 'season': 'Year-round heat'},
        'Hyderabad': {'temp': '25-35°C', 'climate': 'Tropical', 'season': 'Hot, monsoon season'},
        'Stockholm': {'temp': '0-20°C', 'climate': 'Continental', 'season': 'Cold winters'},
        'London': {'temp': '5-22°C', 'climate': 'Oceanic', 'season': 'Mild, rainy'},
        'Tokyo': {'temp': '5-30°C', 'climate': 'Humid subtropical', 'season': 'Four distinct seasons'}
    }
    if destination.name in climate_data:
        return climate_data[destination.name]
    return {'temp': '15-25°C', 'climate': 'Moderate', 'season': 'Year-round'}

def get_smart_packing_list(
    baby_age: int,
    destination: Destination,
    comfort_score: int,
    flight_hours: float,
    special_needs: bool,
    pumping_needed: bool,
    trip_duration: int = 5
) -> List[str]:
    """Generate dynamic packing list based on inputs"""
    base_items = [
        "Diapers", "Wipes", "Changing mat", "Onesies", "Socks",
        "Swaddle blankets", "Pacifiers", "Bottles", "Nursing cover",
        "Baby carrier", "Basic meds", "Thermometer", "Snacks"
    ]
    if baby_age <= 6:
        base_items += ["Formula or breastmilk storage", "Burp cloths", "Portable sterilizer"]
    elif baby_age <= 12:
        base_items += ["Teething toys", "Light books"]
    else:
        base_items += ["Activity books", "Utensils", "Travel stroller"]

    if comfort_score < 5 or trip_duration > 10:
        base_items += ["Extra clothes", "Portable laundry detergent", "Medicine kit"]
    if flight_hours > 5:
        base_items += ["Extra diapers for flight", "Flight pillow", "Tablet with baby videos"]
    if special_needs:
        base_items += ["Medical documentation", "Prescription supplies"]
    if pumping_needed:
        base_items += ["Pump kit", "Extra bottles", "Cooler bag"]

    return sorted(set(base_items))

def validate_packing_list(packing_list: List[str], baby_age: int, trip_duration: int) -> Dict[str, List[str]]:
    """Validate packing list and suggest missing items"""
    essential_keywords = {
        "diapers": "Diapers",
        "wipes": "Wipes",
        "bottles": "Bottles",
        "clothes": "Clothes",
        "medical": "Basic meds"
    }
    missing_items = []
    included_items = []
    list_text = ' '.join(packing_list).lower()
    for keyword, item_name in essential_keywords.items():
        if keyword in list_text:
            included_items.append(item_name)
        else:
            missing_items.append(item_name)
    if baby_age <= 6 and 'burp' not in list_text:
        missing_items.append("Burp cloths")
    if trip_duration > 7 and 'laundry' not in list_text:
        missing_items.append("Laundry detergent")
    return {
        "missing_essentials": missing_items,
        "included_essentials": included_items,
        "validation_score": len(included_items) / len(essential_keywords) * 100
    }