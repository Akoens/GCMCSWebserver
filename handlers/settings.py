from flask import Blueprint, render_template


def construct_blueprint():
    settings = Blueprint('settings', __name__)

    @settings.route('/settings', methods=['GET'])
    def display():
        return render_template("settings.html", title="Settings")

    return settings
