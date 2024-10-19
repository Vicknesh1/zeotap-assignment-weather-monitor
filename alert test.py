import pytest
from src.data_processing.alerting import check_temperature_threshold, check_condition_threshold

def test_check_temperature_threshold():
    threshold = 35
    data = [
        {'main': {'temp': 34}},
        {'main': {'temp': 36}},
        {'main': {'temp': 35}},
    ]
    assert check_temperature_threshold(data, threshold) == True

    data = [
        {'main': {'temp': 34}},
        {'main': {'temp': 33}},
        {'main': {'temp': 35}},
    ]
    assert check_temperature_threshold(data, threshold) == False

def test_check_condition_threshold():
    condition = "Rain"
    threshold = 2
    data = [
        {'weather': [{'main': 'Clear'}]},
        {'weather': [{'main': 'Rain'}]},
        {'weather': [{'main': 'Rain'}]},
    ]
    assert check_condition_threshold(data, condition, threshold) == True

    data = [
        {'weather': [{'main': 'Clear'}]},
        {'weather': [{'main': 'Rain'}]},
        {'weather': [{'main': 'Cloudy'}]},
    ]
    assert check_condition_threshold(data, condition, threshold) == False

def test_check_temperature_threshold_empty_data():
    with pytest.raises(ValueError):
        check_temperature_threshold([], 35)

def test_check_condition_threshold_empty_data():
    with pytest.raises(ValueError):
        check_condition_threshold([], "Rain", 2)
