"""RUN THIS FILE BY python main.py"""
import matplotlib
from Entity.Weather import WeatherEntity
from private.request import GetApiFromWeather
from operations.operations import Operations
from operations.save_data_to_jsonfile import resenting_data_with_matplot

matplotlib.use('TkAgg')  # Use the TkAgg backend

def reutrn_data_to_save(weather:WeatherEntity):
    """data to save""" 
    return weather.__dict__
# set the entity values
def retrieve_important_forecast(data_: any,weather: any):
    """Class representing Weather"""
    # Iterating through the outer dictionary
    for item, details in data_.items():
        if 'location' == item:
            weather.country = {
                'name':details['country'],
                'city':details['name'],
                'region':details['region'],
            }
            weather.time = details['localtime']   
        if 'current' == item:
            weather.current = {
                'current_temp_c': details['temp_c'],
                'current_temp_f': details['temp_f'],
                'last_updated': details['last_updated'],
                'wind_dir': details['wind_dir'],
                'pressure_mb': details['pressure_mb'],
                'pressure_in': details['pressure_in'],
                'cloud': details['cloud'],
                'gust_mph': details['gust_mph'],
                'gust_kph': details['gust_kph'],
                }
            weather.humidity = details['humidity']
            # weather.city = details['name']
        if 'forecast' == item:
            weather.forecast = details['forecastday']
def py():
    """All variables and functions here"""
    base_url = 'https://api.weatherapi.com/v1'
    url = base_url +"/forecast.json"
    api_key = '66c7c4d9d45644d685c182344241201'
    params = {"key": api_key,"q":'38.5934,0.6725','days':5}
    result = GetApiFromWeather(url,params).get_api_data()
    if result:
        # here we have to save this data in files
        return result
    return None
# Check if this script is being run as the main program
if __name__ == "__main__":
    data = py() # run main function
    Operations.retrieve_important_forecast(data_=data,weather=WeatherEntity)
    # save_data_into_json_file()
    resenting_data_with_matplot()
