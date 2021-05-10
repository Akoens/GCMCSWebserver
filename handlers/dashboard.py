from flask import Blueprint, render_template
from databasemanager.sqlitemanager import SqliteManager


def construct_blueprint():
    dashboard = Blueprint('dashboard', __name__)

    @dashboard.route('/dashboard', methods=['GET'])
    def display():
        manager = SqliteManager()
        data = manager.select_data_by_microcontroller_id(1)
        return render_template("dashboard.html", title="Dashboard", data=data[0])

    return dashboard
