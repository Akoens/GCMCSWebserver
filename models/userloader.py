from databasemanager.sqlitemanager import SqliteManager
from models.user import User
from flask_login import LoginManager


login_manager = LoginManager()


def load_login_manager(app):
    login_manager.init_app(app)
    login_manager.login_view = "login.display"


@login_manager.user_loader
def user_loader(userid):
    manager = SqliteManager()
    return manager.select_user_by_id(int(userid))

