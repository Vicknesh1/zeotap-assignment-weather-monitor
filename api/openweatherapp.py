import requests
from config import API_KEY, CITIES

class OpenWeatherMapAPI:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_weather(city):
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(OpenWeatherMapAPI.BASE_URL, params=params)
        return response.json()

    @staticmethod
    def get_weather_for_cities():
        return {city: OpenWeatherMapAPI.get_weather(city) for city in CITIES}
