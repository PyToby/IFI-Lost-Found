from flask import Blueprint, redirect, request, url_for
from flask_login import login_user, logout_user, current_user
from oauthlib.oauth2 import WebApplicationClient
import os
import requests
import json
import logging

from .models import User
from . import db, login_manager

auth = Blueprint('auth', __name__)

ADMIN_EMAILS = os.getenv('ADMIN_EMAILS', '').split(',')
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

# Make sure logs/ directory exists — works locally and on Render
log_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Set up logging
log_path = os.path.join(log_dir, 'app.log')

logging.basicConfig(
    filename='/logs/app.log',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Set up the OAuth2Session with redirect_uri
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/login')
def login():
    logging.info("Login initiated from IP: %s", request.remote_addr)
    # Get Google's provider configuration
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Build the redirect URL for the callback
    redirect_uri = url_for('auth.callback', _external=True)

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    print(f"Redirect URI: {request_uri}")
    return redirect(request_uri)

    
@auth.route('/login/callback')
def callback():
    # Get the authorization code from the query string
    code = request.args.get("code")
    logging.info("Received callback with code: %s", code)

    # Get Google's provider configuration to retrieve the token endpoint
    google_provider_cfg = requests.get(GOOGLE_DISCOVERY_URL).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
    token_endpoint,
    authorization_response=request.url,
    redirect_url=request.base_url,
    code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        email = userinfo_response.json()["email"]
        pfp = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        logging.warning("Unverified email attempted login: %s", email)
        return "User email not available or not verified by Google.", 400

    # Only allow emails from gjk.cz
    allowed_domain = "gjk.cz"  
    if not email.lower().endswith(f"@{allowed_domain}"):
        #return f"Access denied: only {allowed_domain} emails are allowed. Please use a {allowed_domain} to login to IFILAF.", 403
        logging.warning("Unauthorized domain: %s tried to login", email)
        return redirect(url_for("view.access_denied"))
    
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(
            email=email,
            name=users_name,
            pfp=pfp,
            is_admin=(email in ADMIN_EMAILS)
        )
        db.session.add(user)
        db.session.commit()
    else:
        user.is_admin = email in ADMIN_EMAILS

    login_user(user)
    logging.info("User logged in: %s (Admin: %s)", email, user.is_admin)
    return redirect(url_for("view.home", user_id=user.id, name=user.name))

@auth.route('/logout')
def logout():
    logging.info("User logged out: %s", getattr(current_user, 'email', 'unknown'))
    logout_user()
    return redirect(url_for("view.home"))
