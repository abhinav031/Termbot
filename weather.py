# Imports
import requests
import json
import os
from dotenv import load_dotenv

# DotEnv location
path = '/home/abhi/Documents/Programming/Python/!.env'      # change dis
load_dotenv(dotenv_path=path, verbose=True)


def weather():
    print("Welcome to Weather!")\

    api_key = os.getenv("API")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name : ")
    units = "units=metric"
    complete_url = base_url + "appid=" + api_key + \
        "&q=" + city_name.lower() + "&" + units
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":

        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        feels_like = y["feels_like"]
        max_temp = y["temp_max"]
        min_temp = y["temp_min"]

        z = x["weather"]

        weather_description = z[0]["description"]

    print("Weather in " + city_name.capitalize() + " :"
          "\nTemperature: " + str(current_temperature) + "°C" +
          "\n Feels Like : " + str(feels_like) + "°C"
          "\n Max: " + str(max_temp) + "°C" +
          "\n Min : " + str(min_temp) + "°C" +
          "\n Pressure:  " + str(current_pressure) + "mB" +
          "\n Humidity: " + str(current_humidiy) + "%" +
          "\n description = " + str(weather_description))
