import time
from datetime import datetime
from api.openweathermap import OpenWeatherMapAPI
from data_processing.daily_summary import calculate_daily_summary
from database.db_manager import DBManager
from config import DB_CONNECTION_STRING, UPDATE_INTERVAL

db_manager = DBManager(DB_CONNECTION_STRING)

def process_weather_data():
    weather_data = OpenWeatherMapAPI.get_weather_for_cities()
    for city, data in weather_data.items():
        daily_summary = calculate_daily_summary([data])
        db_manager.insert_daily_summary(datetime.now().date(), city, daily_summary)
        
    # Implement alerting logic here

def main():
    while True:
        process_weather_data()
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
