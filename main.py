from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
API_KEY = os.getenv("API_KEY")
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None

    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)

    return render_template('index.html', weather_data=weather_data)


def get_weather_data(city):
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return weather

    return None


if __name__ == '__main__':
    app.run(debug=True)
