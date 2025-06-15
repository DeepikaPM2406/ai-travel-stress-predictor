# agents/stress_predictor.py
"""
Enhanced Travel Stress Predictor with Departure Search & Trip Duration
"""

import streamlit as st
import time
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

# Import streamlit-searchbox for autocomplete
try:
    from streamlit_searchbox import st_searchbox
    SEARCHBOX_AVAILABLE = True
except ImportError:
    SEARCHBOX_AVAILABLE = False
    st.warning("⚠️ Install streamlit-searchbox for better search: `pip install streamlit-searchbox`")

@dataclass
class Destination:
    name: str
    country: str
    admin: str
    population: int
    type: str
    display: str
    source: str = 'database'

@dataclass
class ProductRecommendation:
    name: str
    description: str
    amazon_url: str
    price_range: str
    rating: str
    category: str

class GlobalLocationService:
    def __init__(self):
        self._search_cache = {}
        self.top_family_destinations = [
            'Dubai', 'Singapore', 'Tokyo', 'London', 'Sydney', 
            'Barcelona', 'Amsterdam', 'Copenhagen', 'Reykjavik', 'Paris'
        ]
        self.all_locations = self._load_all_locations()
    
    def _load_all_locations(self) -> List[Destination]:
        """Load all locations for autocomplete"""
        try:
            import sys
            import os
            
            # Add current directory to path
            current_dir = os.path.dirname(os.path.abspath(__file__))
            if current_dir not in sys.path:
                sys.path.append(current_dir)
            parent_dir = os.path.dirname(current_dir)
            if parent_dir not in sys.path:
                sys.path.append(parent_dir)
            
            from world_locations import WORLD_LOCATIONS, format_display_name
            
            locations = []
            for name, data in WORLD_LOCATIONS.items():
                dest = Destination(
                    name=name,
                    country=data['country'],
                    admin=data.get('admin', ''),
                    population=data['population'],
                    type=data['type'],
                    display=format_display_name(data, name),
                    source='database'
                )
                locations.append(dest)
            
            return locations
            
        except Exception as e:
            st.error(f"Could not load locations: {e}")
            # Fallback locations
            return [
                Destination('Dubai', 'United Arab Emirates', 'Dubai', 3500000, 'city', 'Dubai, UAE'),
                Destination('London', 'United Kingdom', 'England', 9000000, 'city', 'London, UK'),
                Destination('Tokyo', 'Japan', 'Tokyo', 14000000, 'city', 'Tokyo, Japan'),
                Destination('New York', 'United States', 'New York', 8400000, 'city', 'New York, USA'),
                Destination('Singapore', 'Singapore', '', 6000000, 'city', 'Singapore'),
            ]
    
    def search_destinations_autocomplete(self, searchterm: str) -> List[str]:
        """Autocomplete search function for streamlit-searchbox"""
        if not searchterm:
            # Return top destinations for empty search
            return [dest.display for dest in self.all_locations[:10] 
                   if dest.name in self.top_family_destinations]
        
        searchterm_lower = searchterm.lower()
        matches = []
        
        for dest in self.all_locations:
            if (searchterm_lower in dest.name.lower() or 
                searchterm_lower in dest.country.lower() or
                searchterm_lower in dest.display.lower()):
                matches.append(dest.display)
                if len(matches) >= 20:  # Limit results
                    break
        
        return matches
    
    def get_destination_by_display(self, display_name: str) -> Optional[Destination]:
        """Get destination object by display name"""
        for dest in self.all_locations:
            if dest.display == display_name:
                return dest
        return None
    
    def search_destinations(self, query: str, limit: int = 8) -> List[Destination]:
        """Fallback search method"""
        if not query:
            return [dest for dest in self.all_locations[:limit] 
                   if dest.name in self.top_family_destinations]
        
        query_lower = query.lower()
        results = []
        
        for dest in self.all_locations:
            if (query_lower in dest.name.lower() or 
                query_lower in dest.country.lower()):
                results.append(dest)
                if len(results) >= limit:
                    break
        
        return results

