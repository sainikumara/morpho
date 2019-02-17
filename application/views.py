from flask import render_template
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.routes.models import Route

@app.route("/")
def index():
    recommendation = Route.create_recommendation(5)
    message = ""

    if current_user.is_authenticated:
        message = "Results are based on ratings given by other users with similar anthropometric data to yours"
    else:
        message = "Log in and keep your anthropometric data up to date in order to get results relevant to you"

    if len(recommendation[0]) == 0:
        message = "Unfortunately there is not enough data yet to provide a result"

    return render_template("index.html", message = message,
        routes = recommendation[0], averages = recommendation[1])
