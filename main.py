"""RUN main.py"""
import os
import matplotlib
from operations.operations import Operations
from dotenv import load_dotenv
matplotlib.use('TkAgg')  # Use the TkAgg backend
load_dotenv()

def app():
    """Get input and make the call to the operation"""
    print("WELCOME TO THE WEATHER STATION")
    days = input('Enter number of days between 1 - 14: ')
    location = input("Enter the Latitude and Longitude(eg: 37.9087,0.664874):" )
    if len(days.strip()) <= 0:
        print('Please Enter the number of days')
        days = input('Enter number of days between 1 - 14: ')
    if len(location.strip()) <= 0:
        print('Please Enter the location')
        location = input("Enter the Latitude and Longitude(eg: 37.9087,0.664874):" )
    uri = "https://api.weatherapi.com/v1/forecast.json"
    api_key = os.environ.get('API-KEY') #here
    params = {"key": api_key,"q":location,'days':days}
    args={'url':uri,'params':params}
    Operations(args).presenting_data_with_matplot()

if __name__ == "__main__":
    # run main function
    app()


# castalla 38.5934° N, 0.6725° W
# arnhem 51.9851,5.8987