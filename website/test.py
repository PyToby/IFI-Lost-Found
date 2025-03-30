from flask import Flask,render_template

@app.route("/goog")
def goog():
    return "Is here, in my arms"