from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=64)])
    password = PasswordField("Password", [validators.Length(min=2)])

    class Meta:
        csrf = False