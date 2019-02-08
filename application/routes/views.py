from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.routes.models import Route
from application.ratings.models import Rating
from application.routes.forms import RouteForm
from application.ratings.forms import RatingForm

@app.route("/routes", methods=["GET"])
def routes_index():
    return render_template("routes/list.html", routes = Route.query.all(), form = RatingForm())

@app.route("/routes/new/")
@login_required
def routes_form():
    return render_template("routes/new.html", form = RouteForm())

@app.route("/<route_id>/delete/", methods=["POST"])
@login_required
def routes_delete(route_id):
    Route.query.filter_by(id=route_id).delete()
    db.session().commit()

    return redirect(url_for("routes_index"))

@app.route("/routes/", methods=["POST"])
@login_required
def routes_create():
    form = RouteForm(request.form)
    
    if not form.validate():
        return render_template("routes/new.html", form = form)

    route = Route(form.name.data, form.grade.data)
    route.creator_account_id = current_user.id

    db.session().add(route)
    db.session().commit()

    return redirect(url_for("routes_index"))
