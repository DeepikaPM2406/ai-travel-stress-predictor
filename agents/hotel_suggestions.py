# agents/hotel_suggestions.py
"""
Baby-Friendly Hotel Suggestions Service
Provides dynamic hotel search with pre-configured filters for baby amenities
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
import urllib.parse

@dataclass
class BabyFriendlyHotel:
    name: str
    location: str
    rating: str
    price_range: str
    baby_amenities: List[str]
    family_features: str
    description: str
    booking_url: str
    booking_platform: str
    distance_to_hospital: str
    distance_to_pharmacy: str
    nearby_parks: List[str]

@dataclass
class HotelSearchLink:
    platform: str
    url: str
    description: str
    filters_applied: List[str]

class BabyFriendlyHotelService:
    """Service for finding baby-friendly accommodation options"""
    
    def __init__(self):
        self.booking_platforms = {
            'booking.com': {
                'base_url': 'https://www.booking.com/searchresults.html',
                'family_facilities': [
                    ('family_facilities', '8'),  # Family rooms
                    ('family_facilities', '28'), # Children's playground
                    ('hotelfacility', '7'),      # Non-smoking rooms
                    ('hotelfacility', '2'),      # Restaurant
                    ('hotelfacility', '96'),     # Family rooms
                    ('roomfacility', '75'),      # Baby safety gates
                    ('roomfacility', '175'),     # Children's high chair
                ]
            },
            'hotels.com': {
                'base_url': 'https://www.hotels.com/search.do',
                'params': {
                    'amenities': 'KITCHEN,CRIB'
                }
            },
            'airbnb': {
                'base_url': 'https://www.airbnb.com/s/',
                'params': {
                    'refinement_paths[]': '/homes',
                    'amenities[]': '45',  # Crib
                    'amenities[]': '8',   # Kitchen
                    'amenities[]': '33',  # Washer
                }
            },
            'expedia': {
                'base_url': 'https://www.expedia.com/Hotel-Search',
                'params': {
                    'amenities': 'CRIBS_ALLOWED,KITCHEN'
                }
            }
        }
    
    def get_baby_friendly_hotels(self, destination, preferences: Dict, baby_age: int, trip_duration: int) -> List[HotelSearchLink]:
        """Generate dynamic search links for baby-friendly hotels"""
        
        search_links = []
        
        # Get destination info
        dest_name = destination.name
        dest_country = destination.country
        
        # Parse preferences
        budget = preferences.get('budget', 'Mid-range ($100-200/night)')
        essential_amenities = preferences.get('essential_amenities', [])
        accommodation_types = preferences.get('accommodation_type', [])
        location_priorities = preferences.get('location_priorities', [])
        
        # Generate Booking.com search link
        booking_url = self._generate_booking_search(
            dest_name, dest_country, essential_amenities, 
            budget, trip_duration, baby_age
        )
        search_links.append(HotelSearchLink(
            platform="Booking.com",
            url=booking_url,
            description="Comprehensive filters for family facilities, cribs, and kitchenettes",
            filters_applied=self._get_applied_filters(essential_amenities, 'booking')
        ))
        
        # Generate Airbnb search link
        if "Vacation rentals" in accommodation_types or "Serviced apartments" in accommodation_types:
            airbnb_url = self._generate_airbnb_search(
                dest_name, essential_amenities, trip_duration
            )
            search_links.append(HotelSearchLink(
                platform="Airbnb",
                url=airbnb_url,
                description="Entire homes and apartments with baby amenities",
                filters_applied=self._get_applied_filters(essential_amenities, 'airbnb')
            ))
        
        # Generate Hotels.com search link
        hotels_url = self._generate_hotels_search(dest_name, essential_amenities)
        search_links.append(HotelSearchLink(
            platform="Hotels.com",
            url=hotels_url,
            description="Hotels with cribs and kitchen facilities",
            filters_applied=self._get_applied_filters(essential_amenities, 'hotels')
        ))
        
        # Generate Expedia search link
        expedia_url = self._generate_expedia_search(dest_name, essential_amenities)
        search_links.append(HotelSearchLink(
            platform="Expedia",
            url=expedia_url,
            description="Family-friendly hotels with baby amenities",
            filters_applied=self._get_applied_filters(essential_amenities, 'expedia')
        ))
        
        # Add specialized searches based on location priorities
        if "Near hospital/medical center" in location_priorities:
            hospital_search = self._generate_hospital_proximity_search(dest_name)
            search_links.append(hospital_search)
        
        if "Beach/water access" in location_priorities:
            beach_search = self._generate_beach_resort_search(dest_name, essential_amenities)
            search_links.append(beach_search)
        
        return search_links
    
    def _generate_booking_search(self, dest_name: str, dest_country: str, 
                                amenities: List[str], budget: str, 
                                trip_duration: int, baby_age: int) -> str:
        """Generate Booking.com search URL with baby-friendly filters"""
        
        params = {
            'ss': f"{dest_name}, {dest_country}",
            'group_adults': '2',
            'group_children': '1',
            'age': str(baby_age // 12) if baby_age >= 12 else '0',
            'no_rooms': '1',
            'sb_travel_purpose': 'leisure',
        }
        
        # Add price filter based on budget
        price_filters = {
            "Budget ($50-100/night)": ('price_min', '50', 'price_max', '100'),
            "Mid-range ($100-200/night)": ('price_min', '100', 'price_max', '200'),
            "Luxury ($200-400/night)": ('price_min', '200', 'price_max', '400'),
            "Ultra-luxury ($400+/night)": ('price_min', '400', '', '')
        }
        
        if budget in price_filters:
            min_key, min_val, max_key, max_val = price_filters[budget]
            params[min_key] = min_val
            if max_key and max_val:
                params[max_key] = max_val
        
        # Build URL with family facilities
        base_url = self.booking_platforms['booking.com']['base_url']
        query_parts = [f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items()]
        
        # Add family facilities filters
        family_filters = []
        if "Crib/baby cot" in amenities:
            family_filters.append("family_facilities=96")  # Family rooms
            family_filters.append("roomfacility=175")      # High chair
        if "Kitchenette/kitchen" in amenities:
            family_filters.append("roomfacility=22")       # Kitchenette
        if "Laundry facilities" in amenities:
            family_filters.append("hotelfacility=17")      # Laundry
        
        # Add filters for baby-friendly features
        family_filters.extend([
            "review_score_group=review_score_over_8",      # High-rated only
            "family_friendly=1",                            # Family-friendly tag
            "popular_filters=family_friendly"               # Prioritize family hotels
        ])
        
        all_params = '&'.join(query_parts + family_filters)
        return f"{base_url}?{all_params}"
    
    def _generate_airbnb_search(self, dest_name: str, amenities: List[str], 
                               trip_duration: int) -> str:
        """Generate Airbnb search URL with baby-friendly filters"""
        
        base_url = f"https://www.airbnb.com/s/{urllib.parse.quote(dest_name)}/homes"
        
        params = {
            'adults': '2',
            'children': '1',
            'infants': '1',
            'place_id': '',
            'refinement_paths[]': '/homes',
            'search_type': 'filter_change'
        }
        
        # Add amenity filters
        amenity_ids = []
        if "Crib/baby cot" in amenities:
            amenity_ids.append('45')  # Crib
        if "Kitchenette/kitchen" in amenities:
            amenity_ids.append('8')   # Kitchen
        if "Laundry facilities" in amenities:
            amenity_ids.append('33')  # Washer
            amenity_ids.append('34')  # Dryer
        if "High chair" in amenities:
            amenity_ids.append('37')  # High chair
        
        # Add property type filters for families
        params['property_type_id[]'] = ['1', '2']  # Apartments and houses
        params['min_bedrooms'] = '1'
        
        # Build query string
        query_parts = []
        for key, value in params.items():
            if isinstance(value, list):
                for v in value:
                    query_parts.append(f"{key}={v}")
            else:
                query_parts.append(f"{key}={urllib.parse.quote(str(value))}")
        
        # Add amenity filters
        for amenity_id in amenity_ids:
            query_parts.append(f"amenities[]={amenity_id}")
        
        return f"{base_url}?{'&'.join(query_parts)}"
    
    def _generate_hotels_search(self, dest_name: str, amenities: List[str]) -> str:
        """Generate Hotels.com search URL"""
        
        params = {
            'destination': dest_name,
            'startDate': '',  # Will be filled by user
            'endDate': '',    # Will be filled by user
            'adults': '2',
            'children': '1',
            'rooms': '1'
        }
        
        # Add amenity filters
        amenity_codes = []
        if "Crib/baby cot" in amenities:
            amenity_codes.append('CRIB')
        if "Kitchenette/kitchen" in amenities:
            amenity_codes.append('KITCHEN')
        if "Laundry facilities" in amenities:
            amenity_codes.append('LAUNDRY')
        
        if amenity_codes:
            params['amenities'] = ','.join(amenity_codes)
        
        base_url = "https://www.hotels.com/search.do"
        query_string = urllib.parse.urlencode(params)
        return f"{base_url}?{query_string}"
    
    def _generate_expedia_search(self, dest_name: str, amenities: List[str]) -> str:
        """Generate Expedia search URL"""
        
        params = {
            'destination': dest_name,
            'adults': '2',
            'children': '1',
            'childAge': '0',
            'rooms': '1'
        }
        
        # Add filters
        filters = []
        if "Crib/baby cot" in amenities:
            filters.append('CRIBS_ALLOWED')
        if "Kitchenette/kitchen" in amenities:
            filters.append('KITCHEN')
        if "Laundry facilities" in amenities:
            filters.append('LAUNDRY')
        
        if filters:
            params['amenities'] = ','.join(filters)
        
        base_url = "https://www.expedia.com/Hotel-Search"
        query_string = urllib.parse.urlencode(params)
        return f"{base_url}?{query_string}"
    
    def _generate_hospital_proximity_search(self, dest_name: str) -> HotelSearchLink:
        """Generate search for hotels near hospitals"""
        
        search_query = f"{dest_name} hotels near hospital family friendly"
        google_maps_url = f"https://www.google.com/maps/search/{urllib.parse.quote(search_query)}"
        
        return HotelSearchLink(
            platform="Google Maps",
            url=google_maps_url,
            description="Hotels near medical facilities with reviews",
            filters_applied=["Near hospitals", "Family-friendly", "User reviews"]
        )
    
    def _generate_beach_resort_search(self, dest_name: str, amenities: List[str]) -> HotelSearchLink:
        """Generate search for beach resorts with baby facilities"""
        
        params = {
            'ss': f"{dest_name} beach resort",
            'group_adults': '2',
            'group_children': '1',
            'sb_travel_purpose': 'leisure',
            'family_facilities': '96',  # Family rooms
            'hotelfacility': '53',      # Beach
        }
        
        base_url = "https://www.booking.com/searchresults.html"
        query_string = urllib.parse.urlencode(params)
        
        return HotelSearchLink(
            platform="Beach Resorts",
            url=f"{base_url}?{query_string}",
            description="Beach resorts with family amenities",
            filters_applied=["Beach access", "Family rooms", "Resort facilities"]
        )
    
    def _get_applied_filters(self, amenities: List[str], platform: str) -> List[str]:
        """Get list of filters that will be applied for display"""
        
        applied = []
        
        # Common filters
        if "Crib/baby cot" in amenities:
            applied.append("✓ Cribs/Baby cots")
        if "Kitchenette/kitchen" in amenities:
            applied.append("✓ Kitchen facilities")
        if "Laundry facilities" in amenities:
            applied.append("✓ Laundry access")
        if "High chair" in amenities:
            applied.append("✓ High chairs")
        
        # Platform-specific
        if platform == 'booking':
            applied.extend(["✓ Family rooms", "✓ High ratings (8+)"])
        elif platform == 'airbnb':
            applied.extend(["✓ Entire homes", "✓ Multiple bedrooms"])
        
        return applied
    
    def get_search_instructions(self, baby_age: int, trip_duration: int) -> Dict[str, List[str]]:
        """Get platform-specific search instructions"""
        
        return {
            "Before Searching": [
                "📅 Set your exact travel dates for accurate pricing",
                "👶 Specify you're traveling with a baby/child",
                "📍 Consider distance to city center vs. quiet areas",
                "💰 Set your budget range clearly"
            ],
            "Platform Tips": [
                "**Booking.com**: Use 'Family Facilities' filter section",
                "**Airbnb**: Search for 'Entire Place' with baby amenities",
                "**Hotels.com**: Check 'Family-Friendly' in amenities",
                "**Expedia**: Look for 'Family Package' deals"
            ],
            "What to Look For": [
                "🏥 Distance to nearest hospital/clinic",
                "🛒 Proximity to pharmacies and supermarkets",
                "🍼 Kitchen facilities for bottle preparation",
                "🧺 Laundry access for longer stays" if trip_duration > 5 else "🧺 Laundry service available",
                "🛏️ Confirm crib availability before booking",
                "📞 Contact property about baby-specific needs"
            ],
            "Red Flags to Avoid": [
                "❌ No mention of family facilities",
                "❌ Party hotels or adult-only policies",
                "❌ Remote locations without nearby amenities",
                "❌ Properties without recent family reviews"
            ]
        }
    
    def get_booking_checklist(self) -> List[str]:
        """Get checklist for booking baby-friendly accommodation"""
        
        return [
            "☎️ **Call/Email Property**: Confirm crib availability and setup",
            "📸 **Request Photos**: Ask for pictures of baby facilities",
            "🏥 **Verify Medical**: Distance to nearest hospital/clinic",
            "🛒 **Check Amenities**: Nearby pharmacy, supermarket, restaurants",
            "🚗 **Transportation**: Airport transfer and local transport options",
            "🍼 **Kitchen Details**: Microwave, refrigerator, bottle sterilizer",
            "🧺 **Laundry Options**: In-room, on-site, or nearby service",
            "🔒 **Safety Features**: Baby-proofing, pool fencing, balcony locks",
            "📝 **Cancellation Policy**: Flexible options for traveling with baby",
            "💬 **Read Reviews**: Focus on recent reviews from families"
        ]
    
    def generate_accommodation_summary(self, search_links: List[HotelSearchLink], 
                                     destination, preferences: Dict) -> str:
        """Generate a summary of accommodation search options"""
        
        summary = f"""
        ## 🏨 Accommodation Search Summary for {destination.display}
        
        Based on your preferences, we've generated {len(search_links)} specialized searches:
        
        **Your Requirements:**
        - Budget: {preferences.get('budget', 'Not specified')}
        - Essential: {', '.join(preferences.get('essential_amenities', [])[:3])}
        - Priorities: {', '.join(preferences.get('location_priorities', [])[:2])}
        
        **Quick Tips:**
        - 🎯 Start with Booking.com for widest selection
        - 🏠 Try Airbnb for longer stays (kitchen + laundry)
        - 📞 Always confirm baby amenities before booking
        - 📖 Read recent reviews from families
        """
        
        return summary