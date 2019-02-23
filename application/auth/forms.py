from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])

    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=64)])
    password = PasswordField("Password", [validators.Length(min=2, max=128)])

    class Meta:
        csrf = False

class UserHeightForm(FlaskForm):
    new_height = IntegerField("Height", [validators.NumberRange(min=40, max=300)])

    class Meta:
        csrf = False

class UserWeightForm(FlaskForm):
    new_weight = IntegerField("Weight", [validators.NumberRange(min=10, max=300)])

    class Meta:
        csrf = False

class UserArmSpanForm(FlaskForm):
    new_arm_span = IntegerField("Arm Span", [validators.NumberRange(min=40, max=300)])

    class Meta:
        csrf = False
