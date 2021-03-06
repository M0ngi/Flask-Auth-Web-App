from website import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(256))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    role = db.Column(db.Integer, db.ForeignKey('role.id'))