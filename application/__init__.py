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

    stmt = text("CREATE TABLE grades_of_users "
                "(user_id INTEGER NOT NULL, grade_id INTEGER NOT NULL, "
                "PRIMARY KEY (user_id, grade_id), "
                "FOREIGN KEY(user_id) REFERENCES account (id), "
                "FOREIGN KEY(grade_id) REFERENCES grade (id))")
    res = db.engine.execute(stmt)
    db.session().commit()

    
except:
    pass
