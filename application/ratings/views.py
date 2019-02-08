from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.routes.models import Route
from application.ratings.models import Rating
from application.ratings.forms import RatingForm

@app.route("/ratings", methods=["GET"])
def ratings_index():
    return render_template("ratings/list.html", ratings = Rating.query.all())

@app.route("/<route_id>/ratings", methods=["POST"])
@login_required
def ratings_create(route_id):
    form = RatingForm(request.form)

    rating = Rating(int(form.new_rating.data), int(route_id))
    rating.account_id = current_user.id

    db.session().add(rating)
    db.session().commit()

    return redirect(url_for("routes_index"))