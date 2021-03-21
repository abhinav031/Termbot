# Imports
import requests
import json
import webbrowser
import os
import dotenv


def apod():
    print("Welcome to APOD!")
    response = requests.get(
        'https://api.nasa.gov/planetary/apod?api_key=' + os.getenv("NASA_API"))

    e = response.json()

    webbrowser.open(e["hdurl"])
    print(e["explanation"])
