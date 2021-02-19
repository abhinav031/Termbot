# TermBot

# Imports
import requests
import json
import os
import time
from dotenv import load_dotenv

# DotEnv location
path = '/home/abhi/Documents/Programming/Python/!.env'
load_dotenv(dotenv_path=path, verbose=True)

# Welcome message

print("Welcome to TermBot!")

# The thing that runs


def bot():
    cmd = input(
        'Enter a command. (Use command "help" for a list of commands): ')
    command = cmd.lower()

    if command == "help":  # Help Me!!!
        print(
            "calc - A simple, two number calculator" +
            "\nconvert - Convert Kilograms to Pounds and vice-versa" +
            "\nweather - Get weather info of a city" +
            "\nhelp - Lists all available commands" +
            "\ncountdown - Simple countdown" +
            "\nexit - Exit TermBot")

    elif command == "calc":  # (a very bad) Calculator
        print("Welcome to calculator!")
        first = float(input("First Number: "))
        second = float(input("Second Number: "))
        oper = input(
            "Enter an operator (sum, diff, prod, quo, exp, mod) ")
        if(oper == "sum"):
            answer = first + second
            print(answer)
        if(oper == "diff"):
            answer = first - second
            print(answer)
        if(oper == "prod"):
            answer = first * second
            print(answer)
        if(oper == "quo"):
            answer = first / second
            print(answer)
        if(oper == "exp"):
            answer = first ** second
            print(answer)
        if(oper == "mod"):
            answer = first % second
            print(answer)

    elif command == "convert":  # Weight Converter
        print("Welcome to weight converter!")
        weight = float(input("Enter weight (number only): "))
        unit = input("Enter unit to convert to [(K)g or (L)bs]: ")

        if unit.lower() == "k":
            conv = weight / 2.205
            print(str(weight) + " Pounds is " + str(conv) + " Kilograms")
        elif unit.lower() == "l":
            conv = weight * 2.205
            print(str(weight) + " Kilograms is " + str(conv) + " Pounds")

    elif command == "weather":  # Weather
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

        print("Weather in " + city_name.-capitalize() + " :"
              "\nTemperature: " + str(current_temperature) + "°C" +
              "\n Feels Like : " + str(feels_like) + "°C"
              "\n Max: " + str(max_temp) + "°C" +
              "\n Min : " + str(min_temp) + "°C" +
              "\n Pressure:  " + str(current_pressure) + "mB" +
              "\n Humidity: " + str(current_humidiy) + "%" +
              "\n description = " + str(weather_description))

    elif command == "countdown":  # T-10, 9, 8...
        print("Welcome to timer!")

        def countdown(t):

            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1

            print('Yeet!')

        t = input("Enter the time in seconds: ")

        countdown(int(t))

    elif command == "exit":  # I need to get out
        exit()


while True:  # Loop
    bot()
