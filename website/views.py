from flask import Blueprint, render_template, request, jsonify,Response,session
from flask_login import current_user, login_required
from .models import Items, db

view = Blueprint('view', __name__)

test_items=[
    {
        "image":"https://upload.wikimedia.org/wikipedia/en/8/8c/Woods_4_Green_Album_Cover_Art.jpg",
        "title":"Death is not the end",
        "info":"prvni It's a new experience\n--DSBM",
        "date":"11.12. 2010"},
    {
        "image":"https://img.freepik.com/free-photo/panorama-shot-canal-lake-pukaki-twisel-surrounded-with-mountains_181624-45343.jpg?semt=ais_rp_50_assets&w=740&q=80",
        "title":"Tužka",
        "info":"Značky Jablko. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.",
        "date":"31.2. 1969"
    },
    {
        "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTY-u4WUn0yLpgXguBYe8AA0Fq_BdgL4MVfiQ&s",
        "title":"Metr",
        "info":"""Mé délky. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.""",
        "date":"-4.13. 2099"
    },
    {
        "image":"https://upload.wikimedia.org/wikipedia/en/8/8c/Woods_4_Green_Album_Cover_Art.jpg",
        "title":"Death is not the end",
        "info":"It's a new experience\n--DSBM",
        "date":"11.12. 2010"},
    {
        "image":"",
        "title":"Tužka",
        "info":" pata Značky Jablko. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.",
        "date":"31.2. 1969"
    },
    {
        "image":"",
        "title":"Metr",
        "info":"""Mé délky. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.""",
        "date":"-4.13. 2099"
    },
    {
        "image":"https://upload.wikimedia.org/wikipedia/en/8/8c/Woods_4_Green_Album_Cover_Art.jpg",
        "title":"Death is not the end",
        "info":"It's a new experience\n--DSBM",
        "date":"11.12. 2010"},
    {
        "image":"",
        "title":"Tužka",
        "info":"osma Značky Jablko. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.",
        "date":"31.2. 1969"
    },
    {
        "image":"",
        "title":"Metr",
        "info":"""Mé délky. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.""",
        "date":"-4.13. 2099"
    },
    {
        "image":"https://upload.wikimedia.org/wikipedia/en/8/8c/Woods_4_Green_Album_Cover_Art.jpg",
        "title":"Death is not the end",
        "info":"It's a new experience\n--DSBM",
        "date":"11.12. 2010"},
    {
        "image":"",
        "title":"Tužka",
        "info":"Značky Jablko. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.",
        "date":"31.2. 1969"
    },
    {
        "image":"https://upload.wikimedia.org/wikipedia/en/8/8c/Woods_4_Green_Album_Cover_Art.jpg",
        "title":"Death is not the end",
        "info":"It's a new experience\n--DSBM",
        "date":"11.12. 2010"},
    {
        "image":"",
        "title":"Tužka",
        "info":"Značky Jablko. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.",
        "date":"31.2. 1969"
    },
    {
        "image":"",
        "title":"Metr",
        "info":"""Mé délky. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.""",
        "date":"-4.13. 2099"
    },
    {
        "image":"https://upload.wikimedia.org/wikipedia/en/8/8c/Woods_4_Green_Album_Cover_Art.jpg",
        "title":"Death is not the end",
        "info":"It's a new experience\n--DSBM",
        "date":"11.12. 2010"},
    {
        "image":"",
        "title":"Tužka",
        "info":"Značky Jablko. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.",
        "date":"31.2. 1969"
    },
    {
        "image":"",
        "title":"Metr",
        "info":"""Mé délky. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.""",
        "date":"-4.13. 2099"
    },
    {
        "image":"https://upload.wikimedia.org/wikipedia/en/8/8c/Woods_4_Green_Album_Cover_Art.jpg",
        "title":"Death is not the end",
        "info":"It's a new experience\n--DSBM",
        "date":"11.12. 2010"},
    {
        "image":"",
        "title":"(posledni)Tužka",
        "info":"Značky Jablko. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nulla pulvinar eleifend sem. Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Nunc dapibus tortor vel mi dapibus sollicitudin. Aenean vel massa quis mauris vehicula lacinia. Nulla est. In laoreet, magna id viverra tincidunt, sem odio bibendum justo, vel imperdiet sapien wisi sed libero. Integer imperdiet lectus quis justo. Sed convallis magna eu sem. Praesent vitae arcu tempor neque lacinia pretium. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. Integer vulputate sem a nibh rutrum consequat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos.",
        "date":"31.2. 1969"
    },
        ]

ITEMS_PER_RELOAD = 7

class Item_Data:
    def __init__(self, name=None, description=None, table=None, type=None, state=None, pictures=None):
        self.name = name
        self.pictures = pictures
        self.description = description
        self.table = table
        self.type = type
        self.state = state


