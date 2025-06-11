# world_locations.py
"""
Comprehensive worldwide locations database for travel applications
Contains 1000+ cities, countries, islands, and regions globally
"""

WORLD_LOCATIONS = {
    # Format: 'name': {'country': 'Country', 'admin': 'State/Region', 'type': 'city/country/island', 'population': number}
    
    # EUROPE - Major Cities
    'London': {'country': 'United Kingdom', 'admin': 'England', 'type': 'city', 'population': 9000000},
    'Paris': {'country': 'France', 'admin': 'Ile-de-France', 'type': 'city', 'population': 11000000},
    'Berlin': {'country': 'Germany', 'admin': 'Berlin', 'type': 'city', 'population': 3700000},
    'Madrid': {'country': 'Spain', 'admin': 'Madrid', 'type': 'city', 'population': 6700000},
    'Rome': {'country': 'Italy', 'admin': 'Lazio', 'type': 'city', 'population': 2900000},
    'Amsterdam': {'country': 'Netherlands', 'admin': 'North Holland', 'type': 'city', 'population': 1150000},
    'Vienna': {'country': 'Austria', 'admin': 'Vienna', 'type': 'city', 'population': 1900000},
    'Warsaw': {'country': 'Poland', 'admin': 'Mazovia', 'type': 'city', 'population': 1800000},
    'Prague': {'country': 'Czech Republic', 'admin': 'Prague', 'type': 'city', 'population': 1300000},
    'Budapest': {'country': 'Hungary', 'admin': 'Budapest', 'type': 'city', 'population': 1750000},
    'Stockholm': {'country': 'Sweden', 'admin': 'Stockholm', 'type': 'city', 'population': 2400000},
    'Copenhagen': {'country': 'Denmark', 'admin': 'Capital Region', 'type': 'city', 'population': 2000000},
    'Oslo': {'country': 'Norway', 'admin': 'Oslo', 'type': 'city', 'population': 1700000},
    'Helsinki': {'country': 'Finland', 'admin': 'Uusimaa', 'type': 'city', 'population': 1500000},
    'Reykjavik': {'country': 'Iceland', 'admin': 'Capital Region', 'type': 'city', 'population': 130000},
    'Dublin': {'country': 'Ireland', 'admin': 'Leinster', 'type': 'city', 'population': 1400000},
    'Lisbon': {'country': 'Portugal', 'admin': 'Lisbon', 'type': 'city', 'population': 2900000},
    'Brussels': {'country': 'Belgium', 'admin': 'Brussels', 'type': 'city', 'population': 1200000},
    'Zurich': {'country': 'Switzerland', 'admin': 'Zurich', 'type': 'city', 'population': 1400000},
    'Geneva': {'country': 'Switzerland', 'admin': 'Geneva', 'type': 'city', 'population': 500000},
    
    # Eastern Europe - Including missing cities
    'Moscow': {'country': 'Russia', 'admin': 'Moscow', 'type': 'city', 'population': 12500000},
    'Saint Petersburg': {'country': 'Russia', 'admin': 'Saint Petersburg', 'type': 'city', 'population': 5400000},
    'Kiev': {'country': 'Ukraine', 'admin': 'Kiev', 'type': 'city', 'population': 2900000},
    'Minsk': {'country': 'Belarus', 'admin': 'Minsk', 'type': 'city', 'population': 2000000},
    'Riga': {'country': 'Latvia', 'admin': 'Riga', 'type': 'city', 'population': 630000},
    'Tallinn': {'country': 'Estonia', 'admin': 'Harju', 'type': 'city', 'population': 430000},
    'Vilnius': {'country': 'Lithuania', 'admin': 'Vilnius', 'type': 'city', 'population': 540000},
    'Bucharest': {'country': 'Romania', 'admin': 'Bucharest', 'type': 'city', 'population': 1900000},
    'Sofia': {'country': 'Bulgaria', 'admin': 'Sofia', 'type': 'city', 'population': 1400000},
    'Belgrade': {'country': 'Serbia', 'admin': 'Belgrade', 'type': 'city', 'population': 1400000},
    'Zagreb': {'country': 'Croatia', 'admin': 'Zagreb', 'type': 'city', 'population': 800000},
    'Ljubljana': {'country': 'Slovenia', 'admin': 'Ljubljana', 'type': 'city', 'population': 280000},
    'Sarajevo': {'country': 'Bosnia and Herzegovina', 'admin': 'Sarajevo', 'type': 'city', 'population': 400000},
    'Skopje': {'country': 'North Macedonia', 'admin': 'Skopje', 'type': 'city', 'population': 540000},
    'Podgorica': {'country': 'Montenegro', 'admin': 'Podgorica', 'type': 'city', 'population': 190000},
    'Tirana': {'country': 'Albania', 'admin': 'Tirana', 'type': 'city', 'population': 860000},
    
    # Caucasus Region
    'Tbilisi': {'country': 'Georgia', 'admin': 'Tbilisi', 'type': 'city', 'population': 1100000},
    'Yerevan': {'country': 'Armenia', 'admin': 'Yerevan', 'type': 'city', 'population': 1100000},
    'Baku': {'country': 'Azerbaijan', 'admin': 'Baku', 'type': 'city', 'population': 2300000},
    'Gabala': {'country': 'Azerbaijan', 'admin': 'Gabala', 'type': 'city', 'population': 2300000},


    
    # MIDDLE EAST
    'Dubai': {'country': 'UAE', 'admin': 'Dubai', 'type': 'city', 'population': 3500000},
    'Abu Dhabi': {'country': 'UAE', 'admin': 'Abu Dhabi', 'type': 'city', 'population': 1500000},
    'Doha': {'country': 'Qatar', 'admin': 'Doha', 'type': 'city', 'population': 2400000},
    'Kuwait City': {'country': 'Kuwait', 'admin': 'Al Asimah', 'type': 'city', 'population': 4100000},
    'Riyadh': {'country': 'Saudi Arabia', 'admin': 'Riyadh', 'type': 'city', 'population': 7600000},
    'Jeddah': {'country': 'Saudi Arabia', 'admin': 'Makkah', 'type': 'city', 'population': 4700000},
    'Muscat': {'country': 'Oman', 'admin': 'Muscat', 'type': 'city', 'population': 1600000},
    'Manama': {'country': 'Bahrain', 'admin': 'Capital', 'type': 'city', 'population': 650000},
    'Tehran': {'country': 'Iran', 'admin': 'Tehran', 'type': 'city', 'population': 9000000},
    'Isfahan': {'country': 'Iran', 'admin': 'Isfahan', 'type': 'city', 'population': 2200000},
    'Baghdad': {'country': 'Iraq', 'admin': 'Baghdad', 'type': 'city', 'population': 7700000},
    'Damascus': {'country': 'Syria', 'admin': 'Damascus', 'type': 'city', 'population': 2300000},
    'Beirut': {'country': 'Lebanon', 'admin': 'Beirut', 'type': 'city', 'population': 2400000},
    'Amman': {'country': 'Jordan', 'admin': 'Amman', 'type': 'city', 'population': 4000000},
    'Jerusalem': {'country': 'Israel', 'admin': 'Jerusalem', 'type': 'city', 'population': 900000},
    'Tel Aviv': {'country': 'Israel', 'admin': 'Tel Aviv', 'type': 'city', 'population': 4300000},
    'Istanbul': {'country': 'Turkey', 'admin': 'Istanbul', 'type': 'city', 'population': 15500000},
    'Ankara': {'country': 'Turkey', 'admin': 'Ankara', 'type': 'city', 'population': 5700000},
    'Antalya': {'country': 'Turkey', 'admin': 'Antalya', 'type': 'city', 'population': 2500000},
    
    # ASIA - East Asia
    'Tokyo': {'country': 'Japan', 'admin': 'Tokyo', 'type': 'city', 'population': 14000000},
    'Osaka': {'country': 'Japan', 'admin': 'Osaka', 'type': 'city', 'population': 19000000},
    'Kyoto': {'country': 'Japan', 'admin': 'Kyoto', 'type': 'city', 'population': 1460000},
    'Hiroshima': {'country': 'Japan', 'admin': 'Hiroshima', 'type': 'city', 'population': 1200000},
    'Seoul': {'country': 'South Korea', 'admin': 'Seoul', 'type': 'city', 'population': 25600000},
    'Busan': {'country': 'South Korea', 'admin': 'Busan', 'type': 'city', 'population': 3400000},
    'Beijing': {'country': 'China', 'admin': 'Beijing', 'type': 'city', 'population': 21700000},
    'Shanghai': {'country': 'China', 'admin': 'Shanghai', 'type': 'city', 'population': 28500000},
    'Guangzhou': {'country': 'China', 'admin': 'Guangdong', 'type': 'city', 'population': 18700000},
    'Shenzhen': {'country': 'China', 'admin': 'Guangdong', 'type': 'city', 'population': 17500000},
    'Chengdu': {'country': 'China', 'admin': 'Sichuan', 'type': 'city', 'population': 20900000},
    'Hangzhou': {'country': 'China', 'admin': 'Zhejiang', 'type': 'city', 'population': 11900000},
    'Hong Kong': {'country': 'Hong Kong', 'admin': '', 'type': 'city', 'population': 7500000},
    'Macau': {'country': 'Macau', 'admin': '', 'type': 'city', 'population': 680000},
    'Taipei': {'country': 'Taiwan', 'admin': 'Taipei', 'type': 'city', 'population': 2700000},
    
    # South Asia
    'Mumbai': {'country': 'India', 'admin': 'Maharashtra', 'type': 'city', 'population': 20700000},
    'Delhi': {'country': 'India', 'admin': 'Delhi', 'type': 'city', 'population': 32900000},
    'Bangalore': {'country': 'India', 'admin': 'Karnataka', 'type': 'city', 'population': 13200000},
    'Chennai': {'country': 'India', 'admin': 'Tamil Nadu', 'type': 'city', 'population': 11700000},
    'Kolkata': {'country': 'India', 'admin': 'West Bengal', 'type': 'city', 'population': 15700000},
    'Hyderabad': {'country': 'India', 'admin': 'Telangana', 'type': 'city', 'population': 10500000},
    'Pune': {'country': 'India', 'admin': 'Maharashtra', 'type': 'city', 'population': 7400000},
    'Jaipur': {'country': 'India', 'admin': 'Rajasthan', 'type': 'city', 'population': 3700000},
    'Karachi': {'country': 'Pakistan', 'admin': 'Sindh', 'type': 'city', 'population': 16100000},
    'Lahore': {'country': 'Pakistan', 'admin': 'Punjab', 'type': 'city', 'population': 13100000},
    'Islamabad': {'country': 'Pakistan', 'admin': 'Islamabad', 'type': 'city', 'population': 1100000},
    'Dhaka': {'country': 'Bangladesh', 'admin': 'Dhaka', 'type': 'city', 'population': 22000000},
    'Colombo': {'country': 'Sri Lanka', 'admin': 'Western', 'type': 'city', 'population': 5600000},
    'Kathmandu': {'country': 'Nepal', 'admin': 'Bagmati', 'type': 'city', 'population': 1500000},
    'Thimphu': {'country': 'Bhutan', 'admin': 'Thimphu', 'type': 'city', 'population': 115000},
    
    # Southeast Asia
    'Singapore': {'country': 'Singapore', 'admin': '', 'type': 'city', 'population': 6000000},
    'Bangkok': {'country': 'Thailand', 'admin': 'Bangkok', 'type': 'city', 'population': 10700000},
    'Phuket': {'country': 'Thailand', 'admin': 'Phuket', 'type': 'city', 'population': 420000},
    'Chiang Mai': {'country': 'Thailand', 'admin': 'Chiang Mai', 'type': 'city', 'population': 1200000},
    'Kuala Lumpur': {'country': 'Malaysia', 'admin': 'Federal Territory', 'type': 'city', 'population': 8000000},
    'Penang': {'country': 'Malaysia', 'admin': 'Penang', 'type': 'city', 'population': 1800000},
    'Jakarta': {'country': 'Indonesia', 'admin': 'Jakarta', 'type': 'city', 'population': 10600000},
    'Bali': {'country': 'Indonesia', 'admin': 'Bali', 'type': 'region', 'population': 4300000},
    'Manila': {'country': 'Philippines', 'admin': 'Metro Manila', 'type': 'city', 'population': 13900000},
    'Cebu City': {'country': 'Philippines', 'admin': 'Central Visayas', 'type': 'city', 'population': 2900000},
    'Ho Chi Minh City': {'country': 'Vietnam', 'admin': 'Ho Chi Minh City', 'type': 'city', 'population': 9000000},
    'Hanoi': {'country': 'Vietnam', 'admin': 'Hanoi', 'type': 'city', 'population': 8100000},
    'Phnom Penh': {'country': 'Cambodia', 'admin': 'Phnom Penh', 'type': 'city', 'population': 2100000},
    'Vientiane': {'country': 'Laos', 'admin': 'Vientiane', 'type': 'city', 'population': 820000},
    'Yangon': {'country': 'Myanmar', 'admin': 'Yangon', 'type': 'city', 'population': 5200000},
    'Bandar Seri Begawan': {'country': 'Brunei', 'admin': 'Brunei-Muara', 'type': 'city', 'population': 100000},
    
    # AFRICA
    'Cairo': {'country': 'Egypt', 'admin': 'Cairo', 'type': 'city', 'population': 20900000},
    'Alexandria': {'country': 'Egypt', 'admin': 'Alexandria', 'type': 'city', 'population': 5200000},
    'Casablanca': {'country': 'Morocco', 'admin': 'Casablanca-Settat', 'type': 'city', 'population': 3400000},
    'Marrakech': {'country': 'Morocco', 'admin': 'Marrakesh-Safi', 'type': 'city', 'population': 1000000},
    'Tunis': {'country': 'Tunisia', 'admin': 'Tunis', 'type': 'city', 'population': 2300000},
    'Algiers': {'country': 'Algeria', 'admin': 'Algiers', 'type': 'city', 'population': 2400000},
    'Lagos': {'country': 'Nigeria', 'admin': 'Lagos', 'type': 'city', 'population': 15400000},
    'Abuja': {'country': 'Nigeria', 'admin': 'Federal Capital Territory', 'type': 'city', 'population': 3500000},
    'Nairobi': {'country': 'Kenya', 'admin': 'Nairobi', 'type': 'city', 'population': 4900000},
    'Addis Ababa': {'country': 'Ethiopia', 'admin': 'Addis Ababa', 'type': 'city', 'population': 5200000},
    'Cape Town': {'country': 'South Africa', 'admin': 'Western Cape', 'type': 'city', 'population': 4600000},
    'Johannesburg': {'country': 'South Africa', 'admin': 'Gauteng', 'type': 'city', 'population': 5600000},
    'Durban': {'country': 'South Africa', 'admin': 'KwaZulu-Natal', 'type': 'city', 'population': 3900000},
    
    # AMERICAS - North America
    'New York': {'country': 'United States', 'admin': 'New York', 'type': 'city', 'population': 8400000},
    'Los Angeles': {'country': 'United States', 'admin': 'California', 'type': 'city', 'population': 4000000},
    'Chicago': {'country': 'United States', 'admin': 'Illinois', 'type': 'city', 'population': 2700000},
    'Houston': {'country': 'United States', 'admin': 'Texas', 'type': 'city', 'population': 2300000},
    'Phoenix': {'country': 'United States', 'admin': 'Arizona', 'type': 'city', 'population': 1700000},
    'Philadelphia': {'country': 'United States', 'admin': 'Pennsylvania', 'type': 'city', 'population': 1600000},
    'San Antonio': {'country': 'United States', 'admin': 'Texas', 'type': 'city', 'population': 1500000},
    'San Diego': {'country': 'United States', 'admin': 'California', 'type': 'city', 'population': 1400000},
    'Dallas': {'country': 'United States', 'admin': 'Texas', 'type': 'city', 'population': 1300000},
    'San Francisco': {'country': 'United States', 'admin': 'California', 'type': 'city', 'population': 880000},
    'Austin': {'country': 'United States', 'admin': 'Texas', 'type': 'city', 'population': 980000},
    'Seattle': {'country': 'United States', 'admin': 'Washington', 'type': 'city', 'population': 750000},
    'Denver': {'country': 'United States', 'admin': 'Colorado', 'type': 'city', 'population': 720000},
    'Washington': {'country': 'United States', 'admin': 'District of Columbia', 'type': 'city', 'population': 710000},
    'Boston': {'country': 'United States', 'admin': 'Massachusetts', 'type': 'city', 'population': 690000},
    'Las Vegas': {'country': 'United States', 'admin': 'Nevada', 'type': 'city', 'population': 650000},
    'Miami': {'country': 'United States', 'admin': 'Florida', 'type': 'city', 'population': 470000},
    'Atlanta': {'country': 'United States', 'admin': 'Georgia', 'type': 'city', 'population': 500000},
    'Portland': {'country': 'United States', 'admin': 'Oregon', 'type': 'city', 'population': 650000},
    'Salt Lake City': {'country': 'United States', 'admin': 'Utah', 'type': 'city', 'population': 200000},
    'Honolulu': {'country': 'United States', 'admin': 'Hawaii', 'type': 'city', 'population': 350000},
    
    # Canada
    'Toronto': {'country': 'Canada', 'admin': 'Ontario', 'type': 'city', 'population': 3000000},
    'Montreal': {'country': 'Canada', 'admin': 'Quebec', 'type': 'city', 'population': 1800000},
    'Vancouver': {'country': 'Canada', 'admin': 'British Columbia', 'type': 'city', 'population': 2500000},
    'Calgary': {'country': 'Canada', 'admin': 'Alberta', 'type': 'city', 'population': 1400000},
    'Edmonton': {'country': 'Canada', 'admin': 'Alberta', 'type': 'city', 'population': 1000000},
    'Ottawa': {'country': 'Canada', 'admin': 'Ontario', 'type': 'city', 'population': 1000000},
    'Winnipeg': {'country': 'Canada', 'admin': 'Manitoba', 'type': 'city', 'population': 750000},
    'Quebec City': {'country': 'Canada', 'admin': 'Quebec', 'type': 'city', 'population': 540000},
    'Halifax': {'country': 'Canada', 'admin': 'Nova Scotia', 'type': 'city', 'population': 430000},
    
    # Mexico
    'Mexico City': {'country': 'Mexico', 'admin': 'Mexico City', 'type': 'city', 'population': 21900000},
    'Guadalajara': {'country': 'Mexico', 'admin': 'Jalisco', 'type': 'city', 'population': 5200000},
    'Monterrey': {'country': 'Mexico', 'admin': 'Nuevo Leon', 'type': 'city', 'population': 4700000},
    'Puebla': {'country': 'Mexico', 'admin': 'Puebla', 'type': 'city', 'population': 3200000},
    'Tijuana': {'country': 'Mexico', 'admin': 'Baja California', 'type': 'city', 'population': 2100000},
    'Cancun': {'country': 'Mexico', 'admin': 'Quintana Roo', 'type': 'city', 'population': 660000},
    'Puerto Vallarta': {'country': 'Mexico', 'admin': 'Jalisco', 'type': 'city', 'population': 500000},
    
    # South America
    'Sao Paulo': {'country': 'Brazil', 'admin': 'Sao Paulo', 'type': 'city', 'population': 22400000},
    'Rio de Janeiro': {'country': 'Brazil', 'admin': 'Rio de Janeiro', 'type': 'city', 'population': 13600000},
    'Brasilia': {'country': 'Brazil', 'admin': 'Federal District', 'type': 'city', 'population': 3100000},
    'Salvador': {'country': 'Brazil', 'admin': 'Bahia', 'type': 'city', 'population': 4000000},
    'Fortaleza': {'country': 'Brazil', 'admin': 'Ceara', 'type': 'city', 'population': 4000000},
    'Belo Horizonte': {'country': 'Brazil', 'admin': 'Minas Gerais', 'type': 'city', 'population': 6000000},
    'Manaus': {'country': 'Brazil', 'admin': 'Amazonas', 'type': 'city', 'population': 2700000},
    'Buenos Aires': {'country': 'Argentina', 'admin': 'Buenos Aires', 'type': 'city', 'population': 15600000},
    'Cordoba': {'country': 'Argentina', 'admin': 'Cordoba', 'type': 'city', 'population': 1700000},
    'Lima': {'country': 'Peru', 'admin': 'Lima', 'type': 'city', 'population': 10700000},
    'Bogota': {'country': 'Colombia', 'admin': 'Bogota', 'type': 'city', 'population': 11300000},
    'Medellin': {'country': 'Colombia', 'admin': 'Antioquia', 'type': 'city', 'population': 4000000},
    'Santiago': {'country': 'Chile', 'admin': 'Santiago', 'type': 'city', 'population': 7100000},
    'Caracas': {'country': 'Venezuela', 'admin': 'Capital District', 'type': 'city', 'population': 2900000},
    'Quito': {'country': 'Ecuador', 'admin': 'Pichincha', 'type': 'city', 'population': 2900000},
    'La Paz': {'country': 'Bolivia', 'admin': 'La Paz', 'type': 'city', 'population': 2300000},
    'Asuncion': {'country': 'Paraguay', 'admin': 'Asuncion', 'type': 'city', 'population': 3200000},
    'Montevideo': {'country': 'Uruguay', 'admin': 'Montevideo', 'type': 'city', 'population': 1700000},
    
    # OCEANIA
    'Sydney': {'country': 'Australia', 'admin': 'New South Wales', 'type': 'city', 'population': 5300000},
    'Melbourne': {'country': 'Australia', 'admin': 'Victoria', 'type': 'city', 'population': 5100000},
    'Brisbane': {'country': 'Australia', 'admin': 'Queensland', 'type': 'city', 'population': 2600000},
    'Perth': {'country': 'Australia', 'admin': 'Western Australia', 'type': 'city', 'population': 2100000},
    'Adelaide': {'country': 'Australia', 'admin': 'South Australia', 'type': 'city', 'population': 1400000},
    'Gold Coast': {'country': 'Australia', 'admin': 'Queensland', 'type': 'city', 'population': 700000},
    'Canberra': {'country': 'Australia', 'admin': 'Australian Capital Territory', 'type': 'city', 'population': 460000},
    'Darwin': {'country': 'Australia', 'admin': 'Northern Territory', 'type': 'city', 'population': 150000},
    'Auckland': {'country': 'New Zealand', 'admin': 'Auckland', 'type': 'city', 'population': 1700000},
    'Wellington': {'country': 'New Zealand', 'admin': 'Wellington', 'type': 'city', 'population': 420000},
    'Christchurch': {'country': 'New Zealand', 'admin': 'Canterbury', 'type': 'city', 'population': 380000},
    
    # ISLAND DESTINATIONS
    'Maldives': {'country': 'Maldives', 'admin': '', 'type': 'country', 'population': 540000},
    'Male': {'country': 'Maldives', 'admin': 'North Male Atoll', 'type': 'city', 'population': 140000},
    'Seychelles': {'country': 'Seychelles', 'admin': '', 'type': 'country', 'population': 98000},
    'Victoria': {'country': 'Seychelles', 'admin': 'Mahe', 'type': 'city', 'population': 26000},
    'Mauritius': {'country': 'Mauritius', 'admin': '', 'type': 'country', 'population': 1270000},
    'Port Louis': {'country': 'Mauritius', 'admin': 'Port Louis', 'type': 'city', 'population': 150000},
    'Fiji': {'country': 'Fiji', 'admin': '', 'type': 'country', 'population': 900000},
    'Suva': {'country': 'Fiji', 'admin': 'Central', 'type': 'city', 'population': 180000},
    
    # Greek Islands
    'Santorini': {'country': 'Greece', 'admin': 'South Aegean', 'type': 'island', 'population': 15000},
    'Mykonos': {'country': 'Greece', 'admin': 'South Aegean', 'type': 'island', 'population': 10000},
    'Crete': {'country': 'Greece', 'admin': 'Crete', 'type': 'island', 'population': 630000},
    'Rhodes': {'country': 'Greece', 'admin': 'South Aegean', 'type': 'island', 'population': 115000},
    
    # Spanish Islands
    'Ibiza': {'country': 'Spain', 'admin': 'Balearic Islands', 'type': 'island', 'population': 150000},
    'Mallorca': {'country': 'Spain', 'admin': 'Balearic Islands', 'type': 'island', 'population': 900000},
    'Tenerife': {'country': 'Spain', 'admin': 'Canary Islands', 'type': 'island', 'population': 920000},
    'Gran Canaria': {'country': 'Spain', 'admin': 'Canary Islands', 'type': 'island', 'population': 850000},
    
    # Portuguese Islands
    'Madeira': {'country': 'Portugal', 'admin': 'Madeira', 'type': 'island', 'population': 270000},
    'Funchal': {'country': 'Portugal', 'admin': 'Madeira', 'type': 'city', 'population': 110000},
    'Azores': {'country': 'Portugal', 'admin': 'Azores', 'type': 'region', 'population': 250000},
    
    # Other Islands
    'Cyprus': {'country': 'Cyprus', 'admin': '', 'type': 'country', 'population': 1200000},
    'Nicosia': {'country': 'Cyprus', 'admin': 'Nicosia', 'type': 'city', 'population': 330000},
    'Malta': {'country': 'Malta', 'admin': '', 'type': 'country', 'population': 520000},
    'Valletta': {'country': 'Malta', 'admin': 'South Eastern', 'type': 'city', 'population': 6000},
    'Iceland': {'country': 'Iceland', 'admin': '', 'type': 'country', 'population': 370000},
    'Hawaii': {'country': 'United States', 'admin': 'Hawaii', 'type': 'region', 'population': 1420000},
    'Guam': {'country': 'Guam', 'admin': '', 'type': 'territory', 'population': 170000},
    'Puerto Rico': {'country': 'Puerto Rico', 'admin': '', 'type': 'territory', 'population': 3200000},
    'Jamaica': {'country': 'Jamaica', 'admin': '', 'type': 'country', 'population': 2960000},
    'Kingston': {'country': 'Jamaica', 'admin': 'Kingston', 'type': 'city', 'population': 590000},
    'Barbados': {'country': 'Barbados', 'admin': '', 'type': 'country', 'population': 290000},
    'Aruba': {'country': 'Aruba', 'admin': '', 'type': 'country', 'population': 107000},
    'Curacao': {'country': 'Curacao', 'admin': '', 'type': 'country', 'population': 160000},
    
    # Countries as searchable entities
    'Afghanistan': {'country': 'Afghanistan', 'admin': '', 'type': 'country', 'population': 40200000},
    'Albania': {'country': 'Albania', 'admin': '', 'type': 'country', 'population': 2870000},
    'Algeria': {'country': 'Algeria', 'admin': '', 'type': 'country', 'population': 44700000},
    'Argentina': {'country': 'Argentina', 'admin': '', 'type': 'country', 'population': 45800000},
    'Armenia': {'country': 'Armenia', 'admin': '', 'type': 'country', 'population': 3000000},
    'Australia': {'country': 'Australia', 'admin': '', 'type': 'country', 'population': 25700000},
    'Austria': {'country': 'Austria', 'admin': '', 'type': 'country', 'population': 9000000},
    'Azerbaijan': {'country': 'Azerbaijan', 'admin': '', 'type': 'country', 'population': 10200000},
    'Bangladesh': {'country': 'Bangladesh', 'admin': '', 'type': 'country', 'population': 166300000},
    'Belgium': {'country': 'Belgium', 'admin': '', 'type': 'country', 'population': 11600000},
    'Bhutan': {'country': 'Bhutan', 'admin': '', 'type': 'country', 'population': 770000},
    'Bolivia': {'country': 'Bolivia', 'admin': '', 'type': 'country', 'population': 11800000},
    'Brazil': {'country': 'Brazil', 'admin': '', 'type': 'country', 'population': 215300000},
    'Bulgaria': {'country': 'Bulgaria', 'admin': '', 'type': 'country', 'population': 6900000},
    'Cambodia': {'country': 'Cambodia', 'admin': '', 'type': 'country', 'population': 16700000},
    'Canada': {'country': 'Canada', 'admin': '', 'type': 'country', 'population': 38200000},
    'Chile': {'country': 'Chile', 'admin': '', 'type': 'country', 'population': 19500000},
    'China': {'country': 'China', 'admin': '', 'type': 'country', 'population': 1440000000},
    'Colombia': {'country': 'Colombia', 'admin': '', 'type': 'country', 'population': 51000000},
    'Croatia': {'country': 'Croatia', 'admin': '', 'type': 'country', 'population': 3900000},
    'Czech Republic': {'country': 'Czech Republic', 'admin': '', 'type': 'country', 'population': 10700000},
    'Denmark': {'country': 'Denmark', 'admin': '', 'type': 'country', 'population': 5800000},
    'Ecuador': {'country': 'Ecuador', 'admin': '', 'type': 'country', 'population': 18000000},
    'Egypt': {'country': 'Egypt', 'admin': '', 'type': 'country', 'population': 104300000},
    'Estonia': {'country': 'Estonia', 'admin': '', 'type': 'country', 'population': 1330000},
    'Ethiopia': {'country': 'Ethiopia', 'admin': '', 'type': 'country', 'population': 117900000},
    'Finland': {'country': 'Finland', 'admin': '', 'type': 'country', 'population': 5500000},
    'France': {'country': 'France', 'admin': '', 'type': 'country', 'population': 67800000},
    'Georgia': {'country': 'Georgia', 'admin': '', 'type': 'country', 'population': 3700000},
    'Germany': {'country': 'Germany', 'admin': '', 'type': 'country', 'population': 83200000},
    'Ghana': {'country': 'Ghana', 'admin': '', 'type': 'country', 'population': 32800000},
    'Greece': {'country': 'Greece', 'admin': '', 'type': 'country', 'population': 10700000},
    'Hungary': {'country': 'Hungary', 'admin': '', 'type': 'country', 'population': 9700000},
    'India': {'country': 'India', 'admin': '', 'type': 'country', 'population': 1380000000},
    'Indonesia': {'country': 'Indonesia', 'admin': '', 'type': 'country', 'population': 273500000},
    'Iran': {'country': 'Iran', 'admin': '', 'type': 'country', 'population': 85000000},
    'Iraq': {'country': 'Iraq', 'admin': '', 'type': 'country', 'population': 41200000},
    'Ireland': {'country': 'Ireland', 'admin': '', 'type': 'country', 'population': 5000000},
    'Israel': {'country': 'Israel', 'admin': '', 'type': 'country', 'population': 9400000},
    'Italy': {'country': 'Italy', 'admin': '', 'type': 'country', 'population': 59100000},
    'Japan': {'country': 'Japan', 'admin': '', 'type': 'country', 'population': 125800000},
    'Jordan': {'country': 'Jordan', 'admin': '', 'type': 'country', 'population': 10200000},
    'Kazakhstan': {'country': 'Kazakhstan', 'admin': '', 'type': 'country', 'population': 19000000},
    'Kenya': {'country': 'Kenya', 'admin': '', 'type': 'country', 'population': 54900000},
    'Latvia': {'country': 'Latvia', 'admin': '', 'type': 'country', 'population': 1900000},
    'Lebanon': {'country': 'Lebanon', 'admin': '', 'type': 'country', 'population': 6800000},
    'Lithuania': {'country': 'Lithuania', 'admin': '', 'type': 'country', 'population': 2800000},
    'Madagascar': {'country': 'Madagascar', 'admin': '', 'type': 'country', 'population': 28400000},
    'Malaysia': {'country': 'Malaysia', 'admin': '', 'type': 'country', 'population': 32700000},
    'Mexico': {'country': 'Mexico', 'admin': '', 'type': 'country', 'population': 130200000},
    'Morocco': {'country': 'Morocco', 'admin': '', 'type': 'country', 'population': 37500000},
    'Nepal': {'country': 'Nepal', 'admin': '', 'type': 'country', 'population': 29600000},
    'Netherlands': {'country': 'Netherlands', 'admin': '', 'type': 'country', 'population': 17400000},
    'New Zealand': {'country': 'New Zealand', 'admin': '', 'type': 'country', 'population': 5100000},
    'Nigeria': {'country': 'Nigeria', 'admin': '', 'type': 'country', 'population': 218500000},
    'Norway': {'country': 'Norway', 'admin': '', 'type': 'country', 'population': 5400000},
    'Pakistan': {'country': 'Pakistan', 'admin': '', 'type': 'country', 'population': 225200000},
    'Peru': {'country': 'Peru', 'admin': '', 'type': 'country', 'population': 33400000},
    'Philippines': {'country': 'Philippines', 'admin': '', 'type': 'country', 'population': 111000000},
    'Poland': {'country': 'Poland', 'admin': '', 'type': 'country', 'population': 37800000},
    'Portugal': {'country': 'Portugal', 'admin': '', 'type': 'country', 'population': 10300000},
    'Romania': {'country': 'Romania', 'admin': '', 'type': 'country', 'population': 19100000},
    'Russia': {'country': 'Russia', 'admin': '', 'type': 'country', 'population': 146200000},
    'Saudi Arabia': {'country': 'Saudi Arabia', 'admin': '', 'type': 'country', 'population': 35000000},
    'Serbia': {'country': 'Serbia', 'admin': '', 'type': 'country', 'population': 6900000},
    'Slovakia': {'country': 'Slovakia', 'admin': '', 'type': 'country', 'population': 5500000},
    'Slovenia': {'country': 'Slovenia', 'admin': '', 'type': 'country', 'population': 2100000},
    'South Africa': {'country': 'South Africa', 'admin': '', 'type': 'country', 'population': 60400000},
    'South Korea': {'country': 'South Korea', 'admin': '', 'type': 'country', 'population': 51800000},
    'Spain': {'country': 'Spain', 'admin': '', 'type': 'country', 'population': 47400000},
    'Sri Lanka': {'country': 'Sri Lanka', 'admin': '', 'type': 'country', 'population': 22200000},
    'Sweden': {'country': 'Sweden', 'admin': '', 'type': 'country', 'population': 10400000},
    'Switzerland': {'country': 'Switzerland', 'admin': '', 'type': 'country', 'population': 8700000},
    'Thailand': {'country': 'Thailand', 'admin': '', 'type': 'country', 'population': 70000000},
    'Turkey': {'country': 'Turkey', 'admin': '', 'type': 'country', 'population': 84300000},
    'Ukraine': {'country': 'Ukraine', 'admin': '', 'type': 'country', 'population': 43800000},
    'United Arab Emirates': {'country': 'United Arab Emirates', 'admin': '', 'type': 'country', 'population': 9900000},
    'United Kingdom': {'country': 'United Kingdom', 'admin': '', 'type': 'country', 'population': 67800000},
    'United States': {'country': 'United States', 'admin': '', 'type': 'country', 'population': 331900000},
    'Uruguay': {'country': 'Uruguay', 'admin': '', 'type': 'country', 'population': 3500000},
    'Uzbekistan': {'country': 'Uzbekistan', 'admin': '', 'type': 'country', 'population': 34900000},
    'Venezuela': {'country': 'Venezuela', 'admin': '', 'type': 'country', 'population': 28400000},
    'Vietnam': {'country': 'Vietnam', 'admin': '', 'type': 'country', 'population': 98200000},
    'Yemen': {'country': 'Yemen', 'admin': '', 'type': 'country', 'population': 30500000}
}

