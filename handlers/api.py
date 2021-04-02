from flask import Blueprint, request, jsonify
from databasemanager.jsonmanager import JsonManager


def construct_blueprint():
    api = Blueprint('api', __name__)

    @api.route('/api/send', methods=['POST'])
    def send_data():
        if request.method == 'POST':
            data = request.json
            print(data)

            JsonManager.save_data(data)

            return jsonify({'result': 'success'}), 200

    @api.route('/api/receive', methods=['POST'])
    def receive_data():
        if request.method == 'POST':
            data = JsonManager.get_data()
            return jsonify({'result': 'success', 'data': data}), 200

    return api
