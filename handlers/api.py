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
                                  data["ground_temperature"], 1, 1))

            return jsonify({'result': 'success'}), 200

    @api.route('/api/receive', methods=['POST'])
    def receive_data():
        if request.method == 'POST':
            manager = SqliteManager()
            data = manager.select_data_by_microcontroller_id(1)[0].serialize()
            print(data)
            return jsonify({'result': 'success', 'data': data}), 200

    return api