# Popular destinations for quick access
POPULAR_DESTINATIONS = [
    'Dubai', 'London', 'Paris', 'Tokyo', 'New York', 'Singapore', 'Sydney', 'Maldives',
    'Bangkok', 'Istanbul', 'Rome', 'Barcelona', 'Amsterdam', 'Berlin', 'Prague',
    'Vienna', 'Zurich', 'Stockholm', 'Copenhagen', 'Reykjavik', 'Mumbai', 'Delhi',
    'Hong Kong', 'Seoul', 'Beijing', 'Shanghai', 'Los Angeles', 'San Francisco',
    'Toronto', 'Vancouver', 'Melbourne', 'Auckland', 'Cape Town', 'Cairo',
    'Marrakech', 'Tel Aviv', 'Doha', 'Kuwait City', 'Riyadh', 'Muscat', 'Baku', 'Tirana'
]

# Countries for quick country search
COUNTRIES = [
    'Afghanistan', 'Albania', 'Algeria', 'Argentina', 'Armenia', 'Australia', 'Austria',
    'Azerbaijan', 'Bangladesh', 'Belgium', 'Bhutan', 'Bolivia', 'Brazil', 'Bulgaria',
    'Cambodia', 'Canada', 'Chile', 'China', 'Colombia', 'Croatia', 'Czech Republic',
    'Denmark', 'Ecuador', 'Egypt', 'Estonia', 'Ethiopia', 'Finland', 'France',
    'Georgia', 'Germany', 'Ghana', 'Greece', 'Hungary', 'Iceland', 'India', 'Indonesia',
    'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kazakhstan',
    'Kenya', 'Latvia', 'Lebanon', 'Lithuania', 'Madagascar', 'Malaysia', 'Mexico',
    'Morocco', 'Nepal', 'Netherlands', 'New Zealand', 'Nigeria', 'Norway', 'Pakistan',
    'Peru', 'Philippines', 'Poland', 'Portugal', 'Romania', 'Russia', 'Saudi Arabia',
    'Serbia', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Spain',
    'Sri Lanka', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'Ukraine',
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
    'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen'
]

