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
        stmt = text("SELECT route.name, route.grade, COUNT(rating.value) as ratings, AVG(rating.value) AS avg FROM "
                    "route INNER JOIN rating ON route.id = rating.route_id "
                    "GROUP BY route.name ORDER BY avg DESC LIMIT :how_many").params(
                        how_many = number_of_recommendations
                    )
        return stmt

    @staticmethod
    def create_individual_recommendation(user, height_offset, weight_offset, arm_span_offset, number_of_recommendations):
        stmt = text("SELECT route.name, route.grade, COUNT(rating.value) as ratings, AVG(rating.value) AS avg FROM "
	                "route INNER JOIN rating ON route.id = rating.route_id "
                    "WHERE NOT route.id IN "
	                "(SELECT rating.route_id from rating WHERE rating.account_id=:user_id)"
	                "AND rater_height BETWEEN :height - :height_offset AND :height + :height_offset "
	                "AND rater_weight BETWEEN :weight - :weight_offset AND :weight + :weight_offset "
	                "AND rater_arm_span BETWEEN :arm_span - :arm_span_offset AND :arm_span + :arm_span_offset "
	                "GROUP BY route.name "
	                "ORDER BY avg DESC "
	                "LIMIT :how_many").params(
                        user_id = user.get_id(),
                        height = user.get_height(),
                        height_offset = height_offset,
                        weight = user.get_weight(),
                        weight_offset = weight_offset,
                        arm_span = user.get_arm_span(),
                        arm_span_offset = arm_span_offset,
                        how_many = number_of_recommendations
                    )

        return stmt

    @staticmethod
    def create_recommendation(self, user, number_of_recommendations):
        if user.is_authenticated:
            stmt = self.create_individual_recommendation(user, 3, 3, 3, number_of_recommendations)
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

        recommendation = []
        for row in result:
            route_to_recommend = []
            route_name = row[0]
            route_grade = row[1]
            ratings = row[2]
            avg = row[3]
            route_to_recommend.append(route_name)
            route_to_recommend.append(route_grade)
            route_to_recommend.append(ratings)
            route_to_recommend.append("{0:.2f}".format(avg))

            recommendation.append(route_to_recommend)
        
        return recommendation, message

    @staticmethod
    def grades_with_best_ratings():
        stmt = text("SELECT route.grade AS grade, AVG(rating.value) AS avg FROM route "
                    "INNER JOIN rating ON rating.route_id = route.id "
                    "GROUP BY grade "
	                "ORDER BY avg DESC "
                    "LIMIT 5")
        res = db.engine.execute(stmt)

        ratings_of_grades = []
        for row in res:
            rating_of_grade = []
            grade = row[0]
            rating = row[1]
            rating_of_grade.append(grade)
            rating_of_grade.append(rating)
            ratings_of_grades.append(rating_of_grade)

        return ratings_of_grades

    @staticmethod
    def find_routes_user_has_rated(user):
        stmt = text("SELECT route.id FROM route"
                    " LEFT JOIN rating ON rating.route_id = route.id"
                    " WHERE rating.account_id = :user_id"
                    " ORDER BY route.grade").params(user_id = user.id)
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
