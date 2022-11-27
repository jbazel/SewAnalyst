# main.py

import pandas as pd
import numpy
import matplotlib
from flask import Flask
from flask import render_template
from flaskwebgui import FlaskUI

app = Flask(__name__)


def processData(rawData):
    """
    perform all analysis on raw data

    """


def dataReport(data):
    """
    take in processed data
    use pandas to generate any data-frames and perform analysis
    return html data forms

    """


def generateFigures(data):
    """
    take in processed data
    generate figures and graphs in matplotlib
    save figures as files to use in HTML report

    """


def generateReport():
    """
    TO DO
    """


@app.route("/")
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    FlaskUI(app=app, server="flask").run()
