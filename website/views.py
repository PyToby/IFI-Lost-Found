from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

view = Blueprint('view', __name__)

@view.route('/')
def home():
        if current_user.is_authenticated:
            user_id = request.args.get("user_id", current_user.id)
            name = request.args.get("name", current_user.name)
            pfp = request.args.get("pfp", current_user.pfp)
            return render_template('home.html', user_id=user_id, name=name, pfp=pfp, current_user=current_user)
        else:
            return render_template('home.html', current_user=current_user)

@login_required
@view.route('/profil')
def profil():
    return render_template('profile.html', name=current_user.name, pfp=current_user.pfp)