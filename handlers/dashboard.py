from flask import Blueprint, render_template
from databasemanager.jsonmanager import JsonManager


def construct_blueprint():
    dashboard = Blueprint('dashboard', __name__)

    @dashboard.route('/dashboard', methods=['GET'])
    def display():
        data = JsonManager.get_data()
        return render_template("dashboard.html", title="Dashboard", data=data)

    return dashboard
