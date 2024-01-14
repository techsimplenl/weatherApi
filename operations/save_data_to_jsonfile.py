"""Save file into json, csv"""
import json
from Entity.Weather import WeatherEntity
import matplotlib.pyplot as plt

def load_json():
    """LOAD DATA FROM JSON FILE"""
    try:
        with open('json_file.json','r',encoding="utf-8") as fp:
            data = json.load(fp)
        return data
    except FileNotFoundError:
        return None

def save_data_into_json_file():
    """Save data into json file"""
    weather = WeatherEntity
    mydict = {
        'country': weather.country,
        'current': weather.current,
        'time': weather.time,
        'forecast': weather.forecast
    }
    # specifying the json file path and name
    json_file = 'json_file.json'
    # Write data to json file
    with open(json_file, 'w',encoding="utf-8" )as file:
        json.dump(mydict,file)
        print(f'Data has been saved to {json_file}')

def save_data_into_csv_file():
    """Save data into CSV file"""