def get_basic_user_info():
    if current_user.is_authenticated:
        return current_user.id, current_user.name, current_user.pfp
    else:
        return None

def get_user_info():
    if current_user.is_authenticated:
        return current_user
    else:
        return None

def is_owner(user,item_email):
    if user.is_admin or user.email == item_email:
        return True
    return False

@view.route('/')
def home():
    session["test_items_index"] = 0

    more_items_available=True
    if len(test_items) <=ITEMS_PER_RELOAD:
        more_items_available=False

    if current_user.is_authenticated:
        user_id, name, pfp = get_basic_user_info()
        return render_template('home.html', user_id=user_id, name=name, pfp=pfp, current_user=current_user,test_items=test_items[0:ITEMS_PER_RELOAD],more_items_available=more_items_available)
    else:
        return render_template('home.html', current_user=current_user,test_items=test_items[0:ITEMS_PER_RELOAD],more_items_available=more_items_available)

@login_required
@view.route('/profil')
def display_profil():
    user_id, name, pfp = get_basic_user_info()
    return render_template('profile.html', name=name, pfp=pfp, user_id=user_id, current_user=current_user)

@view.route('/info')
def display_info():
    user_data = get_basic_user_info()
    if user_data == None:
        return render_template('info.html',current_user=current_user)
    user_id, name, pfp = user_data
    return render_template('info.html', current_user=current_user,user_id=user_id, name=name, pfp=pfp)

@view.route("/load_next_items")
def load_next_items():
    session["test_items_index"] += ITEMS_PER_RELOAD
    test_items_index = session["test_items_index"]
    more_items_available=True
    if test_items_index+ITEMS_PER_RELOAD >= len(test_items):
        more_items_available=False

    return render_template("preview_list.html",test_items=test_items[test_items_index:test_items_index+ITEMS_PER_RELOAD],more_items_available=more_items_available)


@view.route("/item/<int:item_id>") 
def display_item_detail(item_id):

    item = Items.query.filter_by(id=item_id).first()

    table = {
                "date":item.date,
                "location":item.location}

    item_data = Item_Data(item.name, item.description, table, item.type, item.state, item.pictures)
    
    user_data = get_user_info()
    if user_data == None:
        return render_template("display_item.html",current_user=current_user, item_data=item_data)

    item_data.table["email"] = item.user_email


    if is_owner(user_data,item.user_email):
        return render_template("edit_item.html",current_user=current_user,user_id=user_data.id, name=user_data.name, pfp=user_data.pfp, is_admin=user_data.is_admin, item_data=item_data)

    else:
        return render_template("display_item.html",current_user=current_user, user_id=user_data.id, name=user_data.name, pfp=user_data.pfp, item_data=item_data)

@view.route("/item/new")
def display_item_form():
    user_data = get_user_info()
    if user_data == None:
        return render_template("login_required.html",current_user=current_user)

    return render_template("edit_item.html",current_user=current_user,user_id=user_data.id, name=user_data.name, pfp=user_data.pfp, is_admin=user_data.is_admin, item_data=Item_Data())


@view.route("/item/create", methods=["POST"])
def create_item():
    user_data = get_user_info()
    if user_data == None:
        return jsonify({"success": False, "message": "You must be logged in to create an item."}), 403

    # Create a new item with the data from the form
    new_item = Items(
        name=request.form.get("name"),
        description=request.form.get("description"),
        date=request.form.get("date"),
        location=request.form.get("location"),
        type=request.form.get("type"),
        state=request.form.get("state"),
        user_email=user_data.email
    )

    # Add the new item to the database
    db.session.add(new_item)
    db.session.commit()

    return jsonify({"success": True, "message": "Item created successfully.", "item_id": new_item.id})

@view.route("/item/<int:item_id>/delete", methods=["POST"])
def delete_item(item_id):
    item = Items.query.filter_by(id=item_id).first()
    user_data = get_user_info()
    if is_owner(user_data,item.user_email):
        # Delete the item from the database
        db.session.delete(item)
        db.session.commit()
        return jsonify({"success": True, "message": "Item deleted successfully."})
    else:
        return jsonify({"success": False, "message": "You do not have permission to delete this item."}), 403

@view.route("/item/<int:item_id>/edit", methods=["POST"])
def edit_item(item_id):
    item = Items.query.filter_by(id=item_id).first()
    user_data = get_user_info()
    if is_owner(user_data,item.user_email):
        # Update the item with the new data from the form
        item.name = request.form.get("name")
        item.description = request.form.get("description")
        item.date = request.form.get("date")
        item.location = request.form.get("location")
        item.type = request.form.get("type")
        item.state = request.form.get("state")
        db.session.commit()
        return jsonify({"success": True, "message": "Item updated successfully."})

    return jsonify({"success": False, "message": "You do not have permission to edit this item."}), 403

