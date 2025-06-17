# agents/travel_comfort_analyzer.py
"""
GoBabyGo: Smart Travel Companion for Parents
AI-Powered Travel Comfort Analyzer - Main Interface
Production Version 1.0
"""

import streamlit as st
import time
import pandas as pd
import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

# Import modular services
from .comfort_calculator import TravelComfortCalculator, WeatherComfortService
from .hotel_suggestions import BabyFriendlyHotelService, HotelSearchLink
from .location_service import GlobalLocationService
from .packing_assistant import get_smart_packing_list

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

def get_season_from_date(travel_date, destination_name):
    """Get season and weather info based on travel date and destination"""
    month = travel_date.month
    
    # Seasonal weather data for major destinations
    seasonal_weather = {
        'Dubai': {
            'winter': (12, 1, 2, "Perfect weather! 22-28°C, ideal for families"),
            'spring': (3, 4, 5, "Warm and pleasant, 25-35°C"),
            'summer': (6, 7, 8, "Very hot! 35-45°C, stay indoors midday"),
            'autumn': (9, 10, 11, "Hot but cooling down, 28-38°C")
        },
        'London': {
            'winter': (12, 1, 2, "Cold and wet, 2-8°C, pack warm clothes"),
            'spring': (3, 4, 5, "Mild and rainy, 8-15°C, perfect for sightseeing"),
            'summer': (6, 7, 8, "Warm and pleasant, 15-25°C, ideal weather"),
            'autumn': (9, 10, 11, "Cool and crisp, 8-16°C, beautiful season")
        },
        'Singapore': {
            'winter': (12, 1, 2, "Dry season, 24-30°C, best time to visit"),
            'spring': (3, 4, 5, "Hot and humid, 26-32°C"),
            'summer': (6, 7, 8, "Very hot and humid, 26-33°C, frequent rain"),
            'autumn': (9, 10, 11, "Monsoon season, 25-31°C, heavy rains")
        },
        'Tokyo': {
            'winter': (12, 1, 2, "Cold and dry, 0-10°C, pack warm layers"),
            'spring': (3, 4, 5, "Beautiful cherry blossoms, 10-20°C, perfect weather"),
            'summer': (6, 7, 8, "Hot and humid, 20-30°C, rainy season"),
            'autumn': (9, 10, 11, "Cool and comfortable, 10-22°C, stunning colors")
        },
        'Paris': {
            'winter': (12, 1, 2, "Cold and wet, 3-8°C, cozy indoor activities"),
            'spring': (3, 4, 5, "Mild and blooming, 8-16°C, lovely for walking"),
            'summer': (6, 7, 8, "Warm and sunny, 15-25°C, perfect for tourism"),
            'autumn': (9, 10, 11, "Cool and golden, 8-18°C, beautiful season")
        }
    }
    
    # Default seasonal info for other destinations
    default_seasons = {
        'winter': (12, 1, 2, "Winter season - check local weather"),
        'spring': (3, 4, 5, "Spring season - mild temperatures"),
        'summer': (6, 7, 8, "Summer season - warm weather"),
        'autumn': (9, 10, 11, "Autumn season - cooler temperatures")
    }
    
    # Get destination-specific or default weather
    weather_data = seasonal_weather.get(destination_name, default_seasons)
    
    # Determine season based on month
    for season, (m1, m2, m3, description) in weather_data.items():
        if month in [m1, m2, m3]:
            return season, description
    
    return "spring", "Moderate weather expected"

def calculate_trip_duration_from_dates(start_date, end_date):
    """Calculate trip duration in days from start and end dates"""
    duration = (end_date - start_date).days
    return max(1, duration)  # Minimum 1 day

    # Add this to the TOP of your display_travel_comfort_analyzer() function
# Right after the CSS styling section

def add_google_analytics():
    """Add Google Analytics 4 tracking to the app"""
    # Replace 'G-XXXXXXXXXX' with your actual Measurement ID
    GA_MEASUREMENT_ID = "G-FK6TVDFQ82"  # Get this from Google Analytics
    
    # Google Analytics 4 tracking code
    ga_code = f"""
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_MEASUREMENT_ID}');
    </script>
    """
    
    # Inject the tracking code
    st.markdown(ga_code, unsafe_allow_html=True)

# Call this function right after your CSS styling
def display_travel_comfort_analyzer():
    # Your existing CSS code here...
    st.markdown("""<style>...</style>""", unsafe_allow_html=True)
    
    # Add Google Analytics tracking
    add_google_analytics()
    
    # Rest of your app code...
    st.markdown('<h1 class="gobabygo-header">🍼 GoBabyGo: Smart Travel Companion</h1>', unsafe_allow_html=True)
    # ... rest of your code

