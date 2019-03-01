from flask import render_template
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.routes.models import Route

@app.route("/")
def index():
    recommendation_and_message = Route.create_recommendation(Route, current_user, 5)
    recommendation = recommendation_and_message[0]

    if len(recommendation) == 0:
        message = "Unfortunately there is not enough data yet to provide a result"
    else:
        message = recommendation_and_message[1]

    top_grades = Route.grades_with_best_ratings()
    top_raters = User.top_raters()

    return render_template("index.html", message = message,
        recommendation = recommendation,
        top_grades = top_grades, top_raters = top_raters)
