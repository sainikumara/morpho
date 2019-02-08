from application import db
from application.models import Base

class Rating(Base):
    value = db.Column(db.Integer, nullable=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, value, route):
        self.value = value
        self.route_id = route