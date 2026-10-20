from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
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

    def get_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)

    def remove(self):
        db.session.delete(self)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    prize = db.Column(db.String(150), nullable=True)
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    img = db.Column(db.String(300))
    user_email = db.Column(db.String(150), db.ForeignKey('user.email'), nullable=False)
    type = db.Column(db.String(150), nullable=True) #I found or I lost
    state = db.Column(db.String(150), nullable=True) #Pending, Closed, Archived 

    images = db.relationship('Image', backref='item', lazy=True)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pos = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(300), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)