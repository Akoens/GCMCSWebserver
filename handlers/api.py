from flask import Blueprint, request, jsonify

from databasemanager.sqlitemanager import SqliteManager
from models.data import Data
import random

# Database imports
from databasemanager.sqlitemanager import SqliteManager
from models.data import Data


def random_stuff():
    temp = round(random.uniform(18.0, 25.0))
    light = random.randint(600, 900)
    hum = round(random.uniform(50.0, 60.0))
    heat = round(random.uniform(19.0, 26.0))
    ground = round(random.uniform(16.0, 21.0))
    moist = round(random.uniform(20.0, 60.0))

    manager = SqliteManager()
    microcontrollers = manager.select_microcontrollers_by_user_id(1)
    manager.add_data(Data(temp, light, hum, heat, ground, moist, microcontrollers[0].id, microcontrollers[0].user_id))


def construct_blueprint():
    api = Blueprint('api', __name__)

    @api.route('/api/send', methods=['POST'])
    def send_data():
        if request.method == 'POST':
            data = request.json

            manager = SqliteManager()
            manager.add_data(Data(data["temperature"], data["light"], data["humidity"], data["heat_index"],
                                  data["ground_temperature"], data["ground_moisture"], 1, 1))

            return jsonify({'result': 'success'}), 200

    @api.route('/api/receive', methods=['POST'])
    def receive_data():
        random_stuff()
        if request.method == 'POST':
            manager = SqliteManager()
            data = manager.select_data_by_microcontroller_id(1)[0].serialize()
            return jsonify({'result': 'success', 'data': data}), 200

    @api.route('/api/temperature', methods=['POST'])
    def receive_temperature():
        if request.method == 'POST':
            manager = SqliteManager()
            data = manager.select_temperature_data_by_microcontroller_id(1)
            return jsonify({'result': 'success', 'data': data}), 200

    @api.route('/api/light', methods=['POST'])
    def receive_light():
        if request.method == 'POST':
            manager = SqliteManager()
            data = manager.select_light_data_by_microcontroller_id(1)
            return jsonify({'result': 'success', 'data': data}), 200

    @api.route('/api/humidity', methods=['POST'])
    def receive_humidity():
        if request.method == 'POST':
            manager = SqliteManager()
            data = manager.select_humidity_data_by_microcontroller_id(1)
            return jsonify({'result': 'success', 'data': data}), 200

    @api.route('/api/heat_index', methods=['POST'])
    def receive_heat_index():
        if request.method == 'POST':
            manager = SqliteManager()
            data = manager.select_heat_index_data_by_microcontroller_id(1)
            return jsonify({'result': 'success', 'data': data}), 200

    @api.route('/api/ground_temperature', methods=['POST'])
    def receive_ground_temperature():
        if request.method == 'POST':
            manager = SqliteManager()
            data = manager.select_ground_temperature_data_by_microcontroller_id(1)
            return jsonify({'result': 'success', 'data': data}), 200

    @api.route('/api/ground_moisture', methods=['POST'])
    def receive_ground_moisture():
        if request.method == 'POST':
            manager = SqliteManager()
            data = manager.select_ground_moisture_data_by_microcontroller_id(1)
            return jsonify({'result': 'success', 'data': data}), 200

    @api.route('/api/detail', methods=['POST'])
    def detail_data():
        if request.method == 'POST':
            print("/api/detail")

    return api
