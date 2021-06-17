from wtforms import StringField, PasswordField, SubmitField, validators, Form


class LoginForm(Form):

    email = StringField('E-mail', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])

    submit = SubmitField('Submit')
