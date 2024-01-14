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
def design_plot_with_matlib(**kwargs):
    """Plot for represententing the temperature trends per day in your region"""
    # Convert dates to numerical values for plotting
    numeric_dates = range(len(kwargs['list_dates']))
    #Plotting the data
    plt.plot(numeric_dates, kwargs['list_max_temp_c'], label='Max Temperature', marker='o')
    plt.plot(numeric_dates, kwargs['list_min_temp'], label='Min Temperature', marker='o')
    plt.plot(numeric_dates, kwargs['list_average_temp'], label='Average Temperature', marker='o')
    #Adding labels and tittle
    plt.xlabel("Dates")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature trends from : {kwargs['city']} - {kwargs['name']}")
    plt.xticks(numeric_dates,kwargs['list_dates']) # Use actual dates as x-axis labels
    plt.legend() # Display legend
    # plt.savefig('my_plot.png')
    # Display the plot
    plt.show()
def  resenting_data_with_matplot():
    """RESETING THE LIST OF WEATHER ENTITIES AND CALL"""
    data = WeatherEntity
    forecast = data.forecast
    list_dates = []
    list_average_temp = []
    list_min_temp = []
    list_max_temp_c = []
    for index,item in enumerate(forecast):
        list_dates.append(item['date'])
        list_max_temp_c.append(item['day']['maxtemp_c'])
        list_average_temp.append(item['day']['avgtemp_c'])
        list_min_temp.append(item['day']['mintemp_c'])
    design_plot_with_matlib(kwargs={
        'list_days':list_dates,
        'list_average_temp':list_average_temp,
        'list_min_temp':list_min_temp,
        'list_max_temp_c':list_max_temp_c,
        'city': data.country['city'],
        'name': data.country['name']      
    })
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