def display_travel_comfort_analyzer():
    """GoBabyGo main interface for smart family travel planning"""
    
    # Enhanced CSS for all components with GoBabyGo branding - FIXED SEARCHBOX COLORS
    st.markdown("""
    <style>
        /* Main app styling */
        .stApp {
            background: linear-gradient(135deg, #f8f9fa 0%, #e3f2fd 100%);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* ULTIMATE STREAMLIT DROPDOWN FIX - TESTED SOLUTION */
        
        /* Target BaseWeb Select component (Streamlit's dropdown system) */
        div[data-baseweb="select"] {
            background-color: white !important;
        }
        
        div[data-baseweb="select"] > div {
            background-color: white !important;
            color: #2c3e50 !important;
            border: 1px solid #e0e0e0 !important;
        }
        
        /* Target the dropdown menu container */
        div[data-baseweb="select"] ul[role="listbox"],
        div[data-baseweb="popover"] ul[role="listbox"] {
            background-color: white !important;
            border: 1px solid #e0e0e0 !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
        }
        
        /* Target individual options */
        div[data-baseweb="select"] li[role="option"],
        div[data-baseweb="popover"] li[role="option"] {
            background-color: white !important;
            color: #2c3e50 !important;
            padding: 8px 12px !important;
        }
        
        /* Hover state for options */
        div[data-baseweb="select"] li[role="option"]:hover,
        div[data-baseweb="popover"] li[role="option"]:hover {
            background-color: #f5f5f5 !important;
            color: #2c3e50 !important;
        }
        
        /* Target Streamlit selectbox wrapper */
        .stSelectbox > div > div,
        [data-testid="stSelectbox"] > div > div {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Brute force all elements inside selectbox */
        .stSelectbox * {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        .stSelectbox div, 
        .stSelectbox span, 
        .stSelectbox input,
        .stSelectbox button {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Target by test ID */
        [data-testid="stSelectbox"] div[role="button"] {
            background-color: white !important;
            color: #2c3e50 !important;
            border: 1px solid #e0e0e0 !important;
        }
        
        /* Target BaseWeb popover system */
        div[data-baseweb="popover"] {
            background-color: white !important;
        }
        
        div[data-baseweb="popover"] > div {
            background-color: white !important;
        }
        
        /* High specificity override for nested elements */
        body .stSelectbox > div > div > div > div {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Target any dark background inline styles */
        div[style*="background-color: rgb(38, 39, 48)"],
        div[style*="background-color: rgb(38,39,48)"],
        div[style*="background-color: #262730"],
        div[style*="background: rgb(38, 39, 48)"],
        div[style*="background: #262730"] {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Force white background on any potentially dark element */
        .stApp div[style*="38"],
        .stApp div[style*="39"],
        .stApp div[style*="48"] {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* CSS Custom Properties for BaseWeb */
        :root {
            --select-background: white;
            --select-color: #2c3e50;
            --select-border: #e0e0e0;
        }
        
        /* Final fallback - override any remaining dark elements */
        .stSelectbox [style],
        [data-testid="stSelectbox"] [style] {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Fix searchbox specific styles */
        div[data-testid="stForm"] input,
        input[type="text"],
        input[type="search"] {
            background-color: white !important;
            color: #2c3e50 !important;
            border: 2px solid #e9ecef !important;
            border-radius: 8px !important;
            padding: 10px 15px !important;
        }
        
        /* Dark theme override for inputs */
        .st-emotion-cache-1inwz65,
        .st-emotion-cache-16idsys input {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Fix placeholder text */
        input::placeholder {
            color: #6c757d !important;
            opacity: 1 !important;
        }
        
        /* Headers and text */
        h1, h2, h3, h4, h5, h6, p, span, div, label {
            color: #2c3e50 !important;
        }
        
        /* GoBabyGo branded styling */
        .gobabygo-header {
            background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 50%, #45b7d1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5rem;
        }
        
        .gobabygo-tagline {
            text-align: center;
            color: #6c757d;
            font-size: 1.2em;
            margin-bottom: 20px;
            font-weight: 500;
        }
        
        /* Card styling */
        .trip-info-card {
            border: 2px solid #4ecdc4;
            border-radius: 12px;
            padding: 20px;
            margin: 15px 0;
            background: linear-gradient(135deg, #4ecdc420 0%, #4ecdc405 100%);
        }
        
        .comfort-score-card {
            border: 2px solid #ff6b6b;
            border-radius: 12px;
            padding: 20px;
            margin: 15px 0;
            background: linear-gradient(135deg, #ff6b6b20 0%, #ff6b6b05 100%);
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(135deg, #4ecdc4 0%, #45b7d1 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            padding: 12px 24px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3) !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(78, 205, 196, 0.4) !important;
        }
        
        button[kind="primary"] {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%) !important;
            font-size: 18px !important;
            padding: 15px 30px !important;
            box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3) !important;
        }
        
        /* Success, info, warning, error styling */
        .stAlert {
            border-radius: 10px !important;
            border: none !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
        }
        
        /* Progress bar */
        .stProgress > div > div > div {
            background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%) !important;
        }
        
        /* Checkbox styling */
        .stCheckbox > label {
            color: #2c3e50 !important;
            font-weight: 500 !important;
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            background: white !important;
            color: #2c3e50 !important;
            font-weight: 600 !important;
        }
        
        /* Product card styling */
        .product-card {
            border: 2px solid #e9ecef;
            border-radius: 12px;
            padding: 20px;
            background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            height: 100%;
            transition: transform 0.2s ease;
        }
        
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.15);
        }
        
        /* Hotel search card styling */
        .hotel-search-card {
            border: 2px solid #4ecdc4;
            border-radius: 12px;
            padding: 15px;
            margin: 10px 0;
            background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        /* Navigation preview cards */
        .nav-preview-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            border: 2px solid #e9ecef;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .nav-preview-card:hover {
            border-color: #4ecdc4;
            transform: translateY(-2px);
        }
        
        /* Date picker styling - COMPREHENSIVE FIX using dropdown method */
        .stDateInput > div > div {
            background-color: white !important;
            color: #2c3e50 !important;
            border: 2px solid #e9ecef !important;
            border-radius: 8px !important;
        }
        
        /* Apply same BaseWeb fixes as dropdowns for date picker */
        div[data-baseweb="calendar"] {
            background-color: white !important;
        }
        
        div[data-baseweb="calendar"] > div {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Target calendar popover like dropdown popover */
        div[data-baseweb="calendar"] div[data-baseweb="popover"],
        div[data-baseweb="calendar"] ul[role="listbox"] {
            background-color: white !important;
            border: 1px solid #e0e0e0 !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
        }
        
        /* Calendar days like dropdown options */
        div[data-baseweb="calendar"] [role="button"],
        div[data-baseweb="calendar"] li[role="option"] {
            background-color: white !important;
            color: #2c3e50 !important;
            padding: 8px 12px !important;
        }
        
        /* Calendar hover states like dropdown hover */
        div[data-baseweb="calendar"] [role="button"]:hover,
        div[data-baseweb="calendar"] li[role="option"]:hover {
            background-color: #f5f5f5 !important;
            color: #2c3e50 !important;
        }
        
        /* Force override dark backgrounds in calendar like dropdowns */
        div[data-baseweb="calendar"] div[style*="background-color: rgb(38, 39, 48)"],
        div[data-baseweb="calendar"] div[style*="background-color: rgb(38,39,48)"],
        div[data-baseweb="calendar"] div[style*="background-color: #262730"],
        div[data-baseweb="calendar"] div[style*="background: rgb(38, 39, 48)"],
        div[data-baseweb="calendar"] div[style*="background: #262730"] {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Calendar specific dark theme overrides */
        div[data-baseweb="calendar"] div[style*="38"],
        div[data-baseweb="calendar"] div[style*="39"],
        div[data-baseweb="calendar"] div[style*="48"] {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Brute force all calendar elements like dropdown elements */
        div[data-baseweb="calendar"] * {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        div[data-baseweb="calendar"] div, 
        div[data-baseweb="calendar"] span, 
        div[data-baseweb="calendar"] button,
        div[data-baseweb="calendar"] [role="button"] {
            background-color: white !important;
            color: #2c3e50 !important;
        }
        
        /* Selected date styling */
        div[data-baseweb="calendar"] [aria-selected="true"] {
            background-color: #4ecdc4 !important;
            color: white !important;
        }
        
        /* Final fallback for any remaining dark elements in calendar */
        div[data-baseweb="calendar"] [style],
        .stDateInput [style] {
            background-color: white !important;
            color: #2c3e50 !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # GoBabyGo Header with branding
    st.markdown('<h1 class="gobabygo-header">🍼 GoBabyGo: Smart Travel Companion</h1>', unsafe_allow_html=True)
    st.markdown('<p class="gobabygo-tagline">✈️ AI-powered travel planning made easy for parents</p>', unsafe_allow_html=True)
    
    # Initialize services
    if 'location_service' not in st.session_state:
        st.session_state.location_service = GlobalLocationService()
    
    if 'selected_destination' not in st.session_state:
        st.session_state.selected_destination = None
    
    if 'selected_departure' not in st.session_state:
        st.session_state.selected_departure = None
    
    # Feature highlights
    st.info("📊 **Smart Features:** Comfort analysis • Dynamic hotel search • Smart packing with Amazon links • 1000+ destinations worldwide")
    st.markdown("---")
    
    # Trip Overview Section
    st.markdown("## 🗺️ Trip Overview")
    trip_col1, trip_col2, trip_col3 = st.columns([1, 1, 1])

    with trip_col1:
        st.markdown("### 🛫 Departure Location")
        
        # Get departure options (only after location_service is initialized)
        if 'location_service' in st.session_state:
            departure_options = [dest.display for dest in st.session_state.location_service.all_locations[:100]]
            departure_selected = st.selectbox(
                "Select departure city:", 
                [""] + departure_options, 
                key="departure_select",
                help="Choose your departure city"
            )
            
            if departure_selected:
                departure_dest = st.session_state.location_service.get_destination_by_display(departure_selected)
                if departure_dest:
                    st.session_state.selected_departure = departure_dest
                    st.success(f"🛫 **From:** {departure_dest.display}")
        else:
            st.info("Loading locations...")

    with trip_col2:
        st.markdown("### 🎯 Destination")
        
        # Get destination options (only after location_service is initialized)
        if 'location_service' in st.session_state:
            dest_options = [dest.display for dest in st.session_state.location_service.all_locations[:100]]
            destination_selected = st.selectbox(
                "Select destination:", 
                [""] + dest_options, 
                key="dest_select",
                help="Choose your destination"
            )
            
            if destination_selected:
                dest = st.session_state.location_service.get_destination_by_display(destination_selected)
                if dest:
                    st.session_state.selected_destination = dest
                    st.success(f"🎯 **To:** {dest.display}")
                    
                    # Add weather information
                    weather_service = WeatherComfortService()
                    weather_info = weather_service.get_weather_comfort_info(dest)
                    st.info(f"🌡️ **Climate:** {weather_info['temp']} • {weather_info['climate']}")
        else:
            st.info("Loading destinations...")

    with trip_col3:
        st.markdown("### 📅 Travel Dates")
        
        # Date picker implementation - FIXED
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        
        departure_date = st.date_input(
            "Departure Date",
            value=tomorrow,
            min_value=today,
            max_value=today + datetime.timedelta(days=365),
            help="Select your departure date"
        )
        
        # Calculate return date default based on departure date
        default_return = departure_date + datetime.timedelta(days=5)  # 5-day trip default
        
        return_date = st.date_input(
            "Return Date", 
            value=default_return,
            min_value=departure_date + datetime.timedelta(days=1),  # At least 1 day after departure
            max_value=departure_date + datetime.timedelta(days=90),
            help="Select your return date"
        )
        
        # Calculate trip duration
        trip_duration = calculate_trip_duration_from_dates(departure_date, return_date)
        
        # Display trip info with seasonal weather
        if st.session_state.selected_destination:
            season, weather_desc = get_season_from_date(departure_date, st.session_state.selected_destination.name)
            
            st.info(f"📅 **Duration:** {trip_duration} days")
            st.info(f"🌤️ **Season:** {season.title()} travel")
            st.success(f"☀️ **Weather:** {weather_desc}")
        else:
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
        season, weather_desc = get_season_from_date(departure_date, st.session_state.selected_destination.name)
        st.markdown(f"""
        <div class="trip-info-card">
            <h3>🗺️ Your Trip Summary</h3>
            <p><strong>🛫 From:</strong> {st.session_state.selected_departure.display}</p>
            <p><strong>🎯 To:</strong> {st.session_state.selected_destination.display}</p>
            <p><strong>📅 Travel Dates:</strong> {departure_date.strftime('%B %d, %Y')} - {return_date.strftime('%B %d, %Y')}</p>
            <p><strong>⏱️ Duration:</strong> {trip_duration} days</p>
            <p><strong>🌤️ Season:</strong> {season.title()} weather expected</p>
            <p><strong>🌍 Distance:</strong> International Route</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Baby & Travel Information
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 👶 Baby & Travel Information")
        baby_age = st.slider("Baby's Age (months)", 0, 24, 6)
        
        # Age-based guidance
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
        st.markdown("### 🏨 Accommodation Preferences")
        
        hotel_preferences = {
            "budget": st.selectbox("Budget Range", [
                "Budget ($50-100/night)", "Mid-range ($100-200/night)", 
                "Luxury ($200-400/night)", "Ultra-luxury ($400+/night)"
            ]),
            "accommodation_type": st.multiselect("Preferred Accommodation Types", [
                "Hotels with baby amenities", "Family resorts", "Serviced apartments",
                "Vacation rentals", "All-inclusive resorts", "Boutique hotels"
            ], default=["Hotels with baby amenities"]),
            "essential_amenities": st.multiselect("Essential Baby Amenities", [
                "Crib/baby cot", "Kitchenette/kitchen", "Laundry facilities",
                "Baby monitor available", "High chair", "Baby bathtub",
                "Refrigerator", "Microwave", "Baby-proofed rooms"
            ], default=["Crib/baby cot", "Kitchenette/kitchen"]),
            "location_priorities": st.multiselect("Location Priorities", [
                "Near hospital/medical center", "Close to pharmacy", "Near parks/playgrounds",
                "Public transport access", "Shopping centers nearby", "Quiet neighborhood",
                "Beach/water access", "City center location"
            ], default=["Near hospital/medical center", "Close to pharmacy"])
        }
        
        # Display current selections
        if st.session_state.selected_departure:
            st.success(f"🛫 **Departure:** {st.session_state.selected_departure.display}")
        
        if st.session_state.selected_destination:
            dest = st.session_state.selected_destination
            st.success(f"🎯 **Destination:** {dest.display}")
            st.info(f"📍 Type: {dest.type.title()} • Population: {dest.population:,}")
            
            # Add weather information with seasonal context
            weather_service = WeatherComfortService()
            weather_info = weather_service.get_weather_comfort_info(dest)
            season, weather_desc = get_season_from_date(departure_date, dest.name)
            
            st.info(f"🌡️ **Climate:** {weather_info['temp']} • {weather_info['climate']} • {season.title()}")
            st.info(f"☀️ **Travel Weather:** {weather_desc}")
            
            if hasattr(st.session_state.location_service, 'top_family_destinations') and dest.name in st.session_state.location_service.top_family_destinations:
                st.success("👨‍👩‍👧‍👦 **Family-Friendly Destination** - Excellent for children!")
    
    st.markdown("---")
    
    # Enhanced Analysis button
    analysis_button_text = "🚀 Generate Complete Travel Comfort Analysis"
    if st.session_state.selected_departure and st.session_state.selected_destination:
        analysis_button_text += f" ({st.session_state.selected_departure.name} → {st.session_state.selected_destination.name})"
    
    if st.button(analysis_button_text, type="primary", use_container_width=True):
        if st.session_state.selected_destination:
            destination = st.session_state.selected_destination
            departure = st.session_state.selected_departure
            
            with st.spinner("🧠 AI analyzing your travel comfort factors..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                # Calculate comfort score using modular service
                calculator = TravelComfortCalculator()
                comfort_score, factors = calculator.calculate_travel_comfort(
                    baby_age, flight_hours, layovers, departure_time,
                    has_partner, special_needs, pumping_needed, first_international,
                    parent_experience, destination, departure, trip_duration
                )
                
                progress_bar.empty()
                
                # Display results with positive messaging
                st.markdown("---")
                if departure:
                    st.markdown(f"# ✈️ Travel Comfort Analysis: {departure.name} → {destination.display}")
                else:
                    st.markdown(f"# ✈️ Travel Comfort Analysis: {destination.display}")
                
                # Enhanced trip summary with dates and weather
                season, weather_desc = get_season_from_date(departure_date, destination.name)
                st.markdown(f"""
                <div class="trip-info-card">
                    <h3>📋 Trip Overview</h3>
                    <p><strong>🛫 Route:</strong> {departure.display if departure else 'Not specified'} → {destination.display}</p>
                    <p><strong>📅 Travel Dates:</strong> {departure_date.strftime('%B %d, %Y')} - {return_date.strftime('%B %d, %Y')}</p>
                    <p><strong>⏱️ Duration:</strong> {trip_duration} days</p>
                    <p><strong>👶 Traveler:</strong> {baby_age}-month-old baby</p>
                    <p><strong>✈️ Flight:</strong> {flight_hours} hours, {layovers} layover{'s' if layovers != 1 else ''}</p>
                    <p><strong>🌤️ Season:</strong> {season.title()} in {destination.name}</p>
                    <p><strong>☀️ Weather:</strong> {weather_desc}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Comfort level display
                if comfort_score >= 8:
                    emoji, level, color = "😊", "Excellent Comfort", "#28a745"
                    message = "Outstanding! This trip should be very comfortable and enjoyable for your family."
                elif comfort_score >= 6:
                    emoji, level, color = "😌", "Good Comfort", "#17a2b8"  
                    message = "Great setup! With good preparation, this will be a comfortable experience."
                elif comfort_score >= 4:
                    emoji, level, color = "😐", "Moderate Comfort", "#ffc107"
                    message = "Manageable trip - some preparation will help ensure comfort."
                else:
                    emoji, level, color = "😅", "Needs Planning", "#fd7e14"
                    message = "This trip needs extra planning - but it's definitely doable with the right preparation!"
                
                st.markdown(f"""
                <div class="comfort-score-card" style="text-align: center; padding: 30px; border-radius: 20px; 
                           background: linear-gradient(135deg, {color}20 0%, {color}10 100%);
                           border: 2px solid {color}; margin: 20px 0;">
                    <h2>{emoji} Comfort Level: {comfort_score}/10</h2>
                    <h3>{level}</h3>
                    <p style="margin-top: 15px; font-size: 1.1em;">{message}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.progress(comfort_score / 10)
                
                # Get insights using modular service
                insights = calculator.get_comfort_insights(comfort_score, factors)
                
                # DETAILED COMFORT FACTOR BREAKDOWN - FIXED DISPLAY (only showing proper weights, no extra rounding)
                st.markdown("## 📊 Detailed Comfort Factor Analysis")
                st.markdown("*Understanding your comfort score calculation*")
                
                factor_explanations = {
                    'baby_age_comfort': f'👶 **Baby Age ({baby_age} months)**: {factors["baby_age_comfort"]:.1f}/{calculator.factor_weights["baby_age_comfort"]:.0f} points',
                    'flight_comfort': f'✈️ **Flight ({flight_hours}h, {layovers} stops)**: {factors["flight_comfort"]:.1f}/{calculator.factor_weights["flight_comfort"]:.0f} points',
                    'timing_convenience': f'⏰ **Departure Time**: {factors["timing_convenience"]:.1f}/{calculator.factor_weights["timing_convenience"]:.0f} points',
                    'trip_duration_comfort': f'📅 **Trip Duration ({trip_duration} days)**: {factors["trip_duration_comfort"]:.1f}/{calculator.factor_weights["trip_duration_comfort"]:.0f} points',
                    'support_system': f'👥 **Support System**: {factors["support_system"]:.1f}/{calculator.factor_weights["support_system"]:.0f} points',
                    'medical_preparedness': f'🏥 **Medical Preparedness**: {factors["medical_preparedness"]:.1f}/{calculator.factor_weights["medical_preparedness"]:.0f} points',
                    'logistical_ease': f'📋 **Logistics Ease**: {factors["logistical_ease"]:.1f}/{calculator.factor_weights["logistical_ease"]:.0f} points',
                    'experience_advantage': f'🎯 **Experience Level**: {factors["experience_advantage"]:.1f}/{calculator.factor_weights["experience_advantage"]:.0f} points',
                    'destination_friendliness': f'🌍 **Destination ({destination.name})**: {factors["destination_friendliness"]:.1f}/{calculator.factor_weights["destination_friendliness"]:.0f} points'
                }
                
                # Create 3 columns for factor display
                factor_cols = st.columns(3)
                for i, (factor, explanation) in enumerate(factor_explanations.items()):
                    with factor_cols[i % 3]:
                        score = factors[factor]
                        weight = calculator.factor_weights[factor]
                        percentage = (score / weight) * 100
                        
                        if percentage >= 75:
                            st.success(explanation + " ✅")
                        elif percentage >= 50:
                            st.info(explanation + " ⚠️")
                        else:
                            st.warning(explanation + " 🔧")
                
                # Display insights
                st.markdown("### 💡 Comfort Insights")
                st.info(f"**Overall Assessment:** {insights['overall_assessment']}")
                
                if insights['top_strengths']:
                    st.success(f"**Top Strengths:** {', '.join(insights['top_strengths'])}")
                
                if insights['areas_for_improvement']:
                    st.warning(f"**Areas for Improvement:** {', '.join(insights['areas_for_improvement'])}")

                # Navigation Preview - Show users what's coming
                st.markdown("---")
                st.markdown("### 📍 What's Next:")
                nav_col1, nav_col2, nav_col3 = st.columns(3)
                with nav_col1:
                    st.info("🎒 **Smart Packing List**\nPersonalized items with Amazon links")
                with nav_col2:
                    st.info("🏨 **Hotel Search**\nBaby-friendly accommodations")
                with nav_col3:
                    st.info("📋 **Pre-Travel Checklist**\nDon't forget these essentials")
                st.markdown("---")

                # Smart Packing List with Weather-Based Recommendations
                st.markdown("## 🎒 Enhanced Smart Packing Checklist")
                st.markdown(f"*Customized for {baby_age}-month-old • {destination.display} • {trip_duration} days • {season.title()} weather • Comfort Level: {comfort_score}/10*")
                
                # Get weather info for smart packing
                weather_info = WeatherComfortService.get_weather_comfort_info(destination)
                season, weather_desc = get_season_from_date(departure_date, destination.name)
                
                st.info(f"💡 **Smart Suggestions:** Items customized for {weather_info['climate']} weather during {season} season in {destination.name}!")
                
                # Weather-based packing alert
                if 'Very hot' in weather_desc or 'hot' in weather_desc.lower():
                    st.warning(f"🌡️ **Hot Weather Alert:** {weather_desc} - Extra sun protection and cooling items recommended!")
                elif 'Cold' in weather_desc or 'cold' in weather_desc.lower():
                    st.warning(f"❄️ **Cold Weather Alert:** {weather_desc} - Warm layers and heating items essential!")
                elif 'rain' in weather_desc.lower():
                    st.info(f"🌧️ **Rainy Season:** {weather_desc} - Pack waterproof items!")
                
                # Create product recommendation cards
                st.markdown("### 🛍️ Personalized Amazon Product Recommendations")
                st.markdown("*Click any link to search Amazon for these products*")
                
                # Function to create product card
                def create_product_card(col, product_name, price_range, description, amazon_link, rating="4.5/5"):
                    with col:
                        st.markdown(f"""
                        <div class="product-card">
                            <h4 style="color: #ff6b6b; margin-bottom: 10px;">🛍️ {product_name}</h4>
                            <p style="color: #ffc107; font-size: 1.1em; margin: 5px 0;">⭐ {rating} • 💰 {price_range}</p>
                            <p style="color: #6c757d; margin: 15px 0; min-height: 40px;">{description}</p>
                            <a href="{amazon_link}" target="_blank" style="background: linear-gradient(135deg, #ff9500 0%, #ff6200 100%); 
                               color: white; padding: 12px 24px; border-radius: 8px; text-decoration: none; 
                               display: inline-block; font-weight: 600; width: 100%; text-align: center;">
                                🛒 Search on Amazon
                            </a>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Enhanced Climate & Season-Based Essentials Section
                st.markdown(f"#### 🌤️ {season.title()} Weather Essentials")
                
                # Season and climate-specific products
                if season == 'summer' or 'Hot' in weather_info['climate'] or 'Tropical' in weather_info['climate'] or 'hot' in weather_desc.lower():
                    cols = st.columns(3)
                    create_product_card(
                        cols[0], 
                        "Baby Sun Hat with Neck Protection",
                        "$15-25",
                        f"UPF 50+ protection, perfect for {season} travel",
                        f"https://www.amazon.com/s?k=baby+sun+hat+upf+50+{baby_age}+months",
                        "4.4/5"
                    )
                    create_product_card(
                        cols[1],
                        "Lightweight Baby Rompers (6-pack)",
                        "$25-35",
                        f"Breathable cotton for {destination.name} {season}",
                        f"https://www.amazon.com/s?k=baby+summer+rompers+{baby_age}+months+cotton",
                        "4.5/5"
                    )
                    create_product_card(
                        cols[2],
                        "Baby Cooling Towels & Sunscreen",
                        "$18-28",
                        f"Essential for hot {season} weather",
                        "https://www.amazon.com/s?k=baby+cooling+towel+sunscreen+spf+50+travel",
                        "4.6/5"
                    )
                    
                elif season == 'winter' or 'Cold' in weather_info['climate'] or 'cold' in weather_desc.lower():
                    cols = st.columns(3)
                    create_product_card(
                        cols[0],
                        "Baby Winter Travel Suit",
                        "$35-50",
                        f"Perfect for {destination.name} {season} weather",
                        f"https://www.amazon.com/s?k=baby+winter+travel+suit+{baby_age}+months",
                        "4.5/5"
                    )
                    create_product_card(
                        cols[1],
                        "Thermal Baby Layers Set",
                        "$20-30",
                        f"Essential layers for {season} travel",
                        f"https://www.amazon.com/s?k=baby+thermal+underwear+set+{baby_age}+months",
                        "4.4/5"
                    )
                    create_product_card(
                        cols[2],
                        "Baby Winter Accessories Bundle",
                        "$15-25",
                        f"Hat, mittens, scarf for cold {destination.name} weather",
                        "https://www.amazon.com/s?k=baby+winter+hat+mittens+set",
                        "4.6/5"
                    )
                    
                elif 'rain' in weather_desc.lower() or season == 'autumn':
                    cols = st.columns(3)
                    create_product_card(
                        cols[0],
                        "Baby Rain Gear Set",
                        "$25-35",
                        f"Waterproof protection for {season} in {destination.name}",
                        f"https://www.amazon.com/s?k=baby+rain+gear+waterproof+{baby_age}+months",
                        "4.4/5"
                    )
                    create_product_card(
                        cols[1],
                        "Baby Layering Clothes Set",
                        "$30-40",
                        f"Versatile layers for changing {season} weather",
                        f"https://www.amazon.com/s?k=baby+layering+clothes+{baby_age}+months",
                        "4.5/5"
                    )
                    create_product_card(
                        cols[2],
                        "Stroller Rain Cover",
                        "$15-25",
                        f"Keep baby dry during {destination.name} {season}",
                        "https://www.amazon.com/s?k=stroller+rain+cover+universal",
                        "4.3/5"
                    )
                else:  # Spring or moderate climate
                    cols = st.columns(3)
                    create_product_card(
                        cols[0],
                        "Baby Spring/Fall Outfit Set",
                        "$30-40",
                        f"Perfect for mild {season} weather in {destination.name}",
                        f"https://www.amazon.com/s?k=baby+spring+clothes+{baby_age}+months",
                        "4.5/5"
                    )
                    create_product_card(
                        cols[1],
                        "Light Baby Jacket",
                        "$25-35",
                        f"Ideal for {season} travel comfort",
                        f"https://www.amazon.com/s?k=baby+light+jacket+{baby_age}+months",
                        "4.4/5"
                    )
                    create_product_card(
                        cols[2],
                        "Baby All-Weather Blanket",
                        "$20-30",
                        f"Versatile comfort for {season} weather",
                        "https://www.amazon.com/s?k=baby+travel+blanket+all+weather",
                        "4.6/5"
                    )
                
                # Travel Essentials Section
                st.markdown("#### ✈️ Travel Essentials")
                cols = st.columns(3)
                
                create_product_card(
                    cols[0],
                    "Compact Travel Stroller",
                    "$150-250",
                    "One-hand fold, airplane carry-on size",
                    "https://www.amazon.com/s?k=compact+travel+stroller+airplane+lightweight",
                    "4.5/5"
                )
                create_product_card(
                    cols[1],
                    "Baby Carrier for Travel",
                    "$40-80",
                    f"Ergonomic design for {baby_age} months",
                    f"https://www.amazon.com/s?k=baby+carrier+travel+{baby_age}+months+ergonomic",
                    "4.4/5"
                )
                create_product_card(
                    cols[2],
                    "Diaper Bag Backpack",
                    "$35-60",
                    "Multiple compartments, changing pad included",
                    "https://www.amazon.com/s?k=diaper+bag+backpack+travel+organizer+changing+pad",
                    "4.6/5"
                )
                
                # Age-specific products
                st.markdown(f"#### 👶 Age-Specific Items ({baby_age} months)")
                cols = st.columns(3)
                
                if baby_age <= 6:
                    create_product_card(
                        cols[0],
                        "Portable Baby Bassinet",
                        "$60-100",
                        "Foldable design, mosquito net included",
                        "https://www.amazon.com/s?k=portable+baby+bassinet+travel+foldable",
                        "4.3/5"
                    )
                    create_product_card(
                        cols[1],
                        "Formula Dispenser Tower",
                        "$10-15",
                        "BPA-free, 4 compartments, spill-proof",
                        "https://www.amazon.com/s?k=formula+dispenser+travel+container",
                        "4.5/5"
                    )
                    create_product_card(
                        cols[2],
                        "Bottle Sterilizer Bags",
                        "$15-20",
                        "Microwave steam bags, 20 pack",
                        "https://www.amazon.com/s?k=bottle+sterilizer+bags+microwave+travel",
                        "4.4/5"
                    )
                elif baby_age <= 12:
                    create_product_card(
                        cols[0],
                        "Travel High Chair",
                        "$25-40",
                        "Portable booster, fits most chairs",
                        "https://www.amazon.com/s?k=portable+high+chair+booster+travel",
                        "4.4/5"
                    )
                    create_product_card(
                        cols[1],
                        "Baby Food Pouches Variety",
                        "$20-30",
                        "Organic options, TSA-friendly sizes",
                        "https://www.amazon.com/s?k=baby+food+pouches+travel+organic",
                        "4.5/5"
                    )
                    create_product_card(
                        cols[2],
                        "Sippy Cup Travel Set",
                        "$15-25",
                        "Spill-proof, easy clean, 3-pack",
                        "https://www.amazon.com/s?k=sippy+cup+travel+spill+proof+set",
                        "4.6/5"
                    )
                else:  # Toddlers
                    create_product_card(
                        cols[0],
                        "Travel Potty Seat",
                        "$20-30",
                        "Foldable, fits standard toilets",
                        "https://www.amazon.com/s?k=travel+potty+seat+toddler+foldable",
                        "4.4/5"
                    )
                    create_product_card(
                        cols[1],
                        "Toddler Travel Activities",
                        "$25-35",
                        "Quiet books, reusable stickers, crayons",
                        f"https://www.amazon.com/s?k=toddler+travel+activities+{baby_age}+months+airplane",
                        "4.5/5"
                    )
                    create_product_card(
                        cols[2],
                        "Snack Container Set",
                        "$15-25",
                        "Spill-proof, BPA-free, 4-pack",
                        "https://www.amazon.com/s?k=toddler+snack+containers+spill+proof+travel",
                        "4.6/5"
                    )
                
                # Essential Items Checklist
                st.markdown("### ✅ Essential Items to Pack")
                
                # Get basic packing list
                try:
                    packing_items = get_smart_packing_list(
                        baby_age, destination, comfort_score, flight_hours, 
                        special_needs, pumping_needed, trip_duration
                    )
                except:
                    # Fallback packing list
                    packing_items = [
                        "Diapers (extra supply)", "Baby wipes", "Baby clothes (layered)", 
                        "Feeding supplies", "Baby carrier", "Travel stroller",
                        "Baby first aid kit", "Baby sunscreen", "Pacifiers",
                        "Baby toys/entertainment", "Blanket", "Baby monitor",
                        "Changing pad", "Plastic bags", "Hand sanitizer",
                        "Baby food/formula", "Bottles", "Baby medications"
                    ]
                
                # Display in 3 columns with checkboxes
                cols = st.columns(3)
                for i, item in enumerate(packing_items[:18]):  # Limit to 18 most important items
                    with cols[i % 3]:
                        st.checkbox(item, key=f"pack_{i}")
                
                # Weather-specific packing reminders
                st.markdown("### 🌤️ Weather-Specific Reminders")
                if 'hot' in weather_desc.lower():
                    st.warning("☀️ **Hot Weather Essentials:** Extra sun protection, cooling towels, electrolyte drinks, lightweight clothing")
                elif 'cold' in weather_desc.lower():
                    st.warning("❄️ **Cold Weather Essentials:** Warm layers, hand warmers, thermal wear, waterproof boots")
                elif 'rain' in weather_desc.lower():
                    st.info("🌧️ **Rainy Weather Essentials:** Waterproof clothing, umbrella, dry bags, extra clothes")
                else:
                    st.info(f"🌤️ **{season.title()} Weather:** Pack versatile layers for changing conditions")
                
                # Pre-Travel Checklist
                with st.expander("📋 Pre-Travel Checklist", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.checkbox("🩺 Book pediatrician visit 2 weeks before travel", key="pre1")
                        st.checkbox("📄 Copy important documents (passport, insurance)", key="pre2")
                        st.checkbox("📱 Download offline maps and translation apps", key="pre3")
                        st.checkbox("🛄 Check airline baggage policies for baby items", key="pre4")
                        st.checkbox("🏨 Confirm hotel crib/baby equipment availability", key="pre5")
                    with col2:
                        st.checkbox("💉 Check required vaccinations for destination", key="pre6")
                        st.checkbox("🏥 Research hospitals/clinics at destination", key="pre7")
                        st.checkbox("💳 Notify bank of travel plans", key="pre8")
                        st.checkbox("✈️ Select seats (bulkhead for bassinet if needed)", key="pre9")
                        st.checkbox("📱 Get international phone plan or SIM card", key="pre10")
                        
                # Weather-specific pre-travel tasks
                with st.expander(f"🌤️ {season.title()} Weather Preparation", expanded=False):
                    if 'hot' in weather_desc.lower():
                        st.checkbox("☀️ Research air-conditioned venues and indoor activities", key="weather1")
                        st.checkbox("🏊 Pack swimming gear and water play items", key="weather2")
                        st.checkbox("🧴 Buy high-SPF sunscreen suitable for babies", key="weather3")
                    elif 'cold' in weather_desc.lower():
                        st.checkbox("❄️ Research heated indoor activities and venues", key="weather4")
                        st.checkbox("🧤 Pack extra warm accessories (hats, mittens, scarves)", key="weather5")
                        st.checkbox("🔥 Check hotel heating and warm amenities", key="weather6")
                    elif 'rain' in weather_desc.lower():
                        st.checkbox("🌧️ Research covered attractions and indoor activities", key="weather7")
                        st.checkbox("☔ Pack waterproof gear for stroller and baby", key="weather8")
                        st.checkbox("🏠 Plan indoor backup activities", key="weather9")
                
                # Airport & Flight Checklist
                with st.expander("✈️ Airport & Flight Checklist", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.checkbox("🍼 Bring extra bottles for security screening", key="air1")
                        st.checkbox("📄 Bring baby's birth certificate or passport", key="air2")
                        st.checkbox("💧 Follow 3-1-1 rule for liquids (baby food exempt)", key="air3")
                    with col2:
                        st.checkbox("🥛 Pack formula powder (easier than liquid)", key="air4")
                        st.checkbox("👜 Pack essentials in easily accessible bag", key="air5")
                        st.checkbox("⏰ Arrive early for security with baby", key="air6")
                
                # Trip duration advice
                if trip_duration <= 3:
                    st.info("💡 **Short Trip Tip:** Pack light - you can buy essentials locally if needed!")
                elif trip_duration > 14:
                    st.warning("📋 **Extended Trip:** Consider shipping items ahead or researching local shopping options.")
                
                st.markdown("---")
                
                # Baby-Friendly Hotel Suggestions
                st.markdown("## 🏨 Find Baby-Friendly Accommodations")
                st.markdown(f"*Customized searches for {destination.display} with your required amenities*")

                try:
                    hotel_service = BabyFriendlyHotelService()
                    search_links = hotel_service.get_baby_friendly_hotels(
                        destination, hotel_preferences, baby_age, trip_duration
                    )
                except:
                    # Fallback hotel search links
                    search_links = [
                        {
                            'platform': 'Booking.com',
                            'url': f"https://www.booking.com/searchresults.html?ss={destination.name}&checkin={departure_date.strftime('%Y-%m-%d')}&checkout={return_date.strftime('%Y-%m-%d')}&group_adults=2&group_children=1&age=0",
                            'description': 'Comprehensive hotel search with family filters and your exact dates',
                            'filters_applied': ['Family rooms', 'Crib available', 'Kitchen facilities', 'Your travel dates']
                        },
                        {
                            'platform': 'Hotels.com',
                            'url': f"https://www.hotels.com/search.do?destination={destination.name}&adults=2&children=1&checkin={departure_date.strftime('%Y-%m-%d')}&checkout={return_date.strftime('%Y-%m-%d')}",
                            'description': 'Family-friendly hotels and resorts with exact dates',
                            'filters_applied': ['Baby amenities', 'Family suites', 'Pool access', 'Your dates']
                        },
                        {
                            'platform': 'Airbnb',
                            'url': f"https://www.airbnb.com/s/{destination.name}/homes?adults=2&children=1&infants=1&checkin={departure_date.strftime('%Y-%m-%d')}&checkout={return_date.strftime('%Y-%m-%d')}",
                            'description': 'Vacation rentals with kitchen and family amenities',
                            'filters_applied': ['Kitchen', 'Family-friendly', 'Crib available', 'Your exact dates']
                        }
                    ]

                # Display search summary with dates
                st.markdown(f"""
                <div style="border: 2px solid #4ecdc4; border-radius: 12px; padding: 20px; 
                           background: linear-gradient(135deg, #4ecdc420 0%, #4ecdc405 100%); margin: 20px 0;">
                    <h3>🏨 Accommodation Search Summary for {destination.display}</h3>
                    <p><strong>📅 Your Travel Dates:</strong> {departure_date.strftime('%B %d, %Y')} - {return_date.strftime('%B %d, %Y')} ({trip_duration} nights)</p>
                    <p><strong>🌤️ Weather:</strong> {season.title()} season - {weather_desc}</p>
                    <p><strong>Your Requirements:</strong></p>
                    <ul>
                        <li>Budget: {hotel_preferences.get('budget', 'Not specified')}</li>
                        <li>Essential: {', '.join(hotel_preferences.get('essential_amenities', [])[:3])}</li>
                        <li>Priorities: {', '.join(hotel_preferences.get('location_priorities', [])[:2])}</li>
                    </ul>
                    <p><strong>Quick Tips:</strong></p>
                    <ul>
                        <li>🎯 All searches include your exact travel dates</li>
                        <li>🏠 Try Airbnb for longer stays (kitchen + laundry)</li>
                        <li>📞 Always confirm baby amenities before booking</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

                # Display search links with dates
                # Replace the hotel search links display section (around line 1220-1250) with this fixed version:

                # Display search links with dates
                st.markdown("### 🔍 Pre-Configured Search Links (With Your Dates)")
                st.info("Click any link below to search with baby-friendly filters and your exact travel dates already applied!")

                # Create columns for search links
                search_cols = st.columns(2)

                for i, search_link in enumerate(search_links):
                    with search_cols[i % 2]:
                        # Fix: Handle both dictionary and object formats
                        if hasattr(search_link, 'platform'):
                            # It's a HotelSearchLink object
                            platform = search_link.platform
                            description = search_link.description
                            url = search_link.url
                        else:
                            # It's a dictionary (fallback case)
                            platform = search_link.get('platform', 'Hotel Search')
                            description = search_link.get('description', '')
                            url = search_link.get('url', '#')
                        
                        st.markdown(f"""
                        <div class="hotel-search-card">
                            <h4 style="color: #2c3e50; margin: 0 0 10px 0;">🏨 {platform}</h4>
                            <p style="color: #6c757d; margin: 5px 0;">{description}</p>
                            <div style="margin: 10px 0;">
                        """, unsafe_allow_html=True)
                        
                        
                        st.markdown(f"""
                            </div>
                            <a href="{url}" target="_blank" style="background: linear-gradient(135deg, #4ecdc4 0%, #45b7d1 100%); 
                               color: white; padding: 10px 20px; border-radius: 8px; text-decoration: none; 
                               display: inline-block; font-weight: 600; margin-top: 10px; width: 100%; text-align: center;">
                                🔗 Search on {platform} →
                            </a>
                        </div>
                        """, unsafe_allow_html=True)

                # Dynamic destination-specific tips with weather context
                st.markdown("### 💡 Smart Accommodation Tips")
                
                # Weather-based accommodation advice
                if 'hot' in weather_desc.lower():
                    st.warning(f"🌡️ **Hot {season.title()} Weather:** Prioritize accommodations with excellent AC, pools, and shaded outdoor areas for {destination.name}")
                elif 'cold' in weather_desc.lower():
                    st.warning(f"❄️ **Cold {season.title()} Weather:** Look for hotels with good heating, indoor play areas, and warm lobbies in {destination.name}")
                elif 'rain' in weather_desc.lower():
                    st.info(f"🌧️ **Rainy {season.title()} Season:** Choose hotels with covered walkways, indoor activities, and room service in {destination.name}")
                
                # Get destination insights dynamically
                try:
                    destination_insights = st.session_state.location_service.get_destination_insights(destination)
                    
                    if destination_insights.get('family_rating') == 'Excellent':
                        st.success(f"🌟 **Great Choice!** {destination.name} has excellent family infrastructure with widespread baby-friendly facilities!")
                    elif destination_insights.get('infrastructure') == 'World-class':
                        st.info(f"🏨 **{destination.name}** has world-class infrastructure - most hotels will have baby amenities available.")
                    
                    # Language-based tips
                    if destination_insights.get('language_barrier') == 'None':
                        st.info("🗣️ **No Language Barrier** - Easy to communicate specific baby needs with hotel staff.")
                    elif destination_insights.get('language_barrier') == 'Low':
                        st.info("🗣️ **Low Language Barrier** - Most hotel staff speak English, making special requests easier.")
                    
                    # Medical facilities tip
                    if destination_insights.get('medical_facilities') in ['Excellent', 'World-class']:
                        st.success("🏥 **Excellent Medical Infrastructure** - Pediatric care readily available near most hotels.")
                
                except:
                    # Fallback destination tips
                    pass
                
                # Population-based suggestions
                if destination.population > 5000000:
                    st.info("🏙️ **Major City** - Wide variety of family-friendly accommodations available. Consider location carefully for convenience.")
                elif destination.population > 1000000:
                    st.info("🌆 **Large City** - Good selection of hotels with baby amenities. Downtown areas usually well-equipped.")
                elif destination.population > 100000:
                    st.info("🏘️ **Mid-size City** - Limited but quality options. Consider booking early for best family rooms.")
                else:
                    st.info("🏡 **Smaller Destination** - Consider vacation rentals or serviced apartments for more baby-friendly features.")
                
                # Trip duration based tips
                if trip_duration > 7:
                    st.info("🏠 **Extended Stay** - Consider serviced apartments or vacation rentals with full kitchens and laundry facilities.")
                elif trip_duration <= 3:
                    st.info("🏨 **Short Stay** - Hotels with good baby amenities and room service might be more convenient than apartments.")
                
                # Budget-based dynamic suggestions
                if "Budget" in hotel_preferences['budget']:
                    st.info("💰 **Budget Tip** - Check family hostels or budget chains that often have family rooms with cribs at lower prices.")
                elif "Luxury" in hotel_preferences['budget']:
                    st.info("✨ **Luxury Options** - High-end hotels often provide complimentary baby amenities, babysitting services, and kids' clubs.")
                
                # Season-specific accommodation tips
                if season == 'summer':
                    st.info("☀️ **Summer Travel Tip** - Book accommodations with pools and air conditioning well in advance!")
                elif season == 'winter':
                    st.info("❄️ **Winter Travel Tip** - Look for hotels with indoor heating, room service, and covered parking.")
                elif season == 'spring':
                    st.info("🌸 **Spring Travel Tip** - Perfect season for outdoor hotel amenities and garden views!")
                elif season == 'autumn':
                    st.info("🍂 **Autumn Travel Tip** - Great time for hotels with scenic views and moderate pricing.")
                
                # Note about direct booking
                st.info("""
                📌 **Pro Tip**: After finding options on search platforms, consider calling the hotel directly. 
                They may offer better rates, room upgrades, or confirm specific baby amenities that aren't listed online.
                """)
                
                # Success message with positive framing and weather context
                st.markdown("---")
                if comfort_score >= 7:
                    st.success(f"🌟 **Excellent planning!** You're set up for a wonderful {season} family trip to {destination.name}!")
                    st.balloons()
                elif comfort_score >= 5:
                    st.info(f"💪 **Good foundation!** A few tweaks will make this {season} trip even better.")
                else:
                    st.info(f"🎯 **Great start!** With our suggestions, this {season} trip will be much more comfortable.")
                
                # Final summary with dates and weather
                st.markdown("### 📅 Your Trip Summary")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Comfort Score", f"{comfort_score}/10", "")
                with col2:
                    st.metric("Trip Duration", f"{trip_duration} days", f"{departure_date.strftime('%b %d')} - {return_date.strftime('%b %d')}")
                with col3:
                    st.metric("Weather Season", f"{season.title()}", f"{destination.name}")
                
        else:
            st.error("🌍 Please select a destination first!")

# Export for main.py
__all__ = ['display_travel_comfort_analyzer']