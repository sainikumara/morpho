from application import db, bcrypt
from application.models import Base

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(64), unique=True, nullable=False)
    _password = db.Column(db.String(128), nullable=False)

    role = db.Column(db.String(10), nullable=False)

    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    arm_span = db.Column(db.Integer, nullable=True)

    routes_created = db.relationship("Route", backref='account', lazy=True)
    ratings_given = db.relationship("Rating", backref='account', lazy=True)

    def __init__(self, username, plaintext):
        self.username = username
        self._password = bcrypt.generate_password_hash(plaintext, 15).decode('utf-8')

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext, 15)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

    def _set_height(self, value):
        self.height = value
    
    def get_height(self):
        return self.height

    def _set_weight(self, value):
        self.weight = value

    def get_weight(self):
        return self.weight

    def _set_arm_span(self, value):
        self.arm_span = value

    def get_arm_span(self):
        return self.arm_span

    def roles(self):
        if self.role == "ADMIN":
            return ["ADMIN"]
        else:
            return ["DEFAULT"]

    @staticmethod
    def top_raters():
        stmt = text("SELECT account.username AS name, COUNT(rating.id) AS ratings FROM account "
                    "INNER JOIN rating ON rating.account_id = account.id "
                    "GROUP BY name "
	                "ORDER BY ratings DESC "
                    "LIMIT 5")
        res = db.engine.execute(stmt)

        ratings_of_users = []
        for row in res:
            user_and_ratings = []
            username = row[0]
            ratings = row[1]
            user_and_ratings.append(username)
            user_and_ratings.append(ratings)
            ratings_of_users.append(user_and_ratings)

        return ratings_of_users

    @staticmethod
    def interested_in_grades(user):
        stmt = text("SELECT grade_id FROM grades_of_users WHERE user_id = :user_id").params(user_id = user.id)
        res = db.engine.execute(stmt)

        grades = []
        for row in res:
            grades.append(row[0])

        return grades

    @staticmethod
    def remove_grade(user, grade_id):
        stmt = text("DELETE FROM grades_of_users "
                    "WHERE user_id = :user_id AND grade_id =:grade_id"
                    ).params(user_id = user.id, grade_id = grade_id)
        res = db.engine.execute(stmt)

        db.session().commit()
