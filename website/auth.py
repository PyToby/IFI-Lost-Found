from flask import Blueprint, redirect, request, url_for, session
from flask_login import login_user, logout_user
from oauthlib.oauth2 import WebApplicationClient
import requests
import json
import os

from . models import User
from . import db, login_manager

auth = Blueprint('auth', __name__)

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

client = WebApplicationClient(GOOGLE_CLIENT_ID)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login')
def login():
    # Get Google's provider configuration
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Generate the Google login URL
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=url_for('auth.callback', _external=True),
        scope=["openid", "email", "profile"],
    )

    return redirect(request_uri)


from oauthlib.oauth2 import WebApplicationClient

client = WebApplicationClient(GOOGLE_CLIENT_ID)

@auth.route('/callback')
def callback():
    # Get the authorization code
    code = request.args.get("code")

    # Get Google's provider configuration
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Exchange the authorization code for an access token
    token_response = client.fetch_token(
        token_endpoint,
        authorization_response=request.url,
        client_secret=GOOGLE_CLIENT_SECRET,
    )

    # Parse the token response and retrieve user information
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    userinfo_response = requests.get(
        userinfo_endpoint,
        headers={"Authorization": f"Bearer {token_response['access_token']}"}
    )

    # Process user info
    userinfo = userinfo_response.json()
    if not userinfo.get("email_verified"):
        return "User email not available or not verified.", 400

    # Find or create a user in the database
    user = User.query.filter_by(email=userinfo["email"]).first()
    if not user:
        user = User(
            email=userinfo["email"],
            name=userinfo["given_name"],
            pfp=userinfo["picture"],
        )
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for("views.home"))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("views.home"))
