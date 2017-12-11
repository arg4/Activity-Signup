from project import db

class Employee(db.Model):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False)
    activity = db.Column(db.String, nullable=False)
    comments = db.Column(db.String, nullable=True)

    def __init__(self, first_name, last_name, email_address, activity, comments):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.activity = activity
        self.comments = comments

    def __repr__(self):
        return '<title {}'.format(self.name)
