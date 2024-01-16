"""Run main.py"""
import os
import matplotlib
from operations.operations import Operations
from dotenv import load_dotenv
matplotlib.use('TkAgg')  # Use the TkAgg backend
load_dotenv()

def get_user_choice():
    """Get user choice from input."""
    while True:
        try:
            location = str(input('Enter the Latitude and Longitude(eg: 37.9087,0.664874) or name of the town (eg: Paris): '))
            print('Choose option to display the temperature: ')
            print("1. Today")
            print("2. One week")
            print("3. Two Weeks")
            option = int(input("Choose an operation (1-3):\n"))
            if len(location.strip()) <= 0:
                print('Please Enter the location')
            if 1 <= option <= 3:
                mydict = {
                    'location': location,
                    'choice': option
                }
                return mydict
            print('Invalid choice. Please enter a number between 1 and 3')
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def user_input():
    """Get input from the user."""
    user_choice = get_user_choice()
    api_key = os.environ.get('API-KEY') #here
    choice = user_choice['choice']
    location = user_choice['location']
    # Perform actions based on the user's choice
    if choice in (1,2,3):
        # do the operation
        number_of_days = 0
        if choice == 1:
            number_of_days = 1
        elif choice == 2:
            number_of_days = 7
        else:
            number_of_days = 14
        params = {"key": api_key,"q":location,'days':number_of_days}
        return params
    print("Invalid choice. Please choose a valid option")
    return None
def app():
    """Get input and make the call to the operation"""
    print("WELCOME TO THE WEATHER STATION")
    params = user_input()
    uri = "https://api.weatherapi.com/v1/forecast.json"
    args={'url':uri,'params':params}
    Operations(args).presenting_data_with_matplot()
if __name__ == "__main__":
    # run main function
    app()

# castalla 38.5934° N, 0.6725° W
# arnhem 51.9851,5.8987
