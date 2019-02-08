from application import db
from application.models import Base

class Route(Base):
    name = db.Column(db.String(144), nullable=False)
    grade = db.Column(db.String(2), nullable=False)

    creator_account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    
    ratings = db.relationship("Rating", backref='route', lazy=True)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
