from application import db
from application.models import Base

from sqlalchemy.sql import text

class Route(Base):
    name = db.Column(db.String(144), nullable=False)
    grade = db.Column(db.String(2), nullable=False)

    creator_account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    
    ratings = db.relationship("Rating", backref='route', lazy=True)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


    @staticmethod
    def number_of_ratings(self):
        stmt = text("SELECT COUNT(Rating.id) FROM Rating"
                    " WHERE Rating.route_id = :route_to_find;").\
                    params(route_to_find = self.id)
        res = db.engine.execute(stmt)

        for row in res:
            number = int(row[0])

        return number

    @staticmethod
    def average_rating(self):
        stmt = text("SELECT Rating.value FROM Rating"
                    " WHERE Rating.route_id = :route_to_find;").\
                    params(route_to_find = self.id)
        res = db.engine.execute(stmt)

        sum = 0
        for row in res:
            sum += int(row[0])
        
        num = self.number_of_ratings(self)
        avg = sum / num

        return avg