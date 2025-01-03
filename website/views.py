from flask import Blueprint, render_template, request
from flask_login import current_user

view = Blueprint('view', __name__)

@view.route('/')
def home():
    if current_user.is_authenticated:

        user_id = request.args.get("user_id", current_user.id)
        name = request.args.get("name", current_user.name)

        return render_template('home_logged_in.html', user_id=user_id, name=name)
    else:

        return render_template('home_anonym.html')