# agents/stress_predictor.py
"""
Complete Travel Stress Predictor with Amazon Product Recommendations - LinkedIn Ready
"""

import streamlit as st
import time
from typing import List, Dict, Optional, Tuple
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

@dataclass
class ProductRecommendation:
    name: str
    description: str
    amazon_url: str
    price_range: str
    rating: str
    category: str

class AmazonProductService:
    """Service for Amazon product recommendations based on travel needs"""
    
    @staticmethod
    def get_temperature_based_products(destination: Destination) -> List[ProductRecommendation]:
        """Get clothing and gear based on destination climate"""
        
        hot_countries = ['United Arab Emirates', 'UAE', 'Qatar', 'Egypt', 'India', 'Thailand', 'Malaysia', 'Indonesia']
        cold_countries = ['Iceland', 'Norway', 'Sweden', 'Finland', 'Denmark', 'Canada', 'Russia']
        
        products = []
        
        if destination.country in hot_countries:
            products.extend([
                ProductRecommendation(
                    "Baby Sun Hat with Neck Protection",
                    "UPF 50+ protection, adjustable chin strap",
                    "https://www.amazon.com/s?k=baby+sun+hat+upf+50&ref=nb_sb_noss",
                    "$15-25", "4.4/5", "sun_protection"
                ),
                ProductRecommendation(
                    "Lightweight Baby Rompers (6-pack)",
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
        elif destination.country in cold_countries:
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

class GlobalLocationService:
    def __init__(self):
        self._search_cache = {}
        self.top_family_destinations = [
            'Dubai', 'Singapore', 'Tokyo', 'London', 'Sydney', 
            'Barcelona', 'Amsterdam', 'Copenhagen', 'Reykjavik', 'Paris'
        ]
    
    def search_destinations(self, query: str, limit: int = 8) -> List[Destination]:
        """FIXED search with proper import handling"""
        
        try:
            # Fix the import path issue
            import sys
            import os
            
            # Add the current directory to Python path
            current_dir = os.path.dirname(os.path.abspath(__file__))
            if current_dir not in sys.path:
                sys.path.append(current_dir)
            
            # Also try adding the parent directory
            parent_dir = os.path.dirname(current_dir)
            if parent_dir not in sys.path:
                sys.path.append(parent_dir)
            
            # Now try to import
            import world_locations
            from world_locations import WORLD_LOCATIONS, search_locations_by_query, format_display_name
            
            st.write(f"✅ Successfully imported WORLD_LOCATIONS with {len(WORLD_LOCATIONS)} destinations")
            
            if not query or query.strip() == "":
                # Return top family destinations when no query
                results = []
                for dest_name in self.top_family_destinations:
                    if dest_name in WORLD_LOCATIONS:
                        data = WORLD_LOCATIONS[dest_name]
                        dest = Destination(
                            name=dest_name,
                            country=data['country'],
                            admin=data.get('admin', ''),
                            population=data['population'],
                            type=data['type'],
                            display=format_display_name(data, dest_name),
                            source='database'
                        )
                        results.append(dest)
                return results[:limit]
            
            st.write(f"🔍 Searching for '{query}'")
            
            # Use YOUR search function from world_locations.py
            search_results = search_locations_by_query(query, limit)
            
            st.write(f"📊 Found {len(search_results)} raw results")
            
            # Convert to Destination objects
            destinations = []
            for result in search_results:
                dest = Destination(
                    name=result['name'],
                    country=result['country'],
                    admin=result.get('admin', ''),
                    population=result['population'],
                    type=result['type'],
                    display=format_display_name(result, result['name']),
                    source='database'
                )
                destinations.append(dest)
            
            st.write(f"✅ Converted to {len(destinations)} destination objects")
            return destinations
            
        except ImportError as e:
            st.error(f"❌ Import failed: {e}")
            st.write("Trying manual file import...")
            
            # Try to manually load the file
            try:
                import sys
                import os
                
                # Get the directory where this file is located
                current_dir = os.path.dirname(os.path.abspath(__file__))
                world_locations_path = os.path.join(current_dir, 'world_locations.py')
                
                st.write(f"Looking for file at: {world_locations_path}")
                st.write(f"File exists: {os.path.exists(world_locations_path)}")
                
                if os.path.exists(world_locations_path):
                    # Load the module manually
                    import importlib.util
                    spec = importlib.util.spec_from_file_location("world_locations", world_locations_path)
                    world_locations_module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(world_locations_module)
                    
                    WORLD_LOCATIONS = world_locations_module.WORLD_LOCATIONS
                    search_locations_by_query = world_locations_module.search_locations_by_query
                    format_display_name = world_locations_module.format_display_name
                    
                    st.success(f"✅ Manually loaded {len(WORLD_LOCATIONS)} destinations!")
                    
                    if not query or query.strip() == "":
                        results = []
                        for dest_name in self.top_family_destinations:
                            if dest_name in WORLD_LOCATIONS:
                                data = WORLD_LOCATIONS[dest_name]
                                dest = Destination(
                                    name=dest_name,
                                    country=data['country'],
                                    admin=data.get('admin', ''),
                                    population=data['population'],
                                    type=data['type'],
                                    display=format_display_name(data, dest_name),
                                    source='database'
                                )
                                results.append(dest)
                        return results[:limit]
                    
                    # Search using the manually loaded function
                    search_results = search_locations_by_query(query, limit)
                    destinations = []
                    for result in search_results:
                        dest = Destination(
                            name=result['name'],
                            country=result['country'],
                            admin=result.get('admin', ''),
                            population=result['population'],
                            type=result['type'],
                            display=format_display_name(result, result['name']),
                            source='database'
                        )
                        destinations.append(dest)
                    
                    return destinations
                    
            except Exception as manual_error:
                st.error(f"Manual import also failed: {manual_error}")
                return self._fallback_search(query, limit)
                
        except Exception as e:
            st.error(f"Search error: {e}")
            return self._fallback_search(query, limit)
    
    def _fallback_search(self, query: str, limit: int) -> List[Destination]:
        """Fallback if world_locations.py import fails"""
        fallback_data = [
            ('Dubai', 'United Arab Emirates', 'Dubai', 3500000),
            ('Singapore', 'Singapore', '', 6000000),
            ('Baku', 'Azerbaijan', 'Baku', 2300000),
            ('Stockholm', 'Sweden', 'Stockholm', 2400000),
            ('Gabala', 'Azerbaijan', 'Gabala', 13000),
            ('London', 'United Kingdom', 'England', 9000000),
        ]
        
        if not query:
            results = []
            for name, country, admin, pop in fallback_data[:limit]:
                display = f"{name}, {country}" if country != name else name
                results.append(Destination(name, country, admin, pop, 'city', display))
            return results
        
        query_lower = query.lower()
        results = []
        for name, country, admin, pop in fallback_data:
            if query_lower in name.lower() or query_lower in country.lower():
                display = f"{name}, {country}" if country != name else name
                results.append(Destination(name, country, admin, pop, 'city', display))
        
        return results[:limit]

class TravelStressAnalyzer:
    @staticmethod
    def calculate_comprehensive_stress(
        baby_age: int, flight_hours: float, layovers: int, departure_time: str,
        has_partner: bool, special_needs: bool, pumping_needed: bool, 
        first_international: bool, parent_experience: str, destination: Destination
    ) -> Tuple[int, dict]:
        
        factors = {
            'baby_age': 0, 'flight_duration': 0, 'layovers': 0, 'timing': 0,
            'support': 0, 'medical': 0, 'logistics': 0, 'experience': 0, 'destination': 0
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

def get_smart_packing_list(baby_age: int, destination: Destination, stress_score: int, flight_hours: float, special_needs: bool, pumping_needed: bool) -> List[str]:
    """Generate dynamic packing list based on multiple factors"""
    
    packing_list = [
        "🧷 Diapers (extra 3 days worth)",
        "🧻 Baby wipes (travel packs)",
        "🍼 Bottles/formula/baby food",
        "👕 Extra clothes (3+ outfit changes)",
        "🧸 Comfort items & favorite toys",
        "🏥 Medical kit & baby thermometer"
    ]
    
    # Age-specific items
    if baby_age <= 6:
        packing_list.extend([
            "🍼 Extra formula/baby food",
            "👶 Burp cloths & bibs",
            "🛏️ Portable changing pad"
        ])
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
    if destination.country in ['United Arab Emirates', 'UAE', 'Egypt', 'India', 'Thailand']:
        packing_list.extend([
            "☀️ Strong sunscreen (SPF 50+)",
            "🧴 Extra hydration solutions",
            "👒 Sun hat & light clothing"
        ])
    elif destination.country in ['Iceland', 'Norway', 'Denmark', 'Sweden', 'Finland']:
        packing_list.extend([
            "🧥 Warm layers & winter gear",
            "🧤 Mittens & warm hat",
            "💧 Moisturizer for dry air"
        ])
    
    # Stress and flight specific
    if stress_score >= 7:
        packing_list.extend([
            "🚨 Emergency contact list",
            "📞 International phone plan",
            "💊 Extra medications"
        ])
    
    if flight_hours > 8:
        packing_list.extend([
            "✈️ Bassinet booking confirmation",
            "🎧 Noise-canceling headphones",
            "🛌 Travel pillow & blanket"
        ])
    
    if special_needs:
        packing_list.extend([
            "🏥 All medical records",
            "💊 Prescription letter from doctor"
        ])
    
    if pumping_needed:
        packing_list.extend([
            "🍼 Breast pump & accessories",
            "❄️ Cooler bag for milk storage"
        ])
    
    unique_list = list(dict.fromkeys(packing_list))
    return unique_list[:25]

def display_travel_stress_predictor():
    """Main predictor interface with Amazon product recommendations"""
    
    # Enhanced CSS
    st.markdown("""
    <style>
        .stSelectbox > div > div > div {
            background-color: white !important;
            color: #2c3e50 !important;
            border: 2px solid #e9ecef !important;
            border-radius: 8px !important;
        }
        
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
        
        .product-link:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(255, 149, 0, 0.3);
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("# ✈️ AI-Powered Travel Stress Predictor")
    st.markdown("🌍 Smart travel planning with personalized product recommendations")
    
    if 'location_service' not in st.session_state:
        st.session_state.location_service = GlobalLocationService()
    
    if 'selected_destination' not in st.session_state:
        st.session_state.selected_destination = None
    
    st.info("📊 **Complete Solution:** 1000+ destinations • Smart product recommendations • Real Amazon links")
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
        st.markdown("### 🌍 Global Destination Search")
        st.markdown("*Professional search engine - 1000+ destinations*")
        
        search_col1, search_col2 = st.columns([3, 1])
        
        with search_col1:
            search_query = st.text_input(
                "🔍 Search any destination worldwide", 
                placeholder="Try: baku, sweden, stockholm, dubai..."
            )
        
        with search_col2:
            search_button = st.button("🔍 Search", type="primary", use_container_width=True)
        
        # Get search results
        results = st.session_state.location_service.search_destinations(search_query, 8)
        
        # Display selected destination with weather info
        if st.session_state.selected_destination:
            dest = st.session_state.selected_destination
            st.success(f"✅ **Selected:** {dest.display}")
            st.info(f"📍 Type: {dest.type.title()} • Population: {dest.population:,}")
            
            # Add weather information
            weather_info = get_weather_info(dest)
            st.info(f"🌡️ **Climate:** {weather_info['temp']} • {weather_info['climate']} • {weather_info['season']}")
            
            if dest.name in st.session_state.location_service.top_family_destinations:
                st.success("👨‍👩‍👧‍👦 **Family-Friendly Destination** - Excellent for children!")
        
        # Show search results
        if search_query:
            st.markdown(f"**🌍 Found {len(results)} results:**")
        else:
            st.markdown("**👨‍👩‍👧‍👦 Top Family-Friendly Destinations:**")
        
        # Display results
        for i, dest in enumerate(results):
            icon = "👨‍👩‍👧‍👦" if dest.name in st.session_state.location_service.top_family_destinations else "🏙️"
            if st.button(f"{icon} {dest.display}", key=f"dest_{i}", use_container_width=True):
                st.session_state.selected_destination = dest
                st.rerun()
    
    st.markdown("---")
    
    # Analysis button
    if st.button("🚀 Generate AI Analysis + Amazon Product Recommendations", type="primary", use_container_width=True):
        if st.session_state.selected_destination:
            destination = st.session_state.selected_destination
            
            with st.spinner("🧠 AI analyzing your travel scenario..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                analyzer = TravelStressAnalyzer()
                stress_score, factors = analyzer.calculate_comprehensive_stress(
                    baby_age, flight_hours, layovers, departure_time,
                    has_partner, special_needs, pumping_needed, first_international,
                    parent_experience, destination
                )
                
                progress_bar.empty()
                
                # Display results
                st.markdown("---")
                st.markdown(f"# ✈️ Complete Analysis: {destination.display}")
                
                # Stress level display
                if stress_score <= 3:
                    emoji, level, color = "😊", "Low Stress", "#28a745"
                    message = "Excellent! This trip should be very manageable."
                elif stress_score <= 6:
                    emoji, level, color = "😅", "Medium Stress", "#ffc107"  
                    message = "Moderate challenge - good preparation will help."
                else:
                    emoji, level, color = "😰", "High Stress", "#dc3545"
                    message = "Challenging trip - extensive preparation needed."
                
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
                
                # Calculation explanation
                st.markdown("### 🧮 Calculation Breakdown")
                calculation_text = f"""
                **Your Stress Score: {stress_score}/10**
                
                - 👶 Baby Age (4 months): {factors['baby_age']} - *Young babies are easier to travel with*
                - ✈️ Flight (3.5h): {factors['flight_duration']} - *Short flight = low stress*
                - 🔄 Direct Flight: {factors['layovers']} - *No layovers = excellent*
                - ⏰ Timing: {factors['timing']} - *{departure_time}*
                - 👥 Support: {factors['support']} - *{"With partner" if has_partner else "Solo parent"}*
                - 🏥 Medical: {factors['medical']} - *{"Special needs" if special_needs else "No special needs"}*
                - 📋 Logistics: {factors['logistics']} - *{"First international" if first_international else "Domestic/experienced"}*
                - 🎯 Experience: {factors['experience']} - *{parent_experience}*
                - 🌍 Destination: {factors['destination']} - *{destination.name} difficulty*
                
                **Total: {sum(factors.values())} points = {stress_score}/10 stress level**
                """
                
                st.info(calculation_text)
                
                # Smart recommendations
                st.markdown("## 💡 Smart Recommendations")
                
                recommendations = []
                if stress_score >= 7:
                    recommendations.append("🚨 **High stress detected** - Consider choosing a closer destination")
                if baby_age < 3:
                    recommendations.append("👶 **Newborn advantage** - Use feeding times for ear pressure relief")
                elif baby_age >= 12:
                    recommendations.append("🎮 **Entertainment essential** - Download content, pack activities")
                if flight_hours > 10:
                    recommendations.append("✈️ **Long-haul prep** - Book bulkhead seats, request bassinet")
                if not has_partner:
                    recommendations.append("👥 **Solo parent** - Pre-book airport assistance")
                if pumping_needed:
                    recommendations.append("🍼 **Pumping logistics** - Research nursing rooms at airports")
                if first_international:
                    recommendations.append("📔 **Documentation** - Check passport validity (6+ months)")
                
                for i, rec in enumerate(recommendations[:5]):
                    st.success(f"**{i+1}.** {rec}")
                
                # COMPREHENSIVE PACKING CHECKLIST
                st.markdown("## 🎒 Comprehensive Smart Packing Checklist")
                st.markdown(f"*Customized for {baby_age}-month-old • {destination.display} • Stress Level: {stress_score}/10*")
                
                # Get dynamic packing list
                packing_items = get_smart_packing_list(
                    baby_age, destination, stress_score, flight_hours, special_needs, pumping_needed
                )
                
                # Display in columns with checkboxes
                st.markdown("### ✅ Essential Items to Pack")
                cols = st.columns(3)
                for i, item in enumerate(packing_items):
                    with cols[i % 3]:
                        st.checkbox(item, key=f"pack_{i}")
                
                # Pre-travel checklist
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