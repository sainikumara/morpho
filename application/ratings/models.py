from application import db

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    value = db.Column(db.Integer, nullable=True)
    route = db.Column(db.Integer, nullable=False)

    def __init__(self, value, route):
        self.value = value
        self.route = route