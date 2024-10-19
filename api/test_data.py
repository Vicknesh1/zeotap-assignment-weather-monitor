import pytest
from src.data_processing.daily_summary import calculate_daily_summary

def test_calculate_daily_summary():
    test_data = [
        {'main': {'temp': 25}, 'weather': [{'main': 'Clear'}]},
        {'main': {'temp': 30}, 'weather': [{'main': 'Cloudy'}]},
        {'main': {'temp': 20}, 'weather': [{'main': 'Clear'}]}
    ]
    summary = calculate_daily_summary(test_data)
    assert summary['avg_temp'] == 25
    assert summary['max_temp'] == 30
    assert summary['min_temp'] == 20
    assert summary['dominant_condition'] == 'Clear'

# Add more test cases for other modules