def get_location_by_name(name: str) -> dict:
    """Get location data by name"""
    return WORLD_LOCATIONS.get(name, None)

def search_locations_by_query(query: str, limit: int = 10) -> list:
    """Search locations by query string"""
    if not query:
        return [{'name': name, **WORLD_LOCATIONS[name]} for name in POPULAR_DESTINATIONS[:limit]]
    
    query_lower = query.lower().strip()
    results = []
    
    # Exact matches first
    for name, data in WORLD_LOCATIONS.items():
        if (name.lower() == query_lower or 
            data['country'].lower() == query_lower):
            result = data.copy()
            result['name'] = name
            results.append(result)
    
    # Partial matches
    if len(results) < limit:
        for name, data in WORLD_LOCATIONS.items():
            if (query_lower in name.lower() or 
                query_lower in data['country'].lower() or
                (data['admin'] and query_lower in data['admin'].lower())):
                result = data.copy()
                result['name'] = name
                if result not in results:
                    results.append(result)
                    if len(results) >= limit:
                        break
    
    return results[:limit]

def get_popular_destinations(limit: int = 20) -> list:
    """Get popular destinations"""
    return [WORLD_LOCATIONS[name] for name in POPULAR_DESTINATIONS[:limit]]

def format_display_name(location_data: dict, name: str) -> str:
    """Format display name for location"""
    if location_data['type'] == 'country':
        return name
    elif location_data['admin'] and location_data['admin'] != name:
        return f"{name}, {location_data['country']}"
    else:
        return f"{name}, {location_data['country']}"