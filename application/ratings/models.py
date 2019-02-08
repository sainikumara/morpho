from application import db
from application.models import Base

from sqlalchemy.sql import text

class Rating(Base):
    value = db.Column(db.Integer, nullable=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, value, route):
        self.value = value
        self.route_id = route

    def _set_rating_value(self, value):
        self.value = value
