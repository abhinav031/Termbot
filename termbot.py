# TermBot

# Imports
from calc import calc
from convert import convert
from weather import weather
from timestuff import countdown
from scramble import start
from rps import rps
from sysinfo import info
from iss import iss


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
            "\nWeather:" +
            "\n     weather - Get weather info of a city" +
            "\nTime:" +
            "\n     countdown - Simple countdown" +
            "\nFun:"
            "\n     scramble - Generates a 3x3 Rubik's cube scramble. Also functions as a timer" +
            "\n     sysinfo - Gives info about system" +
            "\n     rps - Rock Paper Scissors" +
            "\n     iss - live ISS tracker"
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

    elif command == "exit":  # Exit the script
        exit()

    else:       # Incase theres no such command
        print("Command not found!")


while True:  # Loop
    bot()
