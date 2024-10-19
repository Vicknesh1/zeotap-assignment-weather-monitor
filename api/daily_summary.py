from collections import Counter

def calculate_daily_summary(weather_data):
    temperatures = [data['main']['temp'] for data in weather_data]
    conditions = [data['weather'][0]['main'] for data in weather_data]
    
    return {
        'avg_temp': sum(temperatures) / len(temperatures),
        'max_temp': max(temperatures),
        'min_temp': min(temperatures),
        'dominant_condition': Counter(conditions).most_common(1)[0][0]
    }
