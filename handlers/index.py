from flask import Blueprint, render_template
from flask_login import login_required


def construct_blueprint():
    index = Blueprint('index', __name__)

    @index.route('/', methods=['GET'])
    @login_required
    def display():
        return render_template("index.html", title="Index")

    return index
