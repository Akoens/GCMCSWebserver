from flask import url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.utils import redirect
from flask import render_template, request, Blueprint
from werkzeug.security import check_password_hash

from databasemanager.sqlitemanager import SqliteManager
from models.loginform import LoginForm


def construct_blueprint():
    login = Blueprint('login', __name__)

    @login.route('/login', methods=['GET', 'POST'])
    def display():
        manager = SqliteManager()
        form = LoginForm(request.form)
        error = None

        if request.method == 'POST' and form.validate():
            email = request.form['email']
            password = request.form['password']
            user = manager.user_exists_by_email(email)

            if not user:
                error = 'Wrong username or password'

            else:
                user = manager.select_user_by_email(email)
                if check_password_hash(user.hashed_password, password):
                    login_user(user)
                    return redirect(url_for('dashboard.display'))

                else:
                    error = 'Wrong username or password'

        return render_template('login.html', form=form, error=error)

    @login.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login.display'))

    return login
