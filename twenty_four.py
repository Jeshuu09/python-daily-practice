# Weather Information App

import requests

def get_weather(latitude, longitude, city):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()
        weather = data["current"]

        print("\n===== WEATHER REPORT =====")
        print("City:", city)
        print("Temperature:", weather["temperature_2m"], "°C")
        print("Feels Like:", weather["apparent_temperature"], "°C")
        print("Humidity:", weather["relative_humidity_2m"], "%")
        print("Wind Speed:", weather["wind_speed_10m"], "km/h")

    except requests.exceptions.RequestException:
        print("Unable to connect to the weather service.")

    except (KeyError, ValueError):
        print("Unable to process weather information.")


print("===== WEATHER APP =====")

city = input("Enter city name: ").strip().lower()

locations = {
    "vijayawada": (16.5062, 80.6480),
    "hyderabad": (17.3850, 78.4867),
    "chennai": (13.0827, 80.2707),
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946)
}

if city in locations:
    latitude, longitude = locations[city]
    get_weather(latitude, longitude, city.title())
else:
    print("City not available in the application.")
