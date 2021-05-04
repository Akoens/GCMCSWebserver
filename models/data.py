import sqlite3 as sql


class Data:

    def __init__(self, temperature: float, light: int, humidity: float,
                 heat_index: float, ground_temperature: float,
                 microcontroller_id: int, microcontroller_user_id: int, data_id: int = None,
                 timestamp: sql.Timestamp = None) -> None:
        self.id = data_id
        self.temperature = temperature
        self.light = light
        self.humidity = humidity
        self.heat_index = heat_index
        self.ground_temperature = ground_temperature
        self.timestamp = timestamp
        self.microcontroller_id = microcontroller_id
        self.microcontroller_user_id = microcontroller_user_id

    def __repr__(self) -> str:
        return f"""Data<Id={self.id}, Temperature={self.temperature}, Light={self.light}, Humidity={self.humidity}, Heat index={self.heat_index}, Ground temperature={self.ground_temperature}, Timestamp={self.timestamp} Microcontroller id={self.microcontroller_id}, Microcontroller User id={self.microcontroller_user_id}> """
