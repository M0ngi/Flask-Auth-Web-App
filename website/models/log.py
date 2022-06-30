from website import db
from sqlalchemy.sql import func


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(150))
    description = db.Column(db.String(256))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    other = db.Column(db.String(150))
    actioner_id = db.Column(db.Integer, db.ForeignKey('user.id'))