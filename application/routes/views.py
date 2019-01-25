from application import app, db
from flask import redirect, render_template, request, url_for
from application.routes.models import Route
from application.ratings.models import Rating

@app.route("/routes", methods=["GET"])
def routes_index():
    return render_template("routes/list.html", routes = Route.query.all())

@app.route("/routes/new/")
def routes_form():
    return render_template("routes/new.html")

@app.route("/routes/<route_id>/", methods=["POST"])
def routes_set_done(route_id):

    route = Route.query.get(route_id)
    route.done = True
    db.session().commit()

    return redirect(url_for("routes_index"))

@app.route("/routes/", methods=["POST"])
def routes_create():
    route = Route(request.form.get("name"), request.form.get("grade"))

    db.session().add(route)
    db.session().commit()

    return redirect(url_for("routes_index"))
