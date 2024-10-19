import pytest
from unittest.mock import patch, Mock
from src.main import process_weather_data
from src.database.db_manager import DBManager

@pytest.fixture
def mock_api_response():
    return {
        'Delhi': {
            'main': {'temp': 35.5},
            'weather': [{'main': 'Clear'}]
        },
        'Mumbai': {
            'main': {'temp': 30.0},
            'weather': [{'main': 'Rain'}]
        }
    }

@pytest.fixture
def mock_db_manager():
    return Mock(spec=DBManager)

def test_process_weather_data(mock_api_response, mock_db_manager):
    with patch('src.api.openweathermap.OpenWeatherMapAPI.get_weather_for_cities', return_value=mock_api_response):
        with patch('src.main.db_manager', mock_db_manager):
            process_weather_data()
            
            # Check if data was processed and stored for each city
            assert mock_db_manager.insert_daily_summary.call_count == 2
            
            # Check if alerts were generated (assuming 35°C is our threshold)
            # You would need to implement and mock an alerting system for this

def test_process_weather_data_api_error(mock_db_manager):
    with patch('src.api.openweathermap.OpenWeatherMapAPI.get_weather_for_cities', side_effect=Exception("API Error")):
        with patch('src.main.db_manager', mock_db_manager):
            with pytest.raises(Exception):
                process_weather_data()
            
            # Ensure no data was stored if API call failed
            mock_db_manager.insert_daily_summary.assert_not_called()
