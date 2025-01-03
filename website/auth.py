from flask import Blueprint, redirect, request, url_for
from flask_login import login_user, logout_user
from requests_oauthlib import OAuth2Session
import os
import requests

from .models import User
from . import db, login_manager

auth = Blueprint('auth', __name__)

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

# Set up the OAuth2Session with redirect_uri
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login')
def login():
    # Get Google's provider configuration
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Build the redirect URL for the callback
    redirect_uri = url_for('auth.callback', _external=True)

    # Create an OAuth2 session with the redirect URI
    oauth = OAuth2Session(
    GOOGLE_CLIENT_ID, 
    scope=[
        "https://www.googleapis.com/auth/userinfo.profile", 
        "https://www.googleapis.com/auth/userinfo.email", 
        "openid"
        ]
    )

    # Generate the authorization URL
    authorization_url, state = oauth.authorization_url(authorization_endpoint)

    # Debug: Log the URL to check it's being generated properly
    print(f"Generated authorization URL: {authorization_url}")

    # Return the redirect to the authorization URL
    return redirect(authorization_url)

@auth.route('/callback')
def callback():
    # Get the authorization code from the query string
    code = request.args.get("code")

    # Get Google's provider configuration to retrieve the token endpoint
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Recreate the OAuth2 session with the same redirect URI
    redirect_uri = url_for('auth.callback', _external=True)
    oauth = OAuth2Session(
        GOOGLE_CLIENT_ID,
        scope=["openid", "email", "profile"],
        redirect_uri=redirect_uri  # Ensure the redirect URI matches
    )

    # Exchange the authorization code for an access token
    token = oauth.fetch_token(
        token_endpoint,
        authorization_response=request.url,
        client_secret=GOOGLE_CLIENT_SECRET,
        redirect_uri=redirect_uri  # Explicitly include redirect_uri
    )

    # Use the token to fetch user info
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    userinfo = oauth.get(userinfo_endpoint).json()

    # Handle user info and login
    if not userinfo.get("email_verified"):
        return "Email not verified", 400

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
