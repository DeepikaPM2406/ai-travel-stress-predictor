"""
Travel Comfort Calculator - FIXED SCORING SYSTEM
Provides positive framing for travel planning calculations
"""

from typing import Tuple, Dict, Optional
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

class TravelComfortCalculator:
    """Calculate travel comfort scores with positive framing and FIXED scoring"""

    def __init__(self):
        self.factor_weights = {
            'baby_age_comfort': 3.0,
            'flight_comfort': 3.0,
            'logistical_ease': 2.0,
            'timing_convenience': 2.0,
            'support_system': 2.0,
            'medical_preparedness': 1.0,
            'experience_advantage': 2.0,
            'destination_friendliness': 1.0,
            'trip_duration_comfort': 2.0
        }

    def calculate_travel_comfort(
        self, baby_age: int, flight_hours: float, layovers: int, departure_time: str,
        has_partner: bool, special_needs: bool, pumping_needed: bool, 
        first_international: bool, parent_experience: str, destination: Destination,
        departure_location: Optional[Destination] = None, trip_duration: int = 5
    ) -> Tuple[int, dict]:
        comfort_factors = {
            'baby_age_comfort': self._calculate_baby_age_comfort(baby_age),
            'flight_comfort': self._calculate_flight_comfort(flight_hours, layovers),
            'logistical_ease': self._calculate_logistics_comfort(pumping_needed, first_international),
            'timing_convenience': self._calculate_timing_comfort(departure_time),
            'support_system': self._calculate_support_comfort(has_partner),
            'medical_preparedness': self._calculate_medical_comfort(special_needs),
            'experience_advantage': self._calculate_experience_comfort(parent_experience),
            'destination_friendliness': self._calculate_destination_comfort(destination),
            'trip_duration_comfort': self._calculate_duration_comfort(trip_duration)
        }

        total_comfort = sum(comfort_factors.values())
        max_possible = sum(self.factor_weights.values())
        comfort_score = max(1, min(10, round((total_comfort / max_possible) * 10)))

        return comfort_score, comfort_factors

    def _calculate_baby_age_comfort(self, baby_age: int) -> float:
        """FIXED: Now properly respects weight limits"""
        if baby_age <= 3:
            normalized = 0.83  # 0.83 * 3 = 2.5 (same as before)
        elif baby_age <= 6:
            normalized = 1.0   # 1.0 * 3 = 3.0 (same as before)
        elif baby_age <= 11:
            normalized = 0.33  # 0.33 * 3 = 1.0 (same as before)
        elif baby_age <= 18:
            normalized = 0.5   # 0.5 * 3 = 1.5 (same as before)
        else:
            normalized = 0.83  # 0.83 * 3 = 2.5 (same as before)
        
        return normalized * self.factor_weights['baby_age_comfort']

    def _calculate_flight_comfort(self, flight_hours: float, layovers: int) -> float:
        """FIXED: Now properly respects weight limits - was the main problem!"""
        # Duration comfort (0-1 scale)
        if flight_hours <= 3:
            duration_comfort = 1.0
        elif flight_hours <= 6:
            duration_comfort = 0.83  # was 2.5, now 0.83 * 3 = 2.5
        elif flight_hours <= 10:
            duration_comfort = 0.5   # was 1.5, now 0.5 * 3 = 1.5
        else:
            duration_comfort = 0.17  # was 0.5, now 0.17 * 3 = 0.5
        
        # Layover comfort (0-1 scale)
        if layovers == 0:
            layover_comfort = 0.67   # was 2.0, now 0.67 * 3 = 2.0
        elif layovers == 1:
            layover_comfort = 0.33   # was 1.0, now 0.33 * 3 = 1.0
        else:
            layover_comfort = 0.0
        
        # Combined comfort (weighted average, then scale to weight)
        combined_comfort = (duration_comfort * 0.7) + (layover_comfort * 0.3)
        return combined_comfort * self.factor_weights['flight_comfort']

    def _calculate_timing_comfort(self, departure_time: str) -> float:
        """FIXED: Now properly respects weight limits"""
        timing_scores = {
            "Morning (7-11 AM)": 1.0,     # 1.0 * 2 = 2.0 (same as before)
            "Evening (5-10 PM)": 1.0,     # 1.0 * 2 = 2.0 (same as before)  
            "Afternoon (11 AM-5 PM)": 0.75, # 0.75 * 2 = 1.5 (same as before)
            "Late Night (10 PM-12 AM)": 0.5, # 0.5 * 2 = 1.0 (same as before)
            "Very Early (5-7 AM)": 0.25,  # 0.25 * 2 = 0.5 (same as before)
            "Red-eye (12-5 AM)": 0.0      # 0.0 * 2 = 0.0 (same as before)
        }
        normalized = timing_scores.get(departure_time, 0.5)
        return normalized * self.factor_weights['timing_convenience']

    def _calculate_duration_comfort(self, trip_duration: int) -> float:
        """FIXED: Now properly respects weight limits"""
        if trip_duration <= 3:
            normalized = 1.0   # 1.0 * 2 = 2.0 (same as before)
        elif trip_duration <= 7:
            normalized = 0.75  # 0.75 * 2 = 1.5 (same as before)
        elif trip_duration <= 14:
            normalized = 0.5   # 0.5 * 2 = 1.0 (same as before)
        else:
            normalized = 0.25  # 0.25 * 2 = 0.5 (same as before)
        
        return normalized * self.factor_weights['trip_duration_comfort']

    def _calculate_support_comfort(self, has_partner: bool) -> float:
        """FIXED: Now properly respects weight limits"""
        normalized = 1.0 if has_partner else 0.25  # 1.0*2=2.0 or 0.25*2=0.5
        return normalized * self.factor_weights['support_system']

    def _calculate_medical_comfort(self, special_needs: bool) -> float:
        """FIXED: Now properly respects weight limits"""
        normalized = 0.5 if special_needs else 1.0  # 0.5*1=0.5 or 1.0*1=1.0
        return normalized * self.factor_weights['medical_preparedness']

    def _calculate_logistics_comfort(self, pumping_needed: bool, first_international: bool) -> float:
        """FIXED: Now properly respects weight limits"""
        comfort = 1.0
        if pumping_needed:
            comfort -= 0.25
        if first_international:
            comfort -= 0.25
        normalized = max(0, comfort)
        return normalized * self.factor_weights['logistical_ease']

    def _calculate_experience_comfort(self, parent_experience: str) -> float:
        """FIXED: Now properly respects weight limits"""
        experience_scores = {
            "Travel veteran (10+ flights)": 1.0,     # 1.0 * 2 = 2.0 (same)
            "Experienced traveler (4+ flights)": 0.75, # 0.75 * 2 = 1.5 (same)
            "2-3 previous flights": 0.5,             # 0.5 * 2 = 1.0 (same)
            "First time flying with baby": 0.25      # 0.25 * 2 = 0.5 (same)
        }
        normalized = experience_scores.get(parent_experience, 0.5)
        return normalized * self.factor_weights['experience_advantage']

    def _calculate_destination_comfort(self, destination: Destination) -> float:
        """FIXED: Now properly respects weight limits"""
        excellent = ['Dubai', 'Singapore', 'Tokyo', 'London', 'Sydney', 'Barcelona', 'Amsterdam', 'Copenhagen', 'Reykjavik', 'Paris']
        good = ['New York', 'Los Angeles', 'Rome', 'Berlin', 'Madrid', 'Istanbul', 'Mumbai', 'Delhi', 'Hyderabad', 'Bangkok']
        
        if destination.name in excellent:
            normalized = 1.0   # 1.0 * 1 = 1.0 (same as before)
        elif destination.name in good:
            normalized = 0.7   # 0.7 * 1 = 0.7 (same as before)
        else:
            normalized = 0.5   # 0.5 * 1 = 0.5 (same as before)
        
        return normalized * self.factor_weights['destination_friendliness']

    def get_comfort_insights(self, comfort_score: int, factors: Dict) -> Dict[str, str]:
        insights = {
            'overall_assessment': '',
            'top_strengths': [],
            'areas_for_improvement': [],
            'recommendations': []
        }
        if comfort_score >= 8:
            insights['overall_assessment'] = "Excellent comfort level - this trip is well-suited for traveling with a baby!"
        elif comfort_score >= 6:
            insights['overall_assessment'] = "Good comfort level - with proper preparation, this should be a pleasant trip."
        elif comfort_score >= 4:
            insights['overall_assessment'] = "Moderate comfort level - some planning adjustments could improve the experience."
        else:
            insights['overall_assessment'] = "Lower comfort level - consider modifications or extensive preparation."

        sorted_factors = sorted(factors.items(), key=lambda x: x[1], reverse=True)
        
        # Calculate which factors are strong vs weak based on their percentage of max possible
        insights['top_strengths'] = []
        insights['areas_for_improvement'] = []
        
        for factor, value in sorted_factors:
            max_for_factor = self.factor_weights[factor]
            percentage = value / max_for_factor
            readable_name = self._factor_to_readable(factor)
            
            if percentage >= 0.75:
                insights['top_strengths'].append(readable_name)
            elif percentage < 0.5:
                insights['areas_for_improvement'].append(readable_name)
        
        # Limit to top 3 of each
        insights['top_strengths'] = insights['top_strengths'][:3]
        insights['areas_for_improvement'] = insights['areas_for_improvement'][-3:]

        return insights

    def _factor_to_readable(self, factor: str) -> str:
        readable = {
            'baby_age_comfort': 'Baby age suitability',
            'flight_comfort': 'Flight convenience',
            'logistical_ease': 'Travel logistics',
            'timing_convenience': 'Departure timing',
            'support_system': 'Support system',
            'medical_preparedness': 'Medical considerations',
            'experience_advantage': 'Travel experience',
            'destination_friendliness': 'Destination suitability',
            'trip_duration_comfort': 'Trip length appropriateness'
        }
        return readable.get(factor, factor.replace('_', ' ').title())

