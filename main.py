#main.py

import pandas as pd
from flask import Flask
from flask import render_template
from flaskwebgui import FlaskUI

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
    FlaskUI(app=app, server="flask").run()
