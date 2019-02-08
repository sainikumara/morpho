from flask_wtf import FlaskForm
from wtforms import RadioField

class RatingForm(FlaskForm):
    new_rating = RadioField("Rate", choices=[("1","1"),("2","2"),("3","3"),("3","4"),("5","5")])
 
    class Meta:
        csrf = False
