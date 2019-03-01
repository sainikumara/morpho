from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, SelectMultipleField, StringField, validators

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

class UserGradeForm(FlaskForm):
    grades = SelectMultipleField("Grades", choices=[("3A","3A"),("3B","3B"),("3C","3C"),("4A","4A"),("4B","4B"),("4C","4C"),("5A","5A"),("5B","5B"),("5C","5C"),("6A","6A"),("6B","6B"),("6C","6C"),("7A","7A"),("7B","7B"),("7C","7C"),("8A","8A"),("8B","8B"),("8C","8C"),("9A","9A")])

    class Meta:
        csrf = False
