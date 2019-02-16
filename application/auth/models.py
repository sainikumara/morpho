from application import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(64), unique=True, nullable=False)
    _password = db.Column(db.String(128), nullable=False)

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
