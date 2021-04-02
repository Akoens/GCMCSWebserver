from flask import Blueprint, render_template


def construct_blueprint():
    index = Blueprint('index', __name__)

    @index.route('/', methods=['GET'])
    def display():
        return render_template("index.html", title="Index")

    return index
