import pytest
from unittest.mock import patch, Mock
from src.api.openweathermap import OpenWeatherMapAPI
from config import CITIES

@pytest.fixture
def mock_response():
    return {
        "main": {"temp": 25.5},
        "weather": [{"main": "Clear"}]
    }

def test_get_weather(mock_response):
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_response
        weather = OpenWeatherMapAPI.get_weather('Delhi')
        assert weather == mock_response
        mock_get.assert_called_once()

def test_get_weather_for_cities(mock_response):
    with patch('src.api.openweathermap.OpenWeatherMapAPI.get_weather', return_value=mock_response):
        weather_data = OpenWeatherMapAPI.get_weather_for_cities()
        assert len(weather_data) == len(CITIES)
        for city in CITIES:
            assert city in weather_data
            assert weather_data[city] == mock_response

def test_api_error_handling():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("API Error")
        with pytest.raises(Exception):
            OpenWeatherMapAPI.get_weather('Delhi')
