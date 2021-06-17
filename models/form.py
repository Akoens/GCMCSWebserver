from wtforms import StringField, PasswordField, SubmitField, validators, Form


class SignupForm(Form):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=4, max=35)])
    email = StringField('E-mail', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.DataRequired(), validators.Length(min=6, max=35),
                                              validators.EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Repeat Password')
    submit = SubmitField('Submit')
