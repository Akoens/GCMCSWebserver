import random

from flask import Flask
from config import get_config
from models.userloader import load_login_manager

# Path handler imports
from handlers import index,dashboard, api, settings, login, createuser


if __name__ == '__main__':
    # Import config.
    cfg = get_config()

    handlers = [index, dashboard, api, settings, login, createuser]
    app = Flask(__name__)
    app.secret_key = 'the random string'
    load_login_manager(app)

    for handler in handlers:
        app.register_blueprint(handler.construct_blueprint())


    # Start the webserver.
    app.run(host="0.0.0.0", port=cfg["flask"]["port"])
