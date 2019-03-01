from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.routes.models import Grade, grades_of_users
from application.auth.forms import LoginForm, NewUserForm, UserHeightForm, UserWeightForm, UserArmSpanForm, UserGradeForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
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
    return render_template("auth/new.html", form = NewUserForm(), message = "")

@app.route("/auth/", methods=["POST"])
def users_create():
    form = NewUserForm(request.form)
    
    if not form.validate():
        return render_template("auth/new.html", form = form)
    
    username = form.username.data
    if User.query.filter_by(username=username).first() is None:
        user = User(username, form.password.data)
    else:
        return render_template("auth/new.html", form = NewUserForm(), message = "This username is already taken")

    users_in_database = User.query.order_by(User.username).all()

    if users_in_database:
        user.role = "DEFAULT"
    else:
        user.role = "ADMIN"

    db.session().add(user)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/user_data/", methods=["GET"])
@login_required()
def user_data():
    return render_template("auth/user_data.html",
        height_form = UserHeightForm(),
        weight_form = UserWeightForm(),
        arm_span_form = UserArmSpanForm(),
        user_grade_form = UserGradeForm(),
        user=current_user)

@app.route("/user_data/height/", methods=["POST"])
@login_required()
def user_height():

    form = UserHeightForm(request.form)

    if not form.validate():
        return render_template("auth/user_data.html",
            height_form = form,
            weight_form = UserWeightForm(),
            arm_span_form = UserArmSpanForm(),
            user_grade_form = UserGradeForm(),
            user = current_user)

    user = current_user

    height = form.new_height.data
    if isinstance(height, int):
        user._set_height(height)

    db.session().commit()

    return redirect(url_for("user_data"))

@app.route("/user_data/weight/", methods=["POST"])
@login_required()
def user_weight():

    form = UserWeightForm(request.form)

    if not form.validate():
        return render_template("auth/user_data.html",
            height_form = UserHeightForm(),
            weight_form = form,
            arm_span_form = UserArmSpanForm(),
            user_grade_form = UserGradeForm(),
            user = current_user)

    user = current_user
    
    weight = form.new_weight.data
    if isinstance(weight, int):
        user._set_weight(weight)

    db.session().commit()

    return redirect(url_for("user_data"))

@app.route("/user_data/arm_span/", methods=["POST"])
@login_required()
def user_arm_span():

    form = UserArmSpanForm(request.form)

    if not form.validate():
        return render_template("auth/user_data.html",
            height_form = UserHeightForm(),
            weight_form = UserWeightForm(),
            arm_span_form = form,
            user_grade_form = UserGradeForm(),
            user = current_user)

    user = current_user
    
    arm_span = form.new_arm_span.data
    if isinstance(arm_span, int):
        user._set_arm_span(arm_span)

    db.session().commit()

    return redirect(url_for("user_data"))

@app.route("/user_data/grades/", methods=["POST"])
@login_required()
def user_grades():
    form = UserGradeForm(request.form)

    if not form.validate():
        return render_template("auth/user_data.html",
            height_form = UserHeightForm(),
            weight_form = UserWeightForm(),
            arm_span_form = UserArmSpanForm(),
            user_grade_form = form,
            user = current_user)

    user = current_user

    grades_data = form.grades.data
    for grade_data in grades_data:
        grade = Grade.query.filter_by(id = grade_data).first()
        grade.users.append(user)

    db.session().commit()

    return redirect(url_for("user_data"))

@app.route("/users/", methods=["GET"])
@login_required(role="ADMIN")
def users_index():
    users_to_show = User.query.order_by(User.username).all()

    return render_template("auth/list.html", users = users_to_show)

@app.route("/users/<user_id>/role", methods=["POST"])
@login_required(role="ADMIN")
def change_role(user_id):

    user = User.query.filter_by(id=user_id).first()

    if user.role == "ADMIN":
        user.role = "DEFAULT"
        if user == current_user:
            db.session().commit()
            return redirect(url_for("index"))
    else:
        user.role = "ADMIN"

    db.session().commit()

    return redirect(url_for("users_index"))

@app.route("/users/<user_id>/delete/", methods=["POST"])
@login_required(role="ADMIN")
def users_delete(user_id):
    user = User.query.filter_by(id=user_id).first()

    if user.role != "ADMIN":
        User.query.filter_by(id=user_id).delete()

    db.session().commit()

    return redirect(url_for("users_index"))

@app.route("/users/<grade_id>/remove_grade/", methods=["POST"])
@login_required()
def grade_remove(grade_id):
    user = current_user

    user.remove_grade(user, grade_id)

    return redirect(url_for("user_data"))
