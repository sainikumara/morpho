from application import db
from application.models import Base

from flask_login import current_user

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
        
        avg = 0
        num = self.number_of_ratings(self)
        if num != 0:
            avg = sum / num

        return avg

    @staticmethod
    def find_routes_user_has_rated():
        stmt = text("SELECT Route.id FROM Route"
                     " LEFT JOIN Rating ON Rating.route_id = Route.id"
                     " WHERE Rating.account_id = :user_id"
                     " ORDER BY Route.grade").params(user_id = current_user.id)
        res = db.engine.execute(stmt)

        ids_of_routes_rated = []
        for row in res:
            ids_of_routes_rated.append(int(row[0]))

        return ids_of_routes_rated

    def routes_user_has_rated(self):
        ids = self.find_routes_user_has_rated()

        routes_rated = []
        for id in ids:
            routes_rated.append(Route.query.filter_by(id = id).first())
        
        return routes_rated

    # @staticmethod
    # def find_routes_user_has_not_rated():
    #     stmt = text("SELECT Route.id FROM Rating"
    #                  " LEFT JOIN Route ON Rating.route_id = Route.id"
    #                  " WHERE NOT (Rating.account_id = :user_id)"
    #                  " ORDER BY Route.grade").params(user_id = current_user.id)
    #     res = db.engine.execute(stmt)

    #     print("TULOSTELUAIKA")
        
    #     ids_of_routes_not_rated = []
    #     for row in res:
    #         ids_of_routes_not_rated.append(int(row[0]))
    #         print(row[0])

    #     return ids_of_routes_not_rated

    # def routes_user_has_not_rated(self):
    #     ids = self.find_routes_user_has_not_rated()

    #     routes_not_rated = []
    #     for id_of_route in ids:
    #         routes_not_rated.append(Route.query.filter_by((id = id_of_route)).first())
        
    #     return routes_not_rated