class TravelStressAnalyzer:
    @staticmethod
    def calculate_comprehensive_stress(
        baby_age: int, flight_hours: float, layovers: int, departure_time: str,
        has_partner: bool, special_needs: bool, pumping_needed: bool, 
        first_international: bool, parent_experience: str, destination: Destination,
        departure_location: Optional[Destination] = None, trip_duration: int = 5
    ) -> Tuple[int, dict]:
        
        factors = {
            'baby_age': 0, 'flight_duration': 0, 'layovers': 0, 'timing': 0,
            'support': 0, 'medical': 0, 'logistics': 0, 'experience': 0, 
            'destination': 0, 'trip_length': 0
        }
        
        # Baby age factor (FIXED - 4 months should be low stress)
        if baby_age <= 3:
            factors['baby_age'] = 1  # Very young, sleeps a lot
        elif baby_age <= 6:
            factors['baby_age'] = 1  # Still portable, manageable (4 months = LOW stress)
        elif baby_age <= 11:
            factors['baby_age'] = 3  # Mobile, more challenging
        elif baby_age <= 18:
            factors['baby_age'] = 2  # Active but can be reasoned with
        else:
            factors['baby_age'] = 1  # Can communicate needs
        
        # Flight duration (FIXED scaling)
        if flight_hours > 12:
            factors['flight_duration'] = 3
        elif flight_hours > 8:
            factors['flight_duration'] = 2
        elif flight_hours > 5:
            factors['flight_duration'] = 1  # 3.5 hours = minimal stress
        else:
            factors['flight_duration'] = 0  # Short flights are easy
        
        # Layovers (direct flight = 0 stress)
        factors['layovers'] = min(layovers, 2)  # Direct flight = 0
        
        # Timing
        timing_stress = {
            "Morning (7-11 AM)": 0,
            "Afternoon (11 AM-5 PM)": 1, 
            "Evening (5-10 PM)": 0,
            "Very Early (5-7 AM)": 2,
            "Late Night (10 PM-12 AM)": 1,
            "Red-eye (12-5 AM)": 3
        }
        factors['timing'] = timing_stress.get(departure_time, 1)
        
        # Trip duration factor (NEW)
        if trip_duration <= 3:
            factors['trip_length'] = 0  # Short trips are easier
        elif trip_duration <= 7:
            factors['trip_length'] = 1  # Week-long trips
        elif trip_duration <= 14:
            factors['trip_length'] = 2  # Two weeks
        else:
            factors['trip_length'] = 3  # Extended trips
        
        # Support
        if not has_partner:
            factors['support'] = 2  # Reduced from 3
        
        # Medical and logistics
        if special_needs:
            factors['medical'] = 2  # Reduced from 3
        if pumping_needed:
            factors['logistics'] += 1
        if first_international:
            factors['logistics'] += 1
        
        # Experience
        experience_stress = {
            "First time flying with baby": 2,  # Reduced from 3
            "2-3 previous flights": 1,
            "Experienced traveler (4+ flights)": 0,
            "Travel veteran (10+ flights)": 0
        }
        factors['experience'] = experience_stress.get(parent_experience, 1)
        
        # Destination difficulty
        easy_destinations = ['Dubai', 'Singapore', 'Tokyo', 'London', 'Sydney', 'Barcelona', 'Amsterdam', 'Copenhagen', 'Reykjavik', 'Paris']
        moderate_destinations = ['New York', 'Los Angeles', 'Rome', 'Berlin', 'Madrid', 'Istanbul', 'Mumbai', 'Delhi', 'Hyderabad']
        
        if destination.name in easy_destinations:
            factors['destination'] = 0
        elif destination.name in moderate_destinations:
            factors['destination'] = 1  # Hyderabad = moderate, not high
        else:
            factors['destination'] = 1
        
        total_stress = sum(factors.values())
        final_stress = max(1, min(total_stress, 10))
        
        return final_stress, factors

def get_weather_info(destination: Destination) -> Dict[str, str]:
    """Get weather and temperature information for destination"""
    
    # Climate data for major destinations
    climate_data = {
        # Hot climates
        'Dubai': {'temp': '35-40°C', 'climate': 'Hot & Humid', 'season': 'Year-round heat'},
        'Hyderabad': {'temp': '25-35°C', 'climate': 'Tropical', 'season': 'Hot, monsoon season'},
        'Mumbai': {'temp': '25-32°C', 'climate': 'Tropical', 'season': 'Hot & humid'},
        'Delhi': {'temp': '20-35°C', 'climate': 'Continental', 'season': 'Varies by season'},
        'Bangkok': {'temp': '25-35°C', 'climate': 'Tropical', 'season': 'Hot & humid'},
        'Singapore': {'temp': '25-32°C', 'climate': 'Tropical', 'season': 'Consistently warm'},
        
        # Cold climates
        'Stockholm': {'temp': '0-20°C', 'climate': 'Continental', 'season': 'Cold winters'},
        'Helsinki': {'temp': '-5-22°C', 'climate': 'Continental', 'season': 'Very cold winters'},
        'Oslo': {'temp': '-5-20°C', 'climate': 'Continental', 'season': 'Cold winters'},
        'Reykjavik': {'temp': '0-15°C', 'climate': 'Oceanic', 'season': 'Cool year-round'},
        'Copenhagen': {'temp': '2-22°C', 'climate': 'Oceanic', 'season': 'Mild but cool'},
        
        # Moderate climates
        'London': {'temp': '5-22°C', 'climate': 'Oceanic', 'season': 'Mild, rainy'},
        'Paris': {'temp': '3-25°C', 'climate': 'Oceanic', 'season': 'Mild seasons'},
        'Tokyo': {'temp': '5-30°C', 'climate': 'Humid subtropical', 'season': 'Four distinct seasons'},
        'Sydney': {'temp': '10-25°C', 'climate': 'Oceanic', 'season': 'Mild year-round'},
        'Barcelona': {'temp': '10-28°C', 'climate': 'Mediterranean', 'season': 'Warm summers'},
        'Amsterdam': {'temp': '3-22°C', 'climate': 'Oceanic', 'season': 'Mild, wet'},
    }
    
    # Get climate info for destination
    if destination.name in climate_data:
        return climate_data[destination.name]
    
    # Default based on country/region
    hot_countries = ['India', 'Thailand', 'UAE', 'United Arab Emirates', 'Egypt', 'Malaysia', 'Indonesia']
    cold_countries = ['Sweden', 'Finland', 'Norway', 'Iceland', 'Denmark', 'Canada', 'Russia']
    
    if destination.country in hot_countries:
        return {'temp': '25-35°C', 'climate': 'Tropical/Hot', 'season': 'Generally hot'}
    elif destination.country in cold_countries:
        return {'temp': '0-15°C', 'climate': 'Cold/Continental', 'season': 'Cold winters'}
    else:
        return {'temp': '10-25°C', 'climate': 'Temperate', 'season': 'Moderate climate'}

