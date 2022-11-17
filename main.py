#main.py

import pandas as pd
from flask import Flask
from flask import render_template
from flaskwebgui import FlaskUI

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('Sewanalyst.html')

@app.route("/home", methods=['GET'])
def home():
    return render_template('Sewanalyst.html')

if __name__ == "__main__":
  FlaskUI(app=app, server="flask").run()