class WeatherComfortService:
    @staticmethod
    def get_weather_comfort_info(destination: Destination) -> Dict[str, str]:
        climate_data = {
            'Dubai': {'temp': '35-40°C', 'climate': 'Hot & Humid', 'season': 'Year-round heat', 'comfort': 'Stay hydrated, use AC'},
            'Hyderabad': {'temp': '25-35°C', 'climate': 'Tropical', 'season': 'Hot, monsoon season', 'comfort': 'Light clothing recommended'},
            'Mumbai': {'temp': '25-32°C', 'climate': 'Tropical', 'season': 'Hot & humid', 'comfort': 'Breathable fabrics essential'},
            'Singapore': {'temp': '25-32°C', 'climate': 'Tropical', 'season': 'Consistently warm', 'comfort': 'Excellent AC everywhere'},
            'Stockholm': {'temp': '0-20°C', 'climate': 'Continental', 'season': 'Cold winters', 'comfort': 'Layer clothing, heated indoors'},
            'Reykjavik': {'temp': '0-15°C', 'climate': 'Oceanic', 'season': 'Cool year-round', 'comfort': 'Warm clothing needed'},
            'Copenhagen': {'temp': '2-22°C', 'climate': 'Oceanic', 'season': 'Mild but cool', 'comfort': 'Layers recommended'},
            'London': {'temp': '5-22°C', 'climate': 'Oceanic', 'season': 'Mild, rainy', 'comfort': 'Excellent for families'},
            'Paris': {'temp': '3-25°C', 'climate': 'Oceanic', 'season': 'Mild seasons', 'comfort': 'Generally comfortable'},
            'Tokyo': {'temp': '5-30°C', 'climate': 'Humid subtropical', 'season': 'Four distinct seasons', 'comfort': 'Varies by season'},
            'Sydney': {'temp': '10-25°C', 'climate': 'Oceanic', 'season': 'Mild year-round', 'comfort': 'Ideal for families'}
        }
        return climate_data.get(destination.name, {
            'temp': '15-25°C', 'climate': 'Temperate', 'season': 'Variable', 'comfort': 'Generally moderate'
        })