def get_smart_packing_list(baby_age: int, destination: Destination, stress_score: int, 
                          flight_hours: float, special_needs: bool, pumping_needed: bool,
                          trip_duration: int = 5) -> List[str]:
    """Generate dynamic packing list based on multiple factors including trip duration"""
    
    # Base essentials for all trips
    packing_list = [
        "🧷 Diapers (extra 3 days worth)",
        "🧻 Baby wipes (travel packs)",
        "🍼 Bottles/formula/baby food",
        "👕 Extra clothes (3+ outfit changes)",
        "🧸 Comfort items & favorite toys",
        "🏥 Medical kit & baby thermometer"
    ]
    
    # Trip duration adjustments
    if trip_duration <= 3:  # Short trips (1-3 days)
        packing_list.extend([
            "🎒 Light packing - minimal essentials only",
            "📱 Phone charger & essentials",
            "🧴 Travel-size toiletries"
        ])
    elif trip_duration <= 7:  # Week-long trips
        packing_list.extend([
            "👔 Additional outfit changes (5-7 days)",
            "🧴 Regular-size toiletries",
            "📚 More entertainment options",
            "🧺 Laundry bag for dirty clothes"
        ])
    elif trip_duration <= 14:  # Two weeks
        packing_list.extend([
            "👗 Extended wardrobe (10-14 outfits)",
            "🧴 Full-size toiletries & backup",
            "📖 Books, tablets, extra activities",
            "🧺 Laundry supplies or plan laundry",
            "💊 Extra medications (2+ weeks worth)"
        ])
    else:  # Extended trips (15+ days)
        packing_list.extend([
            "🧳 Large suitcase or multiple bags",
            "👕 Extended wardrobe + shopping plan",
            "🏥 Comprehensive medical kit",
            "📚 Extensive entertainment library",
            "🛒 Plan to buy items locally",
            "📋 Contact local pediatrician"
        ])
    
    # Age-specific items
    if baby_age <= 6:
        packing_list.extend([
            "🍼 Extra formula/baby food",
            "👶 Burp cloths & bibs",
            "🛏️ Portable changing pad"
        ])
        if trip_duration > 7:
            packing_list.append("🍼 Local baby food research")
    elif baby_age <= 12:
        packing_list.extend([
            "🥄 Baby spoon & sippy cup",
            "🎵 Tablet with downloaded content",
            "🧩 Small toys & teething items"
        ])
    else:
        packing_list.extend([
            "📚 Picture books & coloring",
            "🎮 Interactive toys",
            "🥤 Snacks & sippy cups"
        ])
    
    # Destination-specific items
    weather_info = get_weather_info(destination)
    if 'Hot' in weather_info['climate'] or 'Tropical' in weather_info['climate']:
        packing_list.extend([
            "☀️ Strong sunscreen (SPF 50+)",
            "🧴 Extra hydration solutions",
            "👒 Sun hat & light clothing"
        ])
        if trip_duration > 7:
            packing_list.append("🧴 Local sunscreen brands (backup)")
    elif 'Cold' in weather_info['climate'] or 'Continental' in weather_info['climate']:
        packing_list.extend([
            "🧥 Warm layers & winter gear",
            "🧤 Mittens & warm hat",
            "💧 Moisturizer for dry air"
        ])
    
    # Flight duration specific
    if flight_hours > 8:
        packing_list.extend([
            "✈️ Bassinet booking confirmation",
            "🎧 Noise-canceling headphones",
            "🛌 Travel pillow & blanket"
        ])
    
    # Special conditions
    if special_needs:
        packing_list.extend([
            "🏥 All medical records",
            "💊 Prescription letter from doctor"
        ])
        if trip_duration > 7:
            packing_list.append("🏥 Local specialist contacts")
    
    if pumping_needed:
        packing_list.extend([
            "🍼 Breast pump & accessories",
            "❄️ Cooler bag for milk storage"
        ])
    
    # Remove duplicates and limit based on trip length
    unique_list = list(dict.fromkeys(packing_list))
    max_items = 20 + (trip_duration // 3)  # More items for longer trips
    return unique_list[:max_items]

class AmazonProductService:
    """Service for Amazon product recommendations based on travel needs"""
    
    @staticmethod
    def get_temperature_based_products(destination: Destination) -> List[ProductRecommendation]:
        """Get clothing and gear based on destination climate"""
        
        weather_info = get_weather_info(destination)
        products = []
        
        if 'Hot' in weather_info['climate'] or 'Tropical' in weather_info['climate']:
            products.extend([
                ProductRecommendation(
                    "Baby Sun Hat with Neck Protection",
                    "UPF 50+ protection, adjustable chin strap",
                    "https://www.amazon.com/s?k=baby+sun+hat+upf+50&ref=nb_sb_noss",
                    "$15-25", "4.4/5", "sun_protection"
                ),
                ProductRecommendation(
                    "Lightweight Baby Rompers",
                    "Breathable cotton, short sleeve, snap closure",
                    "https://www.amazon.com/s?k=baby+lightweight+rompers+cotton&ref=nb_sb_noss",
                    "$25-35", "4.5/5", "clothing"
                ),
                ProductRecommendation(
                    "Baby Zinc Sunscreen SPF 50+",
                    "Mineral sunscreen, sensitive skin formula",
                    "https://www.amazon.com/s?k=baby+zinc+sunscreen+spf+50&ref=nb_sb_noss",
                    "$18-28", "4.6/5", "sun_protection"
                )
            ])
        elif 'Cold' in weather_info['climate'] or 'Continental' in weather_info['climate']:
            products.extend([
                ProductRecommendation(
                    "Baby Winter Sleep Sack",
                    "Warm fleece, TOG 2.5, various sizes",
                    "https://www.amazon.com/s?k=baby+winter+sleep+sack+fleece&ref=nb_sb_noss",
                    "$30-45", "4.7/5", "warmth"
                ),
                ProductRecommendation(
                    "Thermal Baby Bodysuit Set",
                    "Merino wool blend, long sleeve, 3-pack",
                    "https://www.amazon.com/s?k=baby+thermal+bodysuit+merino+wool&ref=nb_sb_noss",
                    "$45-65", "4.5/5", "clothing"
                ),
                ProductRecommendation(
                    "Baby Winter Hat with Ear Flaps",
                    "Fleece lined, adjustable, wind resistant",
                    "https://www.amazon.com/s?k=baby+winter+hat+ear+flaps&ref=nb_sb_noss",
                    "$15-22", "4.4/5", "warmth"
                )
            ])
        else:
            products.extend([
                ProductRecommendation(
                    "Baby Layer Set (3-piece)",
                    "Onesie + cardigan + pants, mix & match",
                    "https://www.amazon.com/s?k=baby+layer+set+onesie+cardigan&ref=nb_sb_noss",
                    "$35-50", "4.6/5", "clothing"
                )
            ])
        
        return products
    
    @staticmethod
    def get_flight_specific_products(flight_hours: float, baby_age: int) -> List[ProductRecommendation]:
        """Get products based on flight duration and baby age"""
        
        products = [
            ProductRecommendation(
                "Travel Bottle Warmer",
                "Portable, USB rechargeable, fits most bottles",
                "https://www.amazon.com/s?k=travel+bottle+warmer+portable+usb&ref=nb_sb_noss",
                "$35-45", "4.3/5", "feeding"
            ),
            ProductRecommendation(
                "Baby Travel Changing Pad",
                "Foldable, waterproof, includes pockets",
                "https://www.amazon.com/s?k=baby+travel+changing+pad+waterproof&ref=nb_sb_noss",
                "$20-30", "4.5/5", "essentials"
            )
        ]
        
        if flight_hours > 8:
            products.append(
                ProductRecommendation(
                    "Inflatable Baby Travel Bed",
                    "Fits airplane seats, side barriers, compact",
                    "https://www.amazon.com/s?k=inflatable+baby+travel+bed+airplane&ref=nb_sb_noss",
                    "$45-65", "4.1/5", "sleep"
                )
            )
        
        if baby_age >= 6:
            products.append(
                ProductRecommendation(
                    "Baby Travel Activity Table",
                    "Suction cup base, multiple toys, airplane tray compatible",
                    "https://www.amazon.com/s?k=baby+travel+activity+table+suction&ref=nb_sb_noss",
                    "$25-35", "4.5/5", "entertainment"
                )
            )
        
        return products
    
    @staticmethod
    def get_destination_specific_products(destination: Destination) -> List[ProductRecommendation]:
        """Get products based on destination characteristics"""
        
        luxury_destinations = ['Dubai', 'Singapore', 'Tokyo', 'London', 'Paris']
        
        if destination.name in luxury_destinations:
            return [
                ProductRecommendation(
                    "Premium Travel Stroller",
                    "Lightweight, one-hand fold, airplane carry-on size",
                    "https://www.amazon.com/s?k=premium+travel+stroller+lightweight+airplane&ref=nb_sb_noss",
                    "$200-300", "4.7/5", "mobility"
                )
            ]
        else:
            return [
                ProductRecommendation(
                    "Compact Travel Stroller",
                    "Lightweight, easy fold, cup holder included",
                    "https://www.amazon.com/s?k=compact+travel+stroller+lightweight+fold&ref=nb_sb_noss",
                    "$100-150", "4.4/5", "mobility"
                )
            ]

def display_travel_stress_predictor():
    """Enhanced main predictor interface with departure search and trip duration"""
    
    # Enhanced CSS - FIXED for dropdown colors
    st.markdown("""
    <style>
        /* Fix ALL dropdown color issues */
        .stSelectbox > div > div > div {
            background-color: white !important;
            color: #2c3e50 !important;
            border: 2px solid #e9ecef !important;
            border-radius: 8px !important;
        }
        
        .stSelectbox > div > div > div > div {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Fix dropdown menu when opened */
        div[data-baseweb="select"] > div {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Fix dropdown list items */
        div[data-baseweb="select"] ul {
            background-color: white !important;
        }
        
        div[data-baseweb="select"] li {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        div[data-baseweb="select"] li:hover {
            background-color: #f8f9fa !important;
            color: #2c3e50 !important;
        }
        
        /* Fix selected option */
        div[data-baseweb="select"] [aria-selected="true"] {
            background-color: #e3f2fd !important;
            color: #1976d2 !important;
        }
        
        /* Fix ALL select elements */
        .stSelectbox select {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Product cards styling */
        .product-card {
            border: 2px solid #e9ecef;
            border-radius: 12px;
            padding: 15px;
            margin: 10px 0;
            background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .product-link {
            background: linear-gradient(135deg, #ff9500 0%, #ff7700 100%);
            color: white !important;
            padding: 8px 16px;
            border-radius: 6px;
            text-decoration: none !important;
            font-weight: 600;
            display: inline-block;
            margin-top: 8px;
        }
        
        .trip-info-card {
            border: 2px solid #3498db;
            border-radius: 12px;
            padding: 20px;
            margin: 15px 0;
            background: linear-gradient(135deg, #3498db10 0%, #3498db05 100%);
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("# ✈️ AI-Powered Travel Stress Predictor")
    st.markdown("🌍 Complete travel planning with departure search & trip duration")
    
    if 'location_service' not in st.session_state:
        st.session_state.location_service = GlobalLocationService()
    
    if 'selected_destination' not in st.session_state:
        st.session_state.selected_destination = None
    
    if 'selected_departure' not in st.session_state:
        st.session_state.selected_departure = None
    
    st.info("📊 **Enhanced Features:** Departure search • Trip duration • Smart packing • 1000+ destinations")
    st.markdown("---")
    
    # Trip Overview Section
    st.markdown("## 🗺️ Trip Overview")
    trip_col1, trip_col2, trip_col3 = st.columns([1, 1, 1])
    
    with trip_col1:
        st.markdown("### 🛫 Departure Location")
        if SEARCHBOX_AVAILABLE:
            departure_selected = st_searchbox(
                search_function=st.session_state.location_service.search_destinations_autocomplete,
                placeholder="Search departure city...",
                label="From where are you departing?",
                key="departure_search"
            )
            if departure_selected:
                departure_dest = st.session_state.location_service.get_destination_by_display(departure_selected)
                if departure_dest:
                    st.session_state.selected_departure = departure_dest
                    st.success(f"🛫 **From:** {departure_dest.display}")
        else:
            # Fallback without searchbox
            departure_options = [dest.display for dest in st.session_state.location_service.all_locations[:50]]
            departure_selected = st.selectbox("Select departure city:", [""] + departure_options)
            if departure_selected:
                departure_dest = st.session_state.location_service.get_destination_by_display(departure_selected)
                if departure_dest:
                    st.session_state.selected_departure = departure_dest
    
    with trip_col2:
        st.markdown("### 🎯 Destination")
        if SEARCHBOX_AVAILABLE:
            destination_selected = st_searchbox(
                search_function=st.session_state.location_service.search_destinations_autocomplete,
                placeholder="Search destination...",
                label="Where are you going?",
                key="destination_search"
            )
            if destination_selected:
                dest = st.session_state.location_service.get_destination_by_display(destination_selected)
                if dest:
                    st.session_state.selected_destination = dest
                    st.success(f"🎯 **To:** {dest.display}")
                    
                    # Add weather information
                    weather_info = get_weather_info(dest)
                    st.info(f"🌡️ **Climate:** {weather_info['temp']} • {weather_info['climate']}")
        else:
            # Fallback without searchbox
            dest_options = [dest.display for dest in st.session_state.location_service.all_locations[:50]]
            destination_selected = st.selectbox("Select destination:", [""] + dest_options)
            if destination_selected:
                dest = st.session_state.location_service.get_destination_by_display(destination_selected)
                if dest:
                    st.session_state.selected_destination = dest
    
    with trip_col3:
        st.markdown("### 📅 Trip Duration")
        
        # Create a dictionary for better formatting - FIXED
        duration_options = {
            "1 day": 1,
            "2 days": 2, 
            "3 days": 3,
            "4 days": 4,
            "5 days": 5,
            "6 days": 6,
            "1 week (7 days)": 7,
            "8 days": 8,
            "9 days": 9,
            "10 days": 10,
            "11 days": 11,
            "12 days": 12,
            "13 days": 13,
            "2 weeks (14 days)": 14,
            "3 weeks (21 days)": 21,
            "1 month (30 days)": 30,
            "6 weeks (45 days)": 45,
            "2 months (60 days)": 60,
            "3 months (90 days)": 90
        }
        
        # Create selectbox with formatted options
        duration_display = st.selectbox(
            "How many days?", 
            options=list(duration_options.keys()),
            index=4  # Default to "5 days"
        )
        
        # Get the actual number value
        trip_duration = duration_options[duration_display]
        
        st.info(f"📅 **Duration:** {trip_duration} days")
        
        # Trip type indicator
        if trip_duration <= 3:
            st.success("🚀 **Quick Trip** - Minimal packing needed")
        elif trip_duration <= 7:
            st.info("📝 **Standard Trip** - Regular planning required")
        elif trip_duration <= 14:
            st.warning("🧳 **Extended Trip** - Comprehensive packing")
        else:
            st.error("🌍 **Long Journey** - Extensive preparation needed")
    
    # Trip Summary Card
    if st.session_state.selected_departure and st.session_state.selected_destination:
        st.markdown(f"""
        <div class="trip-info-card">
            <h3>🗺️ Your Trip Summary</h3>
            <p><strong>🛫 From:</strong> {st.session_state.selected_departure.display}</p>
            <p><strong>🎯 To:</strong> {st.session_state.selected_destination.display}</p>
            <p><strong>📅 Duration:</strong> {trip_duration} days</p>
            <p><strong>🌍 Distance:</strong> International Route</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 👶 Baby & Travel Information")
        baby_age = st.slider("Baby's Age (months)", 0, 24, 6)
        
        if baby_age <= 2:
            st.info("**👶 Newborn (0-2 months)**: Sleeps frequently, feeding schedule is key")
        elif baby_age <= 5:
            st.info("**🍼 Young Infant (3-5 months)**: Developing routines, still very portable")
        elif baby_age <= 11:
            st.info("**🤹 Mobile Baby (6-11 months)**: Crawling phase, needs entertainment and movement")
        elif baby_age <= 18:
            st.info("**🏃 Active Toddler (12-18 months)**: High energy, requires constant supervision")
        else:
            st.info("**🗣️ Communicative Toddler (19-24 months)**: Can express needs but still challenging")
        
        st.markdown("### ✈️ Flight Details") 
        flight_hours = st.slider("Total Flight Time (hours)", 0.5, 20.0, 3.0, step=0.5)
        
        layovers = st.selectbox("Number of Layovers", 
            options=[0, 1, 2, 3, 4],
            format_func=lambda x: f"{x} layover{'s' if x != 1 else ''}" if x > 0 else "Direct flight"
        )
        
        departure_time = st.selectbox("Primary Departure Time", [
            "Morning (7-11 AM)", "Afternoon (11 AM-5 PM)", "Evening (5-10 PM)",
            "Very Early (5-7 AM)", "Late Night (10 PM-12 AM)", "Red-eye (12-5 AM)"
        ])
        
        st.markdown("### 🛠️ Travel Configuration")
        has_partner = st.checkbox("Traveling with partner/helper", value=True)
        pumping_needed = st.checkbox("Breastfeeding/pumping required")
        special_needs = st.checkbox("Baby has special medical needs")
        first_international = st.checkbox("Baby's first international travel")
        
        parent_experience = st.selectbox("Your baby travel experience", [
            "First time flying with baby", "2-3 previous flights", 
            "Experienced traveler (4+ flights)", "Travel veteran (10+ flights)"
        ])
    
    with col2:
        st.markdown("### 🎯 Additional Search Options")
        st.markdown("*Use the search boxes above for better autocomplete experience*")
        
        # Show fallback search if needed
        if not SEARCHBOX_AVAILABLE:
            st.warning("Install streamlit-searchbox for enhanced autocomplete search!")
            
            search_query = st.text_input(
                "🔍 Search destinations (fallback)", 
                placeholder="Try: hyderabad, finland, dubai..."
            )
            
            if search_query:
                results = st.session_state.location_service.search_destinations(search_query, 8)
                st.markdown(f"**🌍 Found {len(results)} results:**")
                
                for i, dest in enumerate(results):
                    icon = "👨‍👩‍👧‍👦" if dest.name in st.session_state.location_service.top_family_destinations else "🏙️"
                    if st.button(f"{icon} {dest.display}", key=f"fallback_dest_{i}"):
                        st.session_state.selected_destination = dest
                        st.rerun()
        
        # Display current selections
        if st.session_state.selected_departure:
            st.success(f"🛫 **Departure:** {st.session_state.selected_departure.display}")
        
        if st.session_state.selected_destination:
            dest = st.session_state.selected_destination
            st.success(f"🎯 **Destination:** {dest.display}")
            st.info(f"📍 Type: {dest.type.title()} • Population: {dest.population:,}")
            
            # Add weather information
            weather_info = get_weather_info(dest)
            st.info(f"🌡️ **Climate:** {weather_info['temp']} • {weather_info['climate']} • {weather_info['season']}")
            
            if dest.name in st.session_state.location_service.top_family_destinations:
                st.success("👨‍👩‍👧‍👦 **Family-Friendly Destination** - Excellent for children!")
    
    st.markdown("---")
    
    # Enhanced Analysis button
    analysis_button_text = "🚀 Generate Complete Travel Analysis"
    if st.session_state.selected_departure and st.session_state.selected_destination:
        analysis_button_text += f" ({st.session_state.selected_departure.name} → {st.session_state.selected_destination.name})"
    
    if st.button(analysis_button_text, type="primary", use_container_width=True):
        if st.session_state.selected_destination:
            destination = st.session_state.selected_destination
            departure = st.session_state.selected_departure
            
            with st.spinner("🧠 AI analyzing your complete travel scenario..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                analyzer = TravelStressAnalyzer()
                stress_score, factors = analyzer.calculate_comprehensive_stress(
                    baby_age, flight_hours, layovers, departure_time,
                    has_partner, special_needs, pumping_needed, first_international,
                    parent_experience, destination, departure, trip_duration
                )
                
                progress_bar.empty()
                
                # Display results
                st.markdown("---")
                if departure:
                    st.markdown(f"# ✈️ Complete Analysis: {departure.name} → {destination.display}")
                else:
                    st.markdown(f"# ✈️ Complete Analysis: {destination.display}")
                
                # Enhanced trip summary
                st.markdown(f"""
                <div class="trip-info-card">
                    <h3>📋 Trip Overview</h3>
                    <p><strong>🛫 Route:</strong> {departure.display if departure else 'Not specified'} → {destination.display}</p>
                    <p><strong>📅 Duration:</strong> {trip_duration} days</p>
                    <p><strong>👶 Traveler:</strong> {baby_age}-month-old baby</p>
                    <p><strong>✈️ Flight:</strong> {flight_hours} hours, {layovers} layover{'s' if layovers != 1 else ''}</p>
                    <p><strong>🌡️ Climate:</strong> {get_weather_info(destination)['climate']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Stress level display
                if stress_score <= 3:
                    emoji, level, color = "😊", "Low Stress", "#28a745"
                    message = "Excellent! This trip should be very manageable for your family."
                elif stress_score <= 6:
                    emoji, level, color = "😅", "Medium Stress", "#ffc107"  
                    message = "Moderate challenge - good preparation will make this successful."
                else:
                    emoji, level, color = "😰", "High Stress", "#dc3545"
                    message = "Challenging trip - consider modifications or extensive preparation."
                
                st.markdown(f"""
                <div style="text-align: center; padding: 30px; border-radius: 20px; 
                           background: linear-gradient(135deg, {color}20 0%, {color}10 100%);
                           border: 2px solid {color}; margin: 20px 0;">
                    <h2>{emoji} Stress Level: {stress_score}/10</h2>
                    <h3>{level}</h3>
                    <p style="margin-top: 15px; font-size: 1.1em;">{message}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.progress(stress_score / 10)
                
                # DETAILED STRESS BREAKDOWN
                st.markdown("## 📊 Detailed Stress Factor Analysis")
                st.markdown("*Understanding your stress score calculation*")
                
                factor_explanations = {
                    'baby_age': f'👶 **Baby Age ({baby_age} months)**: {factors["baby_age"]}/3 points',
                    'flight_duration': f'✈️ **Flight Duration ({flight_hours}h)**: {factors["flight_duration"]}/3 points',
                    'layovers': f'🔄 **Layovers ({layovers})**: {factors["layovers"]}/2 points',
                    'timing': f'⏰ **Departure Time**: {factors["timing"]}/3 points',
                    'trip_length': f'📅 **Trip Duration ({trip_duration} days)**: {factors["trip_length"]}/3 points',
                    'support': f'👥 **Support System**: {factors["support"]}/2 points',
                    'medical': f'🏥 **Medical Needs**: {factors["medical"]}/2 points',
                    'logistics': f'📋 **Logistics**: {factors["logistics"]}/2 points',
                    'experience': f'🎯 **Your Experience**: {factors["experience"]}/2 points',
                    'destination': f'🌍 **Destination ({destination.name})**: {factors["destination"]}/1 points'
                }
                
                # Create 3 columns for factor display
                factor_cols = st.columns(3)
                for i, (factor, explanation) in enumerate(factor_explanations.items()):
                    with factor_cols[i % 3]:
                        score = factors[factor]
                        if score == 0:
                            st.success(explanation + " ✅")
                        elif score <= 1:
                            st.info(explanation + " ⚠️")
                        else:
                            st.warning(explanation + " 🚨")
                
                # Enhanced calculation explanation
                st.markdown("### 🧮 Calculation Breakdown")
                calculation_text = f"""
                **Your Stress Score: {stress_score}/10**
                
                - 👶 Baby Age ({baby_age} months): {factors['baby_age']} - *{baby_age}-month-olds are {'easy' if baby_age <= 6 else 'challenging'} to travel with*
                - ✈️ Flight ({flight_hours}h): {factors['flight_duration']} - *{'Short' if flight_hours <= 5 else 'Long'} flight duration*
                - 🔄 Layovers: {factors['layovers']} - *{'Direct flight - excellent!' if layovers == 0 else f'{layovers} layover(s)'}*
                - ⏰ Timing: {factors['timing']} - *{departure_time}*
                - 📅 Trip Length ({trip_duration} days): {factors['trip_length']} - *{'Short' if trip_duration <= 3 else 'Extended' if trip_duration > 14 else 'Standard'} trip duration*
                - 👥 Support: {factors['support']} - *{"With partner" if has_partner else "Solo parent"}*
                - 🏥 Medical: {factors['medical']} - *{"Special needs" if special_needs else "No special needs"}*
                - 📋 Logistics: {factors['logistics']} - *{"First international + pumping" if first_international and pumping_needed else "Standard logistics"}*
                - 🎯 Experience: {factors['experience']} - *{parent_experience}*
                - 🌍 Destination: {factors['destination']} - *{destination.name} - {'Easy' if factors['destination'] == 0 else 'Moderate'} destination*
                
                **Total: {sum(factors.values())} points = {stress_score}/10 stress level**
                """
                
                st.info(calculation_text)
                
                # Smart recommendations
                st.markdown("## 💡 Smart Recommendations")
                
                recommendations = []
                if stress_score >= 7:
                    recommendations.append("🚨 **High stress detected** - Consider choosing a closer destination or shorter trip")
                if baby_age < 3:
                    recommendations.append("👶 **Newborn advantage** - Use feeding times for ear pressure relief")
                elif baby_age >= 12:
                    recommendations.append("🎮 **Entertainment essential** - Download content, pack activities")
                if flight_hours > 10:
                    recommendations.append("✈️ **Long-haul prep** - Book bulkhead seats, request bassinet")
                if trip_duration > 14:
                    recommendations.append("📅 **Extended trip** - Research local baby supplies and pediatricians")
                if not has_partner:
                    recommendations.append("👥 **Solo parent** - Pre-book airport assistance")
                if pumping_needed:
                    recommendations.append("🍼 **Pumping logistics** - Research nursing rooms at airports")
                if first_international:
                    recommendations.append("📔 **Documentation** - Check passport validity (6+ months)")
                
                for i, rec in enumerate(recommendations[:6]):
                    st.success(f"**{i+1}.** {rec}")
                
                # ENHANCED PACKING CHECKLIST with trip duration
                st.markdown("## 🎒 Enhanced Smart Packing Checklist")
                st.markdown(f"*Customized for {baby_age}-month-old • {destination.display} • {trip_duration} days • Stress Level: {stress_score}/10*")
                
                # Get enhanced dynamic packing list
                packing_items = get_smart_packing_list(
                    baby_age, destination, stress_score, flight_hours, 
                    special_needs, pumping_needed, trip_duration
                )
                
                # Display in columns with checkboxes
                st.markdown("### ✅ Essential Items to Pack")
                cols = st.columns(3)
                for i, item in enumerate(packing_items):
                    with cols[i % 3]:
                        st.checkbox(item, key=f"pack_{i}")
                
                # Trip duration specific advice
                if trip_duration <= 3:
                    st.info("💡 **Short Trip Tip:** Pack light - you can buy essentials locally if needed!")
                elif trip_duration > 14:
                    st.warning("📋 **Extended Trip:** Consider shipping items ahead or researching local shopping options.")
                
                # Keep existing checklists (Pre-travel, Airport, Destination)
                st.markdown("### 📋 Pre-Travel Checklist")
                pre_travel_items = [
                    "📅 Book pediatrician visit 2 weeks before travel",
                    "💉 Check required vaccinations for destination",
                    "📄 Copy important documents (passport, insurance)",
                    "🏥 Research hospitals/clinics at destination",
                    "📱 Download offline maps and translation apps",
                    "💳 Notify bank of travel plans",
                    "🧳 Check airline baggage policies for baby items",
                    "✈️ Select seats (bulkhead for bassinet if needed)",
                    "🏨 Confirm hotel crib/baby equipment availability",
                    "🌐 Get international phone plan or SIM card"
                ]
                
                if trip_duration > 7:
                    pre_travel_items.extend([
                        "🏥 Research local pediatricians at destination",
                        "🛒 Identify baby supply stores locally",
                        "📋 Plan laundry schedule for extended stays"
                    ])
                
                cols = st.columns(2)
                for i, item in enumerate(pre_travel_items):
                    with cols[i % 2]:
                        st.checkbox(item, key=f"pre_travel_{i}")
                
                st.markdown("### ✈️ Airport & Flight Checklist")
                airport_items = [
                    "🍼 Bring extra bottles for security screening",
                    "🥛 Pack formula powder (easier than liquid)",
                    "🆔 Bring baby's birth certificate or passport",
                    "🎒 Pack essentials in easily accessible bag",
                    "🧴 Follow 3-1-1 rule for liquids (baby food exempt)",
                    "👶 Arrive early for security with baby",
                    "🚪 Use family/priority boarding when available",
                    "🍼 Feed baby during takeoff/landing for ear pressure",
                    "🧸 Keep comfort items easily accessible",
                    "📱 Have entertainment ready before flight"
                ]
                
                cols = st.columns(2)
                for i, item in enumerate(airport_items):
                    with cols[i % 2]:
                        st.checkbox(item, key=f"airport_{i}")
                
                st.markdown("### 🏨 Arrival & Destination Checklist")
                destination_items = [
                    "🏥 Locate nearest hospital/urgent care",
                    "🍼 Find local baby supply stores",
                    "🚰 Check water safety (use bottled if unsure)",
                    "🌡️ Monitor baby for jet lag symptoms",
                    "🧴 Buy local baby products if needed",
                    "📱 Test emergency contacts work locally",
                    "🚗 Install car seat properly if renting car",
                    "🏖️ Apply sunscreen 30 min before sun exposure",
                    "🥛 Maintain feeding schedule as much as possible",
                    "😴 Create familiar sleep environment"
                ]
                
                cols = st.columns(2)
                for i, item in enumerate(destination_items):
                    with cols[i % 2]:
                        st.checkbox(item, key=f"destination_{i}")
                
                # AMAZON PRODUCT RECOMMENDATIONS
                st.markdown("## 🛒 Personalized Amazon Product Recommendations")
                st.markdown("*Click any link to search Amazon for these products*")
                
                amazon_service = AmazonProductService()
                
                # Get product recommendations
                climate_products = amazon_service.get_temperature_based_products(destination)
                flight_products = amazon_service.get_flight_specific_products(flight_hours, baby_age)
                destination_products = amazon_service.get_destination_specific_products(destination)
                
                # Display products by category
                st.markdown("### 🌡️ Climate-Based Essentials")
                cols = st.columns(2)
                for i, product in enumerate(climate_products[:4]):
                    with cols[i % 2]:
                        st.markdown(f"""
                        <div class="product-card">
                            <h4>🏷️ {product.name}</h4>
                            <p><strong>⭐ {product.rating}</strong> • <strong>💰 {product.price_range}</strong></p>
                            <p>{product.description}</p>
                            <a href="{product.amazon_url}" target="_blank" class="product-link">
                                🛒 Search on Amazon
                            </a>
                        </div>
                        """, unsafe_allow_html=True)
                
                st.markdown("### ✈️ Flight Essentials")
                cols = st.columns(2)
                for i, product in enumerate(flight_products[:4]):
                    with cols[i % 2]:
                        st.markdown(f"""
                        <div class="product-card">
                            <h4>🏷️ {product.name}</h4>
                            <p><strong>⭐ {product.rating}</strong> • <strong>💰 {product.price_range}</strong></p>
                            <p>{product.description}</p>
                            <a href="{product.amazon_url}" target="_blank" class="product-link">
                                🛒 Search on Amazon
                            </a>
                        </div>
                        """, unsafe_allow_html=True)
                
                st.markdown("### 🎯 Destination-Specific Gear")
                for product in destination_products:
                    st.markdown(f"""
                    <div class="product-card">
                        <h4>🏷️ {product.name}</h4>
                        <p><strong>⭐ {product.rating}</strong> • <strong>💰 {product.price_range}</strong></p>
                        <p>{product.description}</p>
                        <a href="{product.amazon_url}" target="_blank" class="product-link">
                            🛒 Search on Amazon
                        </a>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Success message
                st.markdown("---")
                if stress_score <= 4:
                    st.success("🌟 **Great setup!** You're well-prepared for a successful trip!")
                    st.balloons()
                elif stress_score <= 7:
                    st.info("💪 **Good foundation!** With proper preparation, this will go well.")
                else:
                    st.warning("🤔 **Consider modifications** to reduce stress and improve experience.")
                
        else:
            st.error("🌍 Please select a destination first!")

# Export for main.py
__all__ = ['display_travel_stress_predictor']