from flask import Blueprint, render_template
from flask_login import login_required


def construct_blueprint():
    dashboard = Blueprint('dashboard', __name__)

    @dashboard.route('/dashboard', methods=['GET'])
    @login_required
    def display():
        return render_template("dashboard.html", title="Dashboard")

    return dashboard
