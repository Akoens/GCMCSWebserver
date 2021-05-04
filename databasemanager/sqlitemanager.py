import sqlite3 as sql
from typing import List

from models.data import Data
from models.microcontroller import Microcontroller
from models.user import User


class SqliteManager:

    def __init__(self, database_name: str = "GCMCS.db", database_location: str = "database/") -> None:
        self.database_name = database_name
        self.database_location = database_location
        self.conn = sql.connect(self.database_location + self.database_name)
        self.c = self.conn.cursor()
        self.__init_database()

    def __init_database(self) -> None:
        try:
            with self.conn:
                self.c.execute("""
                CREATE TABLE IF NOT EXISTS "User" (
                    "id" INTEGER NOT NULL PRIMARY KEY UNIQUE,
                    "name" TEXT NOT NULL,
                    "email"	TEXT NOT NULL UNIQUE,
                    "hashed_password" TEXT NOT NULL
                )""")

                self.c.execute("""
                CREATE TABLE IF NOT EXISTS "Microcontroller" (
                    "id" INTEGER NOT NULL PRIMARY KEY UNIQUE,
                    "name" TEXT,
                    "User_id" INTEGER NOT NULL,
                    FOREIGN KEY("User_id") REFERENCES "User"("id") ON DELETE CASCADE
                )""")

                self.c.execute("""
                CREATE TABLE IF NOT EXISTS "Data" ( 
                    "id" INTEGER NOT NULL PRIMARY KEY UNIQUE,
                    "temperature" REAL, 
                    "light"	INTEGER, 
                    "humidity" REAL, 
                    "heat_index" REAL, 
                    "ground_temperature"	REAL,
                    "timestamp"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    "Microcontroller_id" INTEGER NOT NULL, 
                    "Microcontroller_User_id" INTEGER NOT NULL, 
                    FOREIGN KEY("Microcontroller_id") REFERENCES "Microcontroller"("id") ON DELETE CASCADE, 
                    FOREIGN KEY("Microcontroller_User_id") REFERENCES "Microcontroller"("User_id") ON DELETE CASCADE
                )""")
        except sql.IntegrityError as e:
            print(e)

    # Functions for adding entries to database tables
    def add_user(self, user: User) -> None:
        try:
            with self.conn:
                self.c.execute("""
                                INSERT INTO User (id, name, email, hashed_password)
                                VALUES (:id, :name, :email, :hashed_password)""",
                               {"id": user.id, "name": user.name, "email": user.email,
                                "hashed_password": user.hashed_password})
        except sql.IntegrityError as e:
            print(e)

    def add_microcontroller(self, microcontroller: Microcontroller) -> None:
        try:
            with self.conn:
                self.c.execute("""INSERT INTO Microcontroller (id, name, User_id)
                                VALUES (:id, :name, :user_id)""",
                               {"id": microcontroller.id, "name": microcontroller.name,
                                "user_id": microcontroller.user_id})
        except sql.IntegrityError as e:
            print(e)

    def add_data(self, data: Data) -> None:
        try:
            with self.conn:
                self.c.execute("""
                    INSERT INTO Data (
                        id, temperature, light, humidity, heat_index, ground_temperature,
                        Microcontroller_id, Microcontroller_User_id)
                    VALUES (
                        :id, :temperature, :light, :humidity, :heat_index,:ground_temperature, 
                        :microcontroller_id, :microcontroller_user_id)""", {
                    "id": data.id,
                    "temperature": data.temperature,
                    "light": data.light,
                    "humidity": data.humidity,
                    "heat_index": data.heat_index,
                    "ground_temperature": data.ground_temperature,
                    "microcontroller_id": data.microcontroller_id,
                    "microcontroller_user_id": data.microcontroller_user_id
                })
        except sql.IntegrityError as e:
            print(e)

    # Functions for selecting entries to database tables
    def select_user_by_id(self, user_id: int) -> User:
        try:
            with self.conn:
                self.c.execute("""SELECT * FROM User WHERE id = :user_id""",
                               {"user_id": user_id})
                r = self.c.fetchone()
                return User(r[1], r[2], r[3], r[0])
        except sql.IntegrityError as e:
            print(e)

    def select_user_by_email(self, user_email: str) -> User:
        try:
            with self.conn:
                self.c.execute("""SELECT * FROM User WHERE email = :user_email""",
                               {"user_email": user_email})
                r = self.c.fetchone()
                return User(r[1], r[2], r[3], r[0])
        except sql.IntegrityError as e:
            print(e)

    def select_microcontroller_by_id(self, microcontroller_id: int) -> Microcontroller:
        try:
            with self.conn:
                self.c.execute("""SELECT * FROM Microcontroller WHERE id = :microcontroller_id""",
                               {"microcontroller_id": microcontroller_id})
                r = self.c.fetchone()
                return Microcontroller(r[1], r[2], r[0])
        except sql.IntegrityError as e:
            print(e)

    def select_microcontrollers_by_user_id(self, microcontroller_user_id: int) -> List[Microcontroller]:
        try:
            with self.conn:
                self.c.execute("""SELECT * FROM Microcontroller WHERE user_id = :microcontroller_user_id""",
                               {"microcontroller_user_id": microcontroller_user_id})
                records = self.c.fetchall()
                print(records)
                return [Microcontroller(r[1], r[2], r[0]) for r in records]
        except sql.IntegrityError as e:
            print(e)

    def select_data_by_id(self, data_id: int) -> Data:
        try:
            with self.conn:
                self.c.execute("""SELECT * FROM Data WHERE id = :data_id""", {"data_id": data_id})
                r = self.c.fetchone()
                return Data(r[1], r[2], r[3], r[4], r[5], r[7], r[8], r[0], r[6])
        except sql.IntegrityError as e:
            print(e)

    def select_data_by_microcontroller_id(self, microcontroller_id: int) -> List[Data]:
        try:
            with self.conn:
                self.c.execute("""SELECT * FROM Data WHERE Microcontroller_id = :microcontroller_id""",
                               {"microcontroller_id": microcontroller_id})
                records = self.c.fetchall()
                return [Data(r[1], r[2], r[3], r[4], r[5], r[7], r[8], r[0], r[6]) for r in records]
        except sql.IntegrityError as e:
            print(e)

    # Functions for updating entries to database tables
    def update_user(self, user_id: int) -> None:
        try:
            with self.conn:
                self.c.execute("""UPDATE FROM User VALUES () WHERE id = :user_id """, {"user_id": user_id})
        except sql.IntegrityError as e:
            print(e)

    # Functions for updating entries to database tables
    def delete_user_by_id(self, user_id: int) -> None:
        try:
            with self.conn:
                self.c.execute("""DELETE FROM User WHERE id = :user_id""", {"user_id": user_id})
        except sql.IntegrityError as e:
            print(e)

    def delete_microcontroller_by_id(self, microcontroller_id: int) -> None:
        try:
            with self.conn:
                self.c.execute("""DELETE FROM User WHERE id = :microcontroller_id""",
                               {"microcontroller_id": microcontroller_id})

        except sql.IntegrityError as e:
            print(e)

    def delete_data_by_id(self, data_id: int) -> None:
        try:
            with self.conn:
                self.c.execute("""DELETE FROM User WHERE id = :data_id""", {"data_id": data_id})

        except sql.IntegrityError as e:
            print(e)

    # Close the database connection
    def close(self):
        self.c.close()
        self.conn.close()
