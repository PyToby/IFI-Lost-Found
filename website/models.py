from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    pfp = db.Column(db.String(300))