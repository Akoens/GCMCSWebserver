from flask import Flask
from config import get_config

import handlers.index as index
import handlers.dashboard as dashboard
import handlers.api as api
from handlers import settings, login

if __name__ == '__main__':
    # Import config.
    cfg = get_config()

    handlers = [index, dashboard, api, settings, login]
    app = Flask(__name__)
    for handler in handlers:
        app.register_blueprint(handler.construct_blueprint())

    # Start the webserver.
    app.run(host="0.0.0.0", port=cfg["flask"]["port"])
