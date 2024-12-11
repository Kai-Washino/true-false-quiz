from datetime import datetime
from apps.app import db

class Answer(db.Model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    user_number = db.Column(db.String, index=True)
    question1 = db.Column(db.String)
    question2 = db.Column(db.String)
    question3 = db.Column(db.String)
    question4 = db.Column(db.String)
    question5 = db.Column(db.String)
    question6 = db.Column(db.String)
    question7 = db.Column(db.String)
    question8 = db.Column(db.String)
    question9 = db.Column(db.String)
    question10 = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)