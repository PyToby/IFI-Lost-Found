from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient
from .auth import GOOGLE_CLIENT_ID 
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'nvmkcemutoje'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)
    login_manager.init_app(app)

    from .views import view
    from .auth import auth

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    # OAuth 2 client setup
    client = WebApplicationClient(GOOGLE_CLIENT_ID)

    create_database(app)

    return app

def create_database(app):
    if not path.exists('../../instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created database!')