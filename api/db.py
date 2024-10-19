from pymongo import MongoClient

class DBManager:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client['weather_monitoring']
        self.daily_summaries = self.db['daily_summaries']

    def insert_daily_summary(self, date, city, summary):
        self.daily_summaries.update_one(
            {'date': date, 'city': city},
            {'$set': summary},
            upsert=True
        )

    def get_daily_summaries(self, city, start_date, end_date):
        return list(self.daily_summaries.find({
            'city': city,
            'date': {'$gte': start_date, '$lte': end_date}
        }))
