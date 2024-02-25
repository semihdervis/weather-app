from dotenv import load_dotenv
import os
import requests
import json

# Load variables from .env file
load_dotenv()

# Access api key in .env
api_key = os.getenv("API_KEY")

icon_mapping = {
    '01d': '☀️',  # clear sky day
    '02d': '⛅',  # few clouds day
    '03d': '☁️',  # scattered clouds day
    '04d': '☁️',  # broken clouds day
    '09d': '🌧️',  # shower rain day
    '10d': '🌦️',  # rain day
    '11d': '⛈️',  # thunderstorm day
    '13d': '❄️',  # snow day
    '50d': '🌫️',  # mist day
    # Add night variants if needed
}

def get_weather(api_key, city):
    # OpenWeather API endpoint
    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    # Make the API request
    response = requests.get(endpoint, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()

        # Print relevant weather information
        print(f"Weather in {city}, {data['sys']['country']}, {data['weather'][0]['icon']}, {icon_mapping.get(data['weather'][0]['icon'], '❓')}:")  # Add country information
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")

if __name__ == "__main__":
    city = 'Istanbul'  # Replace with the name of the city you want to get the weather for

    get_weather(api_key, city)
