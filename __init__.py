from flask import Flask
from config import get_config

# Path handler imports
from handlers import index,dashboard, api, settings, login

# Database imports
from databasemanager.sqlitemanager import SqliteManager
from models.data import Data
from models.microcontroller import Microcontroller
from models.user import User

if __name__ == '__main__':
    # Import config.
    cfg = get_config()

    # manager = SqliteManager()
    # manager.add_user(User("bob", "bob@harris.com", "pASS"))
    # user = manager.select_user_by_email("bob@harris.com")
    # manager.add_microcontroller(Microcontroller("bob's microcontroller", user.id))
    # microcontrollers = manager.select_microcontrollers_by_user_id(user.id)
    # for x in range(30):
    #     manager.add_data(Data(float(x), 590, 3.0, 50.0, 18.0, 58.0, microcontrollers[0].id, microcontrollers[0].user_id))
    #
    # print(user)
    # print(microcontrollers)
    # print(data, end="\n\n")

    handlers = [index, dashboard, api, settings, login]
    app = Flask(__name__)
    for handler in handlers:
        app.register_blueprint(handler.construct_blueprint())

    # Start the webserver.
    app.run(host="0.0.0.0", port=cfg["flask"]["port"])
