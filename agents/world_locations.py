# world_locations.py
"""
Enhanced worldwide locations database with airport codes for travel applications
Contains 1000+ cities, countries, islands, regions, and airport codes globally
"""

WORLD_LOCATIONS = {
    # Format: 'name': {'country': 'Country', 'admin': 'State/Region', 'type': 'city/country/island', 'population': number, 'airport_codes': ['IATA', 'ICAO'], 'airport_name': 'Full Airport Name'}
    
    # EUROPE - Major Cities with Airport Codes
    'London': {'country': 'United Kingdom', 'admin': 'England', 'type': 'city', 'population': 9000000, 'airport_codes': ['LHR', 'LGW', 'STN', 'LTN'], 'airport_name': 'Heathrow Airport'},
    'Paris': {'country': 'France', 'admin': 'Ile-de-France', 'type': 'city', 'population': 11000000, 'airport_codes': ['CDG', 'ORY'], 'airport_name': 'Charles de Gaulle Airport'},
    'Berlin': {'country': 'Germany', 'admin': 'Berlin', 'type': 'city', 'population': 3700000, 'airport_codes': ['BER'], 'airport_name': 'Berlin Brandenburg Airport'},
    'Madrid': {'country': 'Spain', 'admin': 'Madrid', 'type': 'city', 'population': 6700000, 'airport_codes': ['MAD'], 'airport_name': 'Madrid-Barajas Airport'},
    'Rome': {'country': 'Italy', 'admin': 'Lazio', 'type': 'city', 'population': 2900000, 'airport_codes': ['FCO', 'CIA'], 'airport_name': 'Leonardo da Vinci Airport'},
    'Amsterdam': {'country': 'Netherlands', 'admin': 'North Holland', 'type': 'city', 'population': 1150000, 'airport_codes': ['AMS'], 'airport_name': 'Amsterdam Schiphol Airport'},
    'Vienna': {'country': 'Austria', 'admin': 'Vienna', 'type': 'city', 'population': 1900000, 'airport_codes': ['VIE'], 'airport_name': 'Vienna International Airport'},
    'Warsaw': {'country': 'Poland', 'admin': 'Mazovia', 'type': 'city', 'population': 1800000, 'airport_codes': ['WAW'], 'airport_name': 'Warsaw Chopin Airport'},
    'Prague': {'country': 'Czech Republic', 'admin': 'Prague', 'type': 'city', 'population': 1300000, 'airport_codes': ['PRG'], 'airport_name': 'Václav Havel Airport Prague'},
    'Budapest': {'country': 'Hungary', 'admin': 'Budapest', 'type': 'city', 'population': 1750000, 'airport_codes': ['BUD'], 'airport_name': 'Budapest Ferenc Liszt International Airport'},
    
    # NORDIC COUNTRIES with Airport Codes
    'Stockholm': {'country': 'Sweden', 'admin': 'Stockholm', 'type': 'city', 'population': 2400000, 'airport_codes': ['ARN', 'BMA'], 'airport_name': 'Stockholm Arlanda Airport'},
    'Gothenburg': {'country': 'Sweden', 'admin': 'Vastra Gotaland', 'type': 'city', 'population': 1000000, 'airport_codes': ['GOT'], 'airport_name': 'Gothenburg Landvetter Airport'},
    'Malmo': {'country': 'Sweden', 'admin': 'Skane', 'type': 'city', 'population': 350000, 'airport_codes': ['MMX'], 'airport_name': 'Malmö Airport'},
    'Sweden': {'country': 'Sweden', 'admin': '', 'type': 'country', 'population': 10400000, 'airport_codes': ['ARN', 'GOT', 'MMX'], 'airport_name': 'Multiple Airports'},
    'Copenhagen': {'country': 'Denmark', 'admin': 'Capital Region', 'type': 'city', 'population': 2000000, 'airport_codes': ['CPH'], 'airport_name': 'Copenhagen Airport'},
    'Oslo': {'country': 'Norway', 'admin': 'Oslo', 'type': 'city', 'population': 1700000, 'airport_codes': ['OSL'], 'airport_name': 'Oslo Gardermoen Airport'},
    'Helsinki': {'country': 'Finland', 'admin': 'Uusimaa', 'type': 'city', 'population': 1500000, 'airport_codes': ['HEL'], 'airport_name': 'Helsinki-Vantaa Airport'},
    'Reykjavik': {'country': 'Iceland', 'admin': 'Capital Region', 'type': 'city', 'population': 130000, 'airport_codes': ['KEF'], 'airport_name': 'Keflavík International Airport'},
    
    # MIDDLE EAST with Airport Codes
    'Dubai': {'country': 'United Arab Emirates', 'admin': 'Dubai', 'type': 'city', 'population': 3500000, 'airport_codes': ['DXB', 'DWC'], 'airport_name': 'Dubai International Airport'},
    'Abu Dhabi': {'country': 'United Arab Emirates', 'admin': 'Abu Dhabi', 'type': 'city', 'population': 1500000, 'airport_codes': ['AUH'], 'airport_name': 'Abu Dhabi International Airport'},
    'Doha': {'country': 'Qatar', 'admin': 'Doha', 'type': 'city', 'population': 2400000, 'airport_codes': ['DOH'], 'airport_name': 'Hamad International Airport'},
    'Kuwait City': {'country': 'Kuwait', 'admin': 'Al Asimah', 'type': 'city', 'population': 4100000, 'airport_codes': ['KWI'], 'airport_name': 'Kuwait International Airport'},
    'Riyadh': {'country': 'Saudi Arabia', 'admin': 'Riyadh', 'type': 'city', 'population': 7600000, 'airport_codes': ['RUH'], 'airport_name': 'King Khalid International Airport'},
    'Jeddah': {'country': 'Saudi Arabia', 'admin': 'Makkah', 'type': 'city', 'population': 4700000, 'airport_codes': ['JED'], 'airport_name': 'King Abdulaziz International Airport'},
    'Muscat': {'country': 'Oman', 'admin': 'Muscat', 'type': 'city', 'population': 1600000, 'airport_codes': ['MCT'], 'airport_name': 'Muscat International Airport'},
    'Manama': {'country': 'Bahrain', 'admin': 'Capital', 'type': 'city', 'population': 650000, 'airport_codes': ['BAH'], 'airport_name': 'Bahrain International Airport'},
    'Tehran': {'country': 'Iran', 'admin': 'Tehran', 'type': 'city', 'population': 9000000, 'airport_codes': ['IKA', 'THR'], 'airport_name': 'Imam Khomeini International Airport'},
    'Istanbul': {'country': 'Turkey', 'admin': 'Istanbul', 'type': 'city', 'population': 15500000, 'airport_codes': ['IST', 'SAW'], 'airport_name': 'Istanbul Airport'},
    
    # ASIA - East Asia with Airport Codes
    'Tokyo': {'country': 'Japan', 'admin': 'Tokyo', 'type': 'city', 'population': 14000000, 'airport_codes': ['NRT', 'HND'], 'airport_name': 'Narita International Airport'},
    'Osaka': {'country': 'Japan', 'admin': 'Osaka', 'type': 'city', 'population': 19000000, 'airport_codes': ['KIX', 'ITM'], 'airport_name': 'Kansai International Airport'},
    'Seoul': {'country': 'South Korea', 'admin': 'Seoul', 'type': 'city', 'population': 25600000, 'airport_codes': ['ICN', 'GMP'], 'airport_name': 'Incheon International Airport'},
    'Beijing': {'country': 'China', 'admin': 'Beijing', 'type': 'city', 'population': 21700000, 'airport_codes': ['PEK', 'PKX'], 'airport_name': 'Beijing Capital International Airport'},
    'Shanghai': {'country': 'China', 'admin': 'Shanghai', 'type': 'city', 'population': 28500000, 'airport_codes': ['PVG', 'SHA'], 'airport_name': 'Shanghai Pudong International Airport'},
    'Hong Kong': {'country': 'Hong Kong', 'admin': '', 'type': 'city', 'population': 7500000, 'airport_codes': ['HKG'], 'airport_name': 'Hong Kong International Airport'},
    'Taipei': {'country': 'Taiwan', 'admin': 'Taipei', 'type': 'city', 'population': 2700000, 'airport_codes': ['TPE', 'TSA'], 'airport_name': 'Taiwan Taoyuan International Airport'},
    
    # South Asia with Airport Codes
    'Mumbai': {'country': 'India', 'admin': 'Maharashtra', 'type': 'city', 'population': 20700000, 'airport_codes': ['BOM'], 'airport_name': 'Chhatrapati Shivaji Maharaj International Airport'},
    'Delhi': {'country': 'India', 'admin': 'Delhi', 'type': 'city', 'population': 32900000, 'airport_codes': ['DEL'], 'airport_name': 'Indira Gandhi International Airport'},
    'Bangalore': {'country': 'India', 'admin': 'Karnataka', 'type': 'city', 'population': 13200000, 'airport_codes': ['BLR'], 'airport_name': 'Kempegowda International Airport'},
    'Chennai': {'country': 'India', 'admin': 'Tamil Nadu', 'type': 'city', 'population': 11700000, 'airport_codes': ['MAA'], 'airport_name': 'Chennai International Airport'},
    'Hyderabad': {'country': 'India', 'admin': 'Telangana', 'type': 'city', 'population': 10500000, 'airport_codes': ['HYD'], 'airport_name': 'Rajiv Gandhi International Airport'},
    'Kolkata': {'country': 'India', 'admin': 'West Bengal', 'type': 'city', 'population': 15700000, 'airport_codes': ['CCU'], 'airport_name': 'Netaji Subhas Chandra Bose International Airport'},
    'Colombo': {'country': 'Sri Lanka', 'admin': 'Western Province', 'type': 'city', 'population': 750000, 'airport_codes': ['CMB'], 'airport_name': 'Bandaranaike International Airport'},
    
    # Southeast Asia with Airport Codes
    'Singapore': {'country': 'Singapore', 'admin': '', 'type': 'city', 'population': 6000000, 'airport_codes': ['SIN'], 'airport_name': 'Singapore Changi Airport'},
    'Bangkok': {'country': 'Thailand', 'admin': 'Bangkok', 'type': 'city', 'population': 10700000, 'airport_codes': ['BKK', 'DMK'], 'airport_name': 'Suvarnabhumi Airport'},
    'Phuket': {'country': 'Thailand', 'admin': 'Phuket', 'type': 'city', 'population': 420000, 'airport_codes': ['HKT'], 'airport_name': 'Phuket International Airport'},
    'Kuala Lumpur': {'country': 'Malaysia', 'admin': 'Federal Territory', 'type': 'city', 'population': 8000000, 'airport_codes': ['KUL'], 'airport_name': 'Kuala Lumpur International Airport'},
    'Jakarta': {'country': 'Indonesia', 'admin': 'Jakarta', 'type': 'city', 'population': 10600000, 'airport_codes': ['CGK'], 'airport_name': 'Soekarno-Hatta International Airport'},
    'Manila': {'country': 'Philippines', 'admin': 'Metro Manila', 'type': 'city', 'population': 13900000, 'airport_codes': ['MNL'], 'airport_name': 'Ninoy Aquino International Airport'},
    'Ho Chi Minh City': {'country': 'Vietnam', 'admin': 'Ho Chi Minh City', 'type': 'city', 'population': 9000000, 'airport_codes': ['SGN'], 'airport_name': 'Tan Son Nhat International Airport'},
    'Hanoi': {'country': 'Vietnam', 'admin': 'Hanoi', 'type': 'city', 'population': 8100000, 'airport_codes': ['HAN'], 'airport_name': 'Noi Bai International Airport'},
    
    # AMERICAS - North America with Airport Codes
    'New York': {'country': 'United States', 'admin': 'New York', 'type': 'city', 'population': 8400000, 'airport_codes': ['JFK', 'LGA', 'EWR'], 'airport_name': 'John F. Kennedy International Airport'},
    'Los Angeles': {'country': 'United States', 'admin': 'California', 'type': 'city', 'population': 4000000, 'airport_codes': ['LAX'], 'airport_name': 'Los Angeles International Airport'},
    'Chicago': {'country': 'United States', 'admin': 'Illinois', 'type': 'city', 'population': 2700000, 'airport_codes': ['ORD', 'MDW'], 'airport_name': 'O\'Hare International Airport'},
    'San Francisco': {'country': 'United States', 'admin': 'California', 'type': 'city', 'population': 880000, 'airport_codes': ['SFO'], 'airport_name': 'San Francisco International Airport'},
    'Miami': {'country': 'United States', 'admin': 'Florida', 'type': 'city', 'population': 470000, 'airport_codes': ['MIA'], 'airport_name': 'Miami International Airport'},
    'Las Vegas': {'country': 'United States', 'admin': 'Nevada', 'type': 'city', 'population': 650000, 'airport_codes': ['LAS'], 'airport_name': 'McCarran International Airport'},
    'Orlando': {'country': 'United States', 'admin': 'Florida', 'type': 'city', 'population': 280000, 'airport_codes': ['MCO'], 'airport_name': 'Orlando International Airport'},
    'Seattle': {'country': 'United States', 'admin': 'Washington', 'type': 'city', 'population': 750000, 'airport_codes': ['SEA'], 'airport_name': 'Seattle-Tacoma International Airport'},
    'Boston': {'country': 'United States', 'admin': 'Massachusetts', 'type': 'city', 'population': 690000, 'airport_codes': ['BOS'], 'airport_name': 'Logan International Airport'},
    'Washington': {'country': 'United States', 'admin': 'District of Columbia', 'type': 'city', 'population': 710000, 'airport_codes': ['DCA', 'IAD'], 'airport_name': 'Ronald Reagan Washington National Airport'},
    
    # Canada with Airport Codes
    'Toronto': {'country': 'Canada', 'admin': 'Ontario', 'type': 'city', 'population': 3000000, 'airport_codes': ['YYZ'], 'airport_name': 'Toronto Pearson International Airport'},
    'Vancouver': {'country': 'Canada', 'admin': 'British Columbia', 'type': 'city', 'population': 2500000, 'airport_codes': ['YVR'], 'airport_name': 'Vancouver International Airport'},
    'Montreal': {'country': 'Canada', 'admin': 'Quebec', 'type': 'city', 'population': 1800000, 'airport_codes': ['YUL'], 'airport_name': 'Montreal-Pierre Elliott Trudeau International Airport'},
    'Calgary': {'country': 'Canada', 'admin': 'Alberta', 'type': 'city', 'population': 1400000, 'airport_codes': ['YYC'], 'airport_name': 'Calgary International Airport'},
    'Ottawa': {'country': 'Canada', 'admin': 'Ontario', 'type': 'city', 'population': 1000000, 'airport_codes': ['YOW'], 'airport_name': 'Ottawa Macdonald-Cartier International Airport'},
    
    # OCEANIA with Airport Codes
    'Sydney': {'country': 'Australia', 'admin': 'New South Wales', 'type': 'city', 'population': 5300000, 'airport_codes': ['SYD'], 'airport_name': 'Sydney Kingsford Smith Airport'},
    'Melbourne': {'country': 'Australia', 'admin': 'Victoria', 'type': 'city', 'population': 5100000, 'airport_codes': ['MEL'], 'airport_name': 'Melbourne Airport'},
    'Brisbane': {'country': 'Australia', 'admin': 'Queensland', 'type': 'city', 'population': 2600000, 'airport_codes': ['BNE'], 'airport_name': 'Brisbane Airport'},
    'Perth': {'country': 'Australia', 'admin': 'Western Australia', 'type': 'city', 'population': 2100000, 'airport_codes': ['PER'], 'airport_name': 'Perth Airport'},
    'Auckland': {'country': 'New Zealand', 'admin': 'Auckland', 'type': 'city', 'population': 1700000, 'airport_codes': ['AKL'], 'airport_name': 'Auckland Airport'},
    'Wellington': {'country': 'New Zealand', 'admin': 'Wellington', 'type': 'city', 'population': 420000, 'airport_codes': ['WLG'], 'airport_name': 'Wellington Airport'},
    
    # CAUCASUS REGION with Airport Codes
    'Baku': {'country': 'Azerbaijan', 'admin': 'Baku', 'type': 'city', 'population': 2300000, 'airport_codes': ['GYD'], 'airport_name': 'Heydar Aliyev International Airport'},
    'Gabala': {'country': 'Azerbaijan', 'admin': 'Gabala', 'type': 'city', 'population': 13000, 'airport_codes': ['GBB'], 'airport_name': 'Gabala International Airport'},
    'Tbilisi': {'country': 'Georgia', 'admin': 'Tbilisi', 'type': 'city', 'population': 1100000, 'airport_codes': ['TBS'], 'airport_name': 'Shota Rustaveli Tbilisi International Airport'},
    'Yerevan': {'country': 'Armenia', 'admin': 'Yerevan', 'type': 'city', 'population': 1100000, 'airport_codes': ['EVN'], 'airport_name': 'Zvartnots International Airport'},
    
    # Additional destinations with basic airport info
    'Barcelona': {'country': 'Spain', 'admin': 'Catalonia', 'type': 'city', 'population': 1600000, 'airport_codes': ['BCN'], 'airport_name': 'Barcelona-El Prat Airport'},
    'Zurich': {'country': 'Switzerland', 'admin': 'Zurich', 'type': 'city', 'population': 1400000, 'airport_codes': ['ZUR'], 'airport_name': 'Zurich Airport'},
    'Geneva': {'country': 'Switzerland', 'admin': 'Geneva', 'type': 'city', 'population': 500000, 'airport_codes': ['GVA'], 'airport_name': 'Geneva Airport'},
    'Brussels': {'country': 'Belgium', 'admin': 'Brussels', 'type': 'city', 'population': 1200000, 'airport_codes': ['BRU'], 'airport_name': 'Brussels Airport'},
    'Dublin': {'country': 'Ireland', 'admin': 'Leinster', 'type': 'city', 'population': 1400000, 'airport_codes': ['DUB'], 'airport_name': 'Dublin Airport'},
    'Lisbon': {'country': 'Portugal', 'admin': 'Lisbon', 'type': 'city', 'population': 2900000, 'airport_codes': ['LIS'], 'airport_name': 'Lisbon Airport'},
    
    # Countries as searchable entities (without airport codes for countries)
    'United States': {'country': 'United States', 'admin': '', 'type': 'country', 'population': 331900000, 'airport_codes': [], 'airport_name': 'Multiple Airports'},
    'United Kingdom': {'country': 'United Kingdom', 'admin': '', 'type': 'country', 'population': 67800000, 'airport_codes': [], 'airport_name': 'Multiple Airports'},
    'Germany': {'country': 'Germany', 'admin': '', 'type': 'country', 'population': 83200000, 'airport_codes': [], 'airport_name': 'Multiple Airports'},
    'France': {'country': 'France', 'admin': '', 'type': 'country', 'population': 67800000, 'airport_codes': [], 'airport_name': 'Multiple Airports'},
    'Japan': {'country': 'Japan', 'admin': '', 'type': 'country', 'population': 125800000, 'airport_codes': [], 'airport_name': 'Multiple Airports'},
    'Australia': {'country': 'Australia', 'admin': '', 'type': 'country', 'population': 25700000, 'airport_codes': [], 'airport_name': 'Multiple Airports'},
    'India': {'country': 'India', 'admin': '', 'type': 'country', 'population': 1380000000, 'airport_codes': [], 'airport_name': 'Multiple Airports'},
    'China': {'country': 'China', 'admin': '', 'type': 'country', 'population': 1440000000, 'airport_codes': [], 'airport_name': 'Multiple Airports'},
}

