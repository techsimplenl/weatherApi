"""ENTITY OF THE WEATHER OBJECT"""
import dataclasses
@dataclasses.dataclass
class WeatherEntity:
    """Class representing Weather"""
    country: dict
    current: dict
    time: str
    forecast: dict   
    def assign_location(self,details):
        """Assigninh variables from location"""
        self.country = {
            'name': details['country'],
            'city': details['name'],
            'region':details['region']
        }
        self.time = details['localtime']
    def assign_current(self,details):
        """Assign variables from current."""
        self.current = {
            'current_temp_c': details['temp_c'],
            'current_temp_f': details['temp_f'],
            'last_updated': details['last_updated'],
            'wind_dir': details['wind_dir'],
            'pressure_mb': details['pressure_mb'],
            'pressure_in': details['pressure_in'],
            'cloud': details['cloud'],
            'gust_mph': details['gust_mph'],
            'gust_kph': details['gust_kph'],
            'humidity': details['humidity']
        }
    def assign_forecast(self,details):
        """Assign variables from forecast."""
        self.forecast = details['forecastday']
 