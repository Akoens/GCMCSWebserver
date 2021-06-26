import random

from flask import Flask
from werkzeug.security import generate_password_hash

from config import get_config
from models.userloader import load_login_manager
from databasemanager.sqlitemanager import SqliteManager
from models.user import User
from models.microcontroller import Microcontroller

# Path handler imports
from handlers import index,dashboard, api, settings, login, createuser


if __name__ == '__main__':
    # Import config.
    cfg = get_config()

    # manager = SqliteManager()
    # manager.add_user(User("Example", "example@email.com", generate_password_hash("Password123")))
    # user = manager.select_user_by_email("example@email.com")
    # manager.add_microcontroller(Microcontroller("Example's Microcontroller", user.id, 1))

    handlers = [index, dashboard, api, settings, login, createuser]
    app = Flask(__name__)
    app.secret_key = 'the random string'
    load_login_manager(app)

    for handler in handlers:
        app.register_blueprint(handler.construct_blueprint())


    # Start the webserver.
    app.run(host="0.0.0.0", port=cfg["flask"]["port"])
