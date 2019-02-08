from application import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    username = db.Column(db.String(64), unique=True, nullable=False)
    _password = db.Column(db.String(128), nullable=False)

    routes_created = db.relationship("Route", backref='account', lazy=True)


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
        self._password = bcrypt.generate_password_hash(plaintext, 20)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)
