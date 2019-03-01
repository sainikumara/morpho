# Flask
from flask import Flask
app = Flask(__name__)

# Bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# db and ORM
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///routes.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# login 1/2
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# load app contents
from application import views

from application.routes import models
from application.routes import views

from application.ratings import models
from application.ratings import views

from application.auth import models
from application.auth import views

from application.routes.models import grades_of_users

# login 2/2
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# database creation
try: 
    db.create_all()
    
    from application.routes.models import Grade
    if Grade.query.count() != 19:
        db.session.query(Grade).delete()
        db.session.commit()

        grade3A = Grade("3A")
        db.session().add(grade3A)
        grade3B = Grade("3B")
        db.session().add(grade3B)
        grade3C = Grade("3C")
        db.session().add(grade3C)
        grade4A = Grade("4A")
        db.session().add(grade4A)
        grade4B = Grade("4B")
        db.session().add(grade4B)
        grade4C = Grade("4C")
        db.session().add(grade4C)
        grade5A = Grade("5A")
        db.session().add(grade5A)
        grade5B = Grade("5B")
        db.session().add(grade5B)
        grade5C = Grade("5C")
        db.session().add(grade5C)
        grade6A = Grade("6A")
        db.session().add(grade6A)
        grade6B = Grade("6B")
        db.session().add(grade6B)
        grade6C = Grade("6C")
        db.session().add(grade6C)
        grade7A = Grade("7A")
        db.session().add(grade7A)
        grade7B = Grade("7B")
        db.session().add(grade7B)
        grade7C = Grade("7C")
        db.session().add(grade7C)
        grade8A = Grade("8A")
        db.session().add(grade8A)
        grade8B = Grade("8B")
        db.session().add(grade8B)
        grade8C = Grade("8C")
        db.session().add(grade8C)
        grade9A = Grade("9A")
        db.session().add(grade9A)

        db.session().commit()
except:
    pass
