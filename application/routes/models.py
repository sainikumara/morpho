from application import db
from application.models import Base

from sqlalchemy.sql import text
from application.ratings.models import Rating

class Route(Base):
    name = db.Column(db.String(144), nullable=False)
    grade = db.Column(db.String(2), nullable=False)

    creator_account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=True)
    
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
        stmt = text("SELECT AVG(value) FROM Rating"
                    " WHERE route_id = :route_to_find;").\
                    params(route_to_find = self.id)
        res = db.engine.execute(stmt)

        for row in res:
            if row[0]:
                avg = row[0]
                return "{0:.2f}".format(avg)
        
        return ""

    def own_rating_value(self, user):
        rating = Rating.query.filter_by(route_id = self.id, account_id = user.id).first()

        if rating:
            return rating.value
        else:
            return ""

    def own_rating_id(self, user):
        rating = Rating.query.filter_by(route_id = self.id, account_id = user.id).first()

        if rating:
            return rating.id

    @staticmethod
    def create_generic_recommendation(number_of_recommendations):
        stmt = text("SELECT route_id, AVG(value) AS avg FROM rating "
                    "GROUP BY route_id ORDER BY avg DESC LIMIT :how_many").params(
                        how_many = number_of_recommendations
                    )

        return stmt

    @staticmethod
    def create_recommendation(self, user, number_of_recommendations):
        if user.is_authenticated:
            stmt = text("SELECT route_id, AVG(value) AS avg FROM "
	                "(SELECT * FROM rating WHERE NOT route_id IN "
	                "(SELECT rating.route_id from rating WHERE rating.account_id=:user_id)"
	                "AND rater_height BETWEEN :height - 3 AND :height + 3 "
	                "AND rater_weight BETWEEN :weight - 3 AND :weight + 3 "
	                "AND rater_arm_span BETWEEN :arm_span - 3 AND :arm_span + 3) AS matching_ratings "
	                "GROUP BY route_id "
	                "ORDER BY avg DESC "
	                "LIMIT :how_many").params(
                        user_id = user.get_id(),
                        height = user.get_height(),
                        weight = user.get_weight(),
                        arm_span = user.get_arm_span(),
                        how_many = number_of_recommendations
                    )

            message = "Results are based on ratings given by other users with similar anthropometric data to yours"
            
        else:
            stmt = self.create_generic_recommendation(number_of_recommendations)
            message = "Log in and keep your anthropometric data up to date in order to get results relevant to you"

        res = db.engine.execute(stmt)
        result = res.fetchall()
        
        if user.is_authenticated and result == []:
            message = "Results are based on ratings given by other users, but there isn't enough data yet to make it anthropometrically relevant to you"
            stmt = self.create_generic_recommendation(number_of_recommendations)
            res = db.engine.execute(stmt)
            result = res.fetchall()

        recommended_routes = []
        average_ratings = []
        for row in result:
            route = Route.query.filter_by(id = row[0]).first()
            recommended_routes.append(route)
            average_rating = row[1]
            average_ratings.append("{0:.2f}".format(average_rating))
        
        return recommended_routes, average_ratings, message


    @staticmethod
    def find_routes_user_has_rated(user):
        stmt = text("SELECT Route.id FROM Route"
                     " LEFT JOIN Rating ON Rating.route_id = Route.id"
                     " WHERE Rating.account_id = :user_id"
                     " ORDER BY Route.grade").params(user_id = user.id)
        res = db.engine.execute(stmt)

        ids_of_routes_rated = []
        for row in res:
            ids_of_routes_rated.append(int(row[0]))

        return ids_of_routes_rated

    def routes_user_has_rated(self, user):
        ids = self.find_routes_user_has_rated(user)

        routes_rated = []
        for id in ids:
            routes_rated.append(Route.query.filter_by(id = id).first())
        
        return routes_rated
