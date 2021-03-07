# TermBot
from calc import calc
from convert import convert
from weather import weather
from timestuff import countdown
from scramble import start
from rps import rps
from sysinfo import info

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
            "\ncountdown - Simple countdown" +
            "\nscramble - Generates a 3x3 Rubik's cube scramble. Also functions as a timer" +
            "\nsysinfo - Gives info about system" +
            "\nrps - Rock Paper Scissors"
            "\nhelp - Lists all available commands" +
            "\nexit - Exit TermBot")

    elif command == "calc":  # (a very bad) Calculator
        calc()

    elif command == "convert":  # Weight Converter
        convert()

    elif command == "weather":  # Weather
        weather()

    elif command == "countdown":  # T-10, 9, 8...
        countdown()

    elif command == "scramble":  # Rubik's cube go brrr
        start()

    elif command == "rps":   # Rock Paper Sissor?
        rps()

    elif command == "sysinfo":   # Haha system info go brrrrr
        info()

    elif command == "exit":  # I need to get out
        exit()

    else:
        print("Command not found!")


while True:  # Loop
    bot()
