"""Operation program"""
from private.request import GetApiFromWeather
from Entity.Weather import WeatherEntity
import matplotlib.pyplot as plt
class Operations:
    """All operations"""
    def __init__(self, args):
        self.__url = args['url']
        self.__params = args['params']
        self.__weather = WeatherEntity
    
    def get_data_from_api(self):
        """Retrieve Data from API."""
        result = GetApiFromWeather(self.__url,self.__params).get_api_data()
        if result:
        # here we have to save this data in files
            return result
        return None

    def retrieve_important_forecast(self):
        """Retrieve important forecast information from the given data."""
        data_ = self.get_data_from_api()
        for item, details in data_.items():
            if 'location' == item:
                self.__weather.assign_location(self.__weather,details)
            if 'current' == item:
                self.__weather.assign_current(self.__weather,details)
            if 'forecast' == item:
                self.__weather.assign_forecast(self.__weather,details)

    def design_plot_with_matlib(self,**kwargs):
        """Plot for represententing the temperature trends per day in your region"""
        # Convert dates to numerical values for plotting
        print(kwargs)
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
        # Display the plot
        plt.show()

    def  presenting_data_with_matplot(self):
        """RESETING THE LIST OF WEATHER ENTITIES AND CALL"""
        self.retrieve_important_forecast()
        forecast = self.__weather.forecast
        list_dates = []
        list_average_temp = []
        list_min_temp = []
        list_max_temp_c = []
        for index,item in enumerate(forecast):
            list_dates.append(item['date'])
            list_max_temp_c.append(item['day']['maxtemp_c'])
            list_average_temp.append(item['day']['avgtemp_c'])
            list_min_temp.append(item['day']['mintemp_c'])
        kwargs = {
            'list_dates':list_dates,
            'list_average_temp':list_average_temp,
            'list_min_temp':list_min_temp,
            'list_max_temp_c':list_max_temp_c,
            'city': self.__weather.country['city'],
            'name': self.__weather.country['name'] 
        }
        self.design_plot_with_matlib(**kwargs)
