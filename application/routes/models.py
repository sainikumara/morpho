from application import db

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=True)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.done = False
