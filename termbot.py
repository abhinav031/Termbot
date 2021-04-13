# TermBot

# Imports
from scripts.apod import apod
from scripts.calc import calc
from scripts.convert import convert
from scripts.iss import iss
from scripts.quote import quote
from scripts.rps import rps
from scripts.scramble import start
from scripts.sysinfo import info
from scripts.timestuff import countdown
from scripts.weather import weather

# Welcome message

print("Welcome to TermBot!")

# The thing that runs


def bot():
    cmd = input(
        'Enter a command. (Use command "help" for a list of commands): ')
    command = cmd.lower()

    if command == "help":  # Help Me!!!
        print(
            "Hello! This is a simple terminal based python script. " +
            "\nMath:" +
            "\n     calc - A simple, two number calculator" +
            "\n     convert - Convert Kilograms to Pounds and vice-versa" +
            "\nSpace:" +
            "\n     iss - live ISS tracker" +
            "\n     apod - NASA Astronomy Picture Of the Day"
            "\nWeather:" +
            "\n     weather - Get weather info of a city" +
            "\nTime:" +
            "\n     countdown - Simple countdown" +
            "\nFun:"
            "\n     scramble - Generates a 3x3 Rubik's cube scramble. Also functions as a timer" +
            "\n     sysinfo - Gives info about system" +
            "\n     rps - Rock Paper Scissors" +
            "\n     inspire - Tells an inspirational quote"
            "\nOther:"
            "\n     help - Lists all available commands" +
            "\n     exit - Exit TermBot")

    elif command == "calc":  # (a very bad) Calculator
        calc()

    elif command == "convert":  # Weight Converter
        convert()

    elif command == "weather":  # Weather
        weather()

    elif command == "countdown":  # T-10, 9, 8...
        countdown()

    elif command == "scramble":  # Rubik's cube Scrambler (3x3)
        start()

    elif command == "rps":   # Rock Paper Sissor
        rps()

    elif command == "sysinfo":   # System Info
        info()

    elif command == "iss":      # ISS Tracker
        iss()

    elif command == "apod":     # APOD
        apod()

    elif command == "inspire":      # Inspirational Quote
        quote()

    elif command == "exit":  # Exit the script
        exit()

    else:       # Incase theres no such command
        print("Command not found!")


while True:  # Loop
    bot()
