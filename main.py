"""RUN THIS FILE BY python main.py"""
import os
import matplotlib
from operations.operations import Operations
from dotenv import load_dotenv
matplotlib.use('TkAgg')  # Use the TkAgg backend
load_dotenv()
if __name__ == "__main__":
    # data = py() # run main function
    URI = "https://api.weatherapi.com/v1/forecast.json"
    api_key = os.environ.get('API-KEY') #here
    params = {"key": api_key,"q":'38.5934,0.6725','days':1}
    args={'url':URI,'params':params}
    Operations(args).presenting_data_with_matplot()