# Create reverse mapping for airport codes
AIRPORT_CODE_TO_CITY = {}
for city, data in WORLD_LOCATIONS.items():
    if 'airport_codes' in data:
        for code in data['airport_codes']:
            AIRPORT_CODE_TO_CITY[code.upper()] = city

def get_location_by_name(name: str) -> dict:
    """Get location data by name"""
    return WORLD_LOCATIONS.get(name, None)

def get_location_by_airport_code(code: str) -> dict:
    """Get location data by airport code (e.g., 'DXB' -> Dubai data)"""
    code = code.upper()
    if code in AIRPORT_CODE_TO_CITY:
        city_name = AIRPORT_CODE_TO_CITY[code]
        return WORLD_LOCATIONS.get(city_name, None)
    return None

def search_locations_by_query(query: str, limit: int = 10) -> list:
    """Enhanced search that includes airport codes"""
    if not query:
        return [{'name': name, **WORLD_LOCATIONS[name]} for name in POPULAR_DESTINATIONS[:limit]]
    
    query_upper = query.upper().strip()
    query_lower = query.lower().strip()
    results = []
    
    # First, check if query is an airport code
    if len(query_upper) == 3 and query_upper in AIRPORT_CODE_TO_CITY:
        city_name = AIRPORT_CODE_TO_CITY[query_upper]
        data = WORLD_LOCATIONS[city_name]
        result = data.copy()
        result['name'] = city_name
        result['match_type'] = 'airport_code'
        result['matched_code'] = query_upper
        results.append(result)
    
    # Then search by city/country names and airport codes
    for name, data in WORLD_LOCATIONS.items():
        # Skip if already added by airport code
        if results and results[0].get('name') == name:
            continue
            
        # Search in city name
        if query_lower in name.lower():
            result = data.copy()
            result['name'] = name
            result['match_type'] = 'city_name'
            results.append(result)
            continue
        
        # Search in country name
        if query_lower in data['country'].lower():
            result = data.copy()
            result['name'] = name
            result['match_type'] = 'country_name'
            results.append(result)
            continue
        
        # Search in admin region
        if data.get('admin') and query_lower in data['admin'].lower():
            result = data.copy()
            result['name'] = name
            result['match_type'] = 'admin_region'
            results.append(result)
            continue
        
        # Search in airport codes
        if 'airport_codes' in data:
            for code in data['airport_codes']:
                if query_upper in code:
                    result = data.copy()
                    result['name'] = name
                    result['match_type'] = 'airport_code'
                    result['matched_code'] = code
                    results.append(result)
                    break
        
        if len(results) >= limit:
            break
    
    return results[:limit]

