from flask import render_template
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User
from application.routes.models import Route

@app.route("/")
def index():
    recommendation = Route.create_recommendation(Route, current_user, 5)
    
    if len(recommendation[0]) == 0:
        message = "Unfortunately there is not enough data yet to provide a result"
    else:
        message = recommendation[2]

    return render_template("index.html", message = message,
        routes = recommendation[0], averages = recommendation[1])
