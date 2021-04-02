import json


class JsonManager:
    @staticmethod
    def save_data(data):
        with open('databasemanager/db.json', 'w') as f:
            json.dump(data, f)

    @staticmethod
    def get_data():
        with open('databasemanager/db.json', 'r') as f:
            return json.loads(f.read())
