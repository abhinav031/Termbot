# Imports
import requests
import json


def iss():
    print("Welcome to ISS tracker!")
    response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    e = response.json()
    lat = str(e["latitude"])
    long = str(e["longitude"])
    alt = str(e["altitude"])

    print(
        "Latitude = " + lat +
        "\nLongitude = " + long +
        "\nAltitude = " + alt
    )
