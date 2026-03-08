from flask import Blueprint, render_template, request, jsonify,Response,session
from flask_login import current_user, login_required
view = Blueprint('view', __name__)

test_items=[
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

def get_user_info():
    if current_user.is_authenticated:
        return current_user.id, current_user.name, current_user.pfp
    else:
        return None

@view.route('/')
def home():
    session["test_items_index"] = 0

    more_items_available=True
    if len(test_items) <=ITEMS_PER_RELOAD:
        more_items_available=False

    if current_user.is_authenticated:
        user_id, name, pfp = get_user_info()
        return render_template('home.html', user_id=user_id, name=name, pfp=pfp, current_user=current_user,test_items=test_items[0:ITEMS_PER_RELOAD],more_items_available=more_items_available)
    else:
        return render_template('home.html', current_user=current_user,test_items=test_items[0:ITEMS_PER_RELOAD],more_items_available=more_items_available)

@login_required
@view.route('/profil')
def profil():
    user_id, name, pfp = get_user_info()
    return render_template('profile.html', name=name, pfp=pfp, user_id=user_id, current_user=current_user)

@view.route('/background_process_test')
def background_process_test():
    print("Hello")
    return render_template('profile.html')

@view.route('/info')
def info():
    user_id, name, pfp = get_user_info()
    return render_template('info.html', current_user=current_user,user_id=user_id, name=name, pfp=pfp)

@view.route("/load_next_items")
def load_next_items():
    session["test_items_index"] += ITEMS_PER_RELOAD
    test_items_index = session["test_items_index"]
    more_items_available=True
    if test_items_index+ITEMS_PER_RELOAD >= len(test_items):
        more_items_available=False

    return render_template("preview_list.html",test_items=test_items[test_items_index:test_items_index+ITEMS_PER_RELOAD],more_items_available=more_items_available)

@view.route("/item")
def item():
    user_id, name, pfp = get_user_info()
    return render_template("item.html",current_user=current_user,user_id=user_id, name=name, pfp=pfp)