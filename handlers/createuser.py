import hashlib
from flask import render_template, request, Blueprint, url_for, flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from databasemanager.sqlitemanager import SqliteManager
from models.form import SignupForm
from models.user import User


def check_password(hashed_password, user_password):
    return hashed_password == hashlib.md5(user_password.encode()).hexdigest()


def construct_blueprint():
    createuser = Blueprint('createuser', __name__)

    @createuser.route('/createuser', methods=['GET', 'POST'])
    def display():
        manager = SqliteManager()
        form = SignupForm(request.form)
        error = None

        # Submit form get handled here
        if request.method == 'POST' and form.validate():
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            hashed_password = generate_password_hash(password)
            # Check if user already exist
            exists = manager.user_exists_by_email(email)
            if not exists:
                manager.add_user(User(name, email, hashed_password))
                return redirect(url_for('login.display'))
            else:
                error = 'E-mail is used'
        return render_template('createuser.html', form=form, error=error)

    return createuser