# Test the fixed scoring system
if __name__ == "__main__":
    # Create test destination
    test_dest = Destination(
        name="London",
        country="United Kingdom", 
        admin="England",
        population=9000000,
        type="capital",
        display="London (LHR), United Kingdom"
    )
    
    calculator = TravelComfortCalculator()
    
    # Test scenario: 6-month baby, moderate flight, good support
    comfort_score, factors = calculator.calculate_travel_comfort(
        baby_age=6,
        flight_hours=7,
        layovers=1,
        departure_time="Morning (7-11 AM)",
        has_partner=True,
        special_needs=False,
        pumping_needed=True,
        first_international=False,
        parent_experience="Experienced traveler (4+ flights)",
        destination=test_dest,
        trip_duration=5
    )
    
    print(f"Comfort Score: {comfort_score}/10")
    print(f"Total: {sum(factors.values()):.1f}/{sum(calculator.factor_weights.values())}")
    print(f"Percentage: {(sum(factors.values())/sum(calculator.factor_weights.values()))*100:.1f}%")
    
    print("\nFactor Breakdown:")
    for factor, score in factors.items():
        weight = calculator.factor_weights[factor]
        percentage = (score/weight)*100
        print(f"  {factor}: {score:.2f}/{weight} ({percentage:.0f}%)")
    
    print("\n✅ SCORING SYSTEM FIXED!")
    print("✅ All factors now respect their weight limits")
    print("✅ Realistic scores that range from 1-10 properly")