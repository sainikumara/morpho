from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators

class RouteForm(FlaskForm):
    name = StringField("Route name", [validators.Length(min=2, max=144)])
    grade = SelectField("Grade", choices=[("3A","3A"),("3B","3B"),("3C","3C"),("4A","4A"),("4B","4B"),("4C","4C"),("5A","5A"),("5B","5B"),("5C","5C"),("6A","6A"),("6B","6B"),("6C","6C"),("7A","7A"),("7B","7B"),("7C","7C"),("8A","8A"),("8B","8B"),("8C","8C"),("9A","9A")])
 
    class Meta:
        csrf = False
