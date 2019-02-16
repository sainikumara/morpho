from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm, UserDataForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data).first()

    if (user is None) or not user.is_correct_password(form.password.data):
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    login_user(user, remember=True)

    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/auth/new/")
def new_user_form():
    return render_template("auth/new.html", form = NewUserForm())

@app.route("/auth/", methods=["POST"])
def users_create():
    form = NewUserForm(request.form)
    
    if not form.validate():
        return render_template("auth/new.html", form = form)

    user = User(form.username.data, form.password.data)

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/user_data/", methods=["GET", "POST"])
@login_required
def user_data():
    if request.method == "GET":
        return render_template("auth/user_data.html", form = UserDataForm(), user=current_user)

    form = UserDataForm(request.form)

    if not form.validate():
        return render_template("auth/user_data.html", form = form, user=current_user)

    user = current_user

    height = form.new_height.data
    if isinstance(height, int):
        user._set_height(height)
    
    weight = form.new_weight.data
    if isinstance(weight, int):
        user._set_weight(weight)
    
    arm_span = form.new_arm_span.data
    if isinstance(arm_span, int):
        user._set_arm_span(arm_span)

    db.session().commit()

    return redirect(url_for("routes_index"))
