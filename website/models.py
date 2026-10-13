from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
#from sqlalchemy_imageattach.entity import Image, image_attachment
from datetime import datetime 

from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    pfp = db.Column(db.String(300))
    is_admin = db.Column(db.Boolean, default=False)

    items = db.relationship('Items', backref='owner', lazy=True)
    #is_admin = db.Column(db.Boolean, default=False)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    prize = db.Column(db.String(150), nullable=True)
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    img = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    images = db.relationship('Image', backref='item', lazy=True)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pos = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(300), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)