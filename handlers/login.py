from flask import Blueprint, render_template


def construct_blueprint():
    login = Blueprint('login', __name__)

    @login.route('/login', methods=['GET'])
    def display():
        return render_template("login.html", title="Login")

    return login
