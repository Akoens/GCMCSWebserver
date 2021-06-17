from flask import Blueprint, render_template


def construct_blueprint():
    dashboard = Blueprint('dashboard', __name__)

    @dashboard.route('/dashboard', methods=['GET'])
    def display():
        return render_template("dashboard.html", title="Dashboard")

    return dashboard
