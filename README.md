This project implements a real-time weather monitoring system that retrieves data from the OpenWeatherMap API, processes it, and stores daily summaries in a database.
Setup

Clone the repository:
Copygit clone https://github.com/yourusername/weather-monitoring.git
cd weather-monitoring

Install dependencies:
Copypip install -r requirements.txt

Set up environment variables:
Create a .env file in the project root and add:
CopyAPI_KEY=your_openweathermap_api_key
DB_CONNECTION_STRING=your_mongodb_connection_string

Run the application:
Copypython src/main.py


Design Choices

Used OpenWeatherMap API for real-time weather data
Implemented daily summaries with MongoDB for efficient storage and retrieval
Modular design for easy extension and maintenance

Dependencies

Python 3.8+
MongoDB (can be run in a Docker container)

For a complete list of Python package dependencies, see requirements.txt.
Running Tests
To run the test suite:
Copypytest tests/
Future Improvements

Implement visualization module
Add email notifications for weather alerts
Extend to support more cities and weather parameters
