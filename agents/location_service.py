# agents/location_service.py
"""
Global Location Service for destination management
Handles location search, autocomplete, and destination data
"""

import streamlit as st
from typing import List, Optional, Dict
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

class GlobalLocationService:
    """Service for managing global location data and search functionality"""
    
    def __init__(self):
        self._search_cache = {}
        self.top_family_destinations = [
            'Dubai', 'Singapore', 'Tokyo', 'London', 'Sydney', 
            'Barcelona', 'Amsterdam', 'Copenhagen', 'Reykjavik', 'Paris'
        ]
        self.all_locations = self._load_all_locations()
    
    def _load_all_locations(self) -> List[Destination]:
        """Load all locations for autocomplete from world_locations.py"""
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
            # Fallback locations if world_locations.py is not available
            return self._get_fallback_locations()
    
    def _get_fallback_locations(self) -> List[Destination]:
        """Fallback location data if main database fails to load"""
        return [
            Destination('Dubai', 'United Arab Emirates', 'Dubai', 3500000, 'city', 'Dubai (DXB), UAE'),
            Destination('London', 'United Kingdom', 'England', 9000000, 'city', 'London (LHR), UK'),
            Destination('Tokyo', 'Japan', 'Tokyo', 14000000, 'city', 'Tokyo (NRT), Japan'),
            Destination('New York', 'United States', 'New York', 8400000, 'city', 'New York (JFK), USA'),
            Destination('Singapore', 'Singapore', '', 6000000, 'city', 'Singapore (SIN)'),
            Destination('Bangkok', 'Thailand', 'Bangkok', 10700000, 'city', 'Bangkok (BKK), Thailand'),
            Destination('Paris', 'France', 'Ile-de-France', 11000000, 'city', 'Paris (CDG), France'),
            Destination('Sydney', 'Australia', 'New South Wales', 5300000, 'city', 'Sydney (SYD), Australia'),
            Destination('Barcelona', 'Spain', 'Catalonia', 1600000, 'city', 'Barcelona (BCN), Spain'),
            Destination('Amsterdam', 'Netherlands', 'North Holland', 1150000, 'city', 'Amsterdam (AMS), Netherlands'),
            Destination('Hyderabad', 'India', 'Telangana', 10500000, 'city', 'Hyderabad (HYD), India'),
        ]
    
    def search_destinations_autocomplete(self, searchterm: str) -> List[str]:
        """Autocomplete search function for streamlit-searchbox integration"""
        if not searchterm:
            # Return top family-friendly destinations for empty search
            return [dest.display for dest in self.all_locations[:10] 
                   if dest.name in self.top_family_destinations]
        
        searchterm_lower = searchterm.lower()
        matches = []
        
        # Search through all locations
        for dest in self.all_locations:
            if (searchterm_lower in dest.name.lower() or 
                searchterm_lower in dest.country.lower() or
                searchterm_lower in dest.display.lower() or
                searchterm_lower in dest.admin.lower()):
                matches.append(dest.display)
                if len(matches) >= 20:  # Limit results for performance
                    break
        
        return matches
    
    def get_destination_by_display(self, display_name: str) -> Optional[Destination]:
        """Get destination object by display name"""
        for dest in self.all_locations:
            if dest.display == display_name:
                return dest
        return None
    
    def search_destinations(self, query: str, limit: int = 8) -> List[Destination]:
        """Fallback search method for non-searchbox implementations"""
        if not query:
            return [dest for dest in self.all_locations[:limit] 
                   if dest.name in self.top_family_destinations]
        
        query_lower = query.lower()
        results = []
        
        for dest in self.all_locations:
            # Search in name, country, and admin fields
            if (query_lower in dest.name.lower() or 
                query_lower in dest.country.lower() or
                query_lower in dest.admin.lower()):
                results.append(dest)
                if len(results) >= limit:
                    break
        
        return results
    
    def get_family_friendly_destinations(self, limit: int = 10) -> List[Destination]:
        """Get curated list of family-friendly destinations"""
        family_destinations = []
        
        for dest in self.all_locations:
            if dest.name in self.top_family_destinations:
                family_destinations.append(dest)
                if len(family_destinations) >= limit:
                    break
        
        return family_destinations
    
    def get_destinations_by_region(self, region: str) -> List[Destination]:
        """Get destinations filtered by geographical region"""
        
        region_mapping = {
            'europe': ['United Kingdom', 'France', 'Germany', 'Spain', 'Italy', 'Netherlands', 
                      'Sweden', 'Norway', 'Denmark', 'Finland', 'Iceland'],
            'asia': ['Japan', 'China', 'India', 'Thailand', 'Singapore', 'Malaysia', 'Indonesia'],
            'middle_east': ['United Arab Emirates', 'Qatar', 'Saudi Arabia', 'Oman', 'Bahrain'],
            'north_america': ['United States', 'Canada'],
            'oceania': ['Australia', 'New Zealand']
        }
        
        region_countries = region_mapping.get(region.lower(), [])
        
        return [dest for dest in self.all_locations 
                if dest.country in region_countries]
    
    def get_destination_insights(self, destination: Destination) -> Dict[str, str]:
        """Get additional insights about a destination for families"""
        
        insights = {
            'family_rating': 'Standard',
            'infrastructure': 'Good',
            'language_barrier': 'Low',
            'medical_facilities': 'Available',
            'baby_facilities': 'Basic'
        }
        
        # Family-friendly destinations get enhanced ratings
        if destination.name in self.top_family_destinations:
            insights.update({
                'family_rating': 'Excellent',
                'infrastructure': 'World-class',
                'baby_facilities': 'Comprehensive'
            })
        
        # Country-specific insights
        english_speaking = ['United States', 'Canada', 'United Kingdom', 'Australia', 'New Zealand', 'Singapore']
        if destination.country in english_speaking:
            insights['language_barrier'] = 'None'
        
        developed_countries = ['Japan', 'Germany', 'France', 'Netherlands', 'Sweden', 'Norway', 'Denmark']
        if destination.country in developed_countries:
            insights.update({
                'infrastructure': 'Excellent',
                'medical_facilities': 'World-class'
            })
        
        # UAE-specific (since it's a key destination)
        if destination.country == 'United Arab Emirates':
            insights.update({
                'family_rating': 'Excellent',
                'infrastructure': 'World-class',
                'language_barrier': 'Low',
                'medical_facilities': 'Excellent',
                'baby_facilities': 'Comprehensive'
            })
        
        return insights
    
    def get_search_suggestions(self, partial_query: str) -> List[str]:
        """Get search suggestions for autocomplete"""
        if len(partial_query) < 2:
            return []
        
        suggestions = set()
        partial_lower = partial_query.lower()
        
        for dest in self.all_locations:
            # Add city names that match
            if dest.name.lower().startswith(partial_lower):
                suggestions.add(dest.name)
            
            # Add country names that match
            if dest.country.lower().startswith(partial_lower):
                suggestions.add(dest.country)
            
            # Limit suggestions
            if len(suggestions) >= 10:
                break
        
        return sorted(list(suggestions))
    
    def validate_destination(self, destination_name: str) -> bool:
        """Validate if a destination exists in the database"""
        destination_lower = destination_name.lower()
        
        for dest in self.all_locations:
            if (dest.name.lower() == destination_lower or 
                dest.display.lower() == destination_lower):
                return True
        
        return False
    
    def get_nearby_destinations(self, destination: Destination, limit: int = 5) -> List[Destination]:
        """Get destinations in the same country or region"""
        
        # Same country destinations
        same_country = [dest for dest in self.all_locations 
                       if dest.country == destination.country and dest.name != destination.name]
        
        if len(same_country) >= limit:
            return same_country[:limit]
        
        # If not enough in same country, get from same region
        region_map = {
            'Europe': ['United Kingdom', 'France', 'Germany', 'Spain', 'Italy', 'Netherlands'],
            'Asia': ['Japan', 'China', 'India', 'Thailand', 'Singapore', 'Malaysia'],
            'Middle East': ['United Arab Emirates', 'Qatar', 'Saudi Arabia', 'Oman']
        }
        
        dest_region = None
        for region, countries in region_map.items():
            if destination.country in countries:
                dest_region = region
                break
        
        if dest_region:
            region_destinations = [dest for dest in self.all_locations 
                                 if dest.country in region_map[dest_region] 
                                 and dest.name != destination.name]
            return (same_country + region_destinations)[:limit]
        
        return same_country[:limit]

