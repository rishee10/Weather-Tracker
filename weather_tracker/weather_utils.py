# weather_utils.py

import requests
from weather_module import Weather

# Replace with your WeatherAPI.com key
API_KEY = "96a34633665d4ff4b4a91753250109"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def fetch_weather(city: str) -> Weather:
    """
    Fetch weather data for a city from WeatherAPI.com.
    Returns a Weather object.
    Handles invalid city names or API errors gracefully.
    """
    try:
        response = requests.get(BASE_URL, params={"key": API_KEY, "q": city})
        response.raise_for_status()
        data = response.json()

        # Extract needed fields
        city_name = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]
        last_updated = data["current"]["last_updated"]

        return Weather(city_name, temp_c, condition, humidity, wind_kph, last_updated)

    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching {city}: {e}")
    except KeyError:
        print(f"Invalid response for {city}. Check city name or API key.")
    return None
