from application import app, db
from flask import redirect, render_template, request, url_for
from application.routes.models import Route

@app.route("/routes", methods=["GET"])
def routes_index():
    return render_template("routes/list.html", routes = Route.query.all())

@app.route("/routes/new/")
def routes_form():
    return render_template("routes/new.html")

@app.route("/routes/<route_id>/", methods=["POST"])
def routes_set_done(route_id):

    r = Route.query.get(route_id)
    r.done = True
    db.session().commit()

    return redirect(url_for("routes_index"))

@app.route("/routes/", methods=["POST"])
def routes_create():
    r = Route(request.form.get("name"))

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("routes_index"))
