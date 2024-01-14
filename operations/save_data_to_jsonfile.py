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
def  resenting_data_with_matplot():
    """RESETING THE LIST OF WEATHER ENTITIES AND CALL"""
    data = WeatherEntity
    forecast = data.forecast
    list_days = []
    list_max_temp_c = []
    
    for index,item in enumerate(forecast):
        list_days.append(item['date'])
        list_max_temp_c.append(item['day']['maxtemp_c'])
    #operation for representing a plotlib
    plt.plot(list_max_temp_c,list_days, label='Linear Function')
    # Add labels and a title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Matplotlib Example')
    # Add a legend
    plt.legend()
    plt.show()
    plt.savefig('my_plot.png')
    # Display the plot
    # plt.show()
    
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