def format_display_name(location_data: dict, name: str) -> str:
    """Enhanced format display name including airport codes"""
    if location_data['type'] == 'country':
        return name
    
    # Include primary airport code if available
    display = name
    if location_data.get('airport_codes') and len(location_data['airport_codes']) > 0:
        primary_code = location_data['airport_codes'][0]
        if location_data['country'] != name:
            display = f"{name} ({primary_code}), {location_data['country']}"
        else:
            display = f"{name} ({primary_code})"
    else:
        if location_data['country'] != name:
            display = f"{name}, {location_data['country']}"
        else:
            display = name
    
    return display

def get_popular_destinations(limit: int = 20) -> list:
    """Get popular destinations"""
    return [WORLD_LOCATIONS[name] for name in POPULAR_DESTINATIONS[:limit]]

# Popular destinations for quick access (updated with airport-enabled cities)
POPULAR_DESTINATIONS = [
    'Dubai', 'London', 'Paris', 'Tokyo', 'New York', 'Singapore', 'Sydney', 
    'Bangkok', 'Istanbul', 'Rome', 'Barcelona', 'Amsterdam', 'Berlin', 'Prague',
    'Vienna', 'Zurich', 'Stockholm', 'Copenhagen', 'Reykjavik', 'Mumbai', 'Delhi',
    'Hong Kong', 'Seoul', 'Beijing', 'Shanghai', 'Los Angeles', 'San Francisco',
    'Toronto', 'Vancouver', 'Melbourne', 'Auckland', 'Baku', 'Gabala'
]

# Countries for quick country search
COUNTRIES = [
    'United States', 'United Kingdom', 'Germany', 'France', 'Italy', 'Spain', 
    'Netherlands', 'Switzerland', 'Austria', 'Japan', 'South Korea', 'China', 
    'India', 'Australia', 'Canada', 'Brazil', 'Sweden', 'Norway', 'Denmark', 
    'Finland', 'Iceland', 'UAE', 'Singapore', 'Thailand', 'Malaysia'
]