class LocationCache:
    """Simple caching mechanism for location searches"""
    
    def __init__(self, max_size: int = 100):
        self.cache = {}
        self.max_size = max_size
        self.access_order = []
    
    def get(self, key: str) -> Optional[List[Destination]]:
        """Get cached search results"""
        if key in self.cache:
            # Move to end (most recently accessed)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None
    
    def set(self, key: str, value: List[Destination]) -> None:
        """Cache search results"""
        if len(self.cache) >= self.max_size:
            # Remove least recently used
            oldest_key = self.access_order.pop(0)
            del self.cache[oldest_key]
        
        self.cache[key] = value
        self.access_order.append(key)
    
    def clear(self) -> None:
        """Clear cache"""
        self.cache.clear()
        self.access_order.clear()

# Utility functions for external use
def format_destination_display(destination: Destination) -> str:
    """Format destination for display with consistent styling"""
    if destination.type == 'country':
        return destination.name
    
    if destination.country != destination.name:
        return f"{destination.name}, {destination.country}"
    else:
        return destination.name

def get_destination_emoji(destination: Destination) -> str:
    """Get appropriate emoji for destination"""
    
    country_emojis = {
        'United Arab Emirates': '🇦🇪',
        'United Kingdom': '🇬🇧',
        'Japan': '🇯🇵',
        'United States': '🇺🇸',
        'Singapore': '🇸🇬',
        'Thailand': '🇹🇭',
        'France': '🇫🇷',
        'Australia': '🇦🇺',
        'Spain': '🇪🇸',
        'Netherlands': '🇳🇱',
        'India': '🇮🇳',
        'Germany': '🇩🇪',
        'Italy': '🇮🇹',
        'Sweden': '🇸🇪',
        'Norway': '🇳🇴',
        'Denmark': '🇩🇰',
        'Iceland': '🇮🇸'
    }
    
    return country_emojis.get(destination.country, '🌍')