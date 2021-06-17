from flask import Blueprint, request, jsonify

from databasemanager.sqlitemanager import SqliteManager
from models.data import Data


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
