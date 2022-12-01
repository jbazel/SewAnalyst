# main.py

import csv
import pandas as pd
import numpy as np
import matplotlib as plt
from flask import Blueprint, render_template, redirect, session, request, flash, Flask, send_from_directory, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flaskwebgui import FlaskUI
import os
from os.path import join, dirname, realpath


app = Flask(__name__)


def processData(rawData):
    """
    perform all analysis on raw data
    create dataFrames
    analyse
    """

    data = pd.read_csv(rawData, index_col=0, parse_dates=True)


def generateFigures(data):
    """
    take in processed data
    generate figures and graphs in matplotlib
    save figures as files to use in HTML report

    NOTES ON USiNG PANDAS AND MATPLOTLIB TO DRAW PLOTS:

    NOTE: this works on whole data, series, and dataFrame

    plotting all data:
        >data.plot()
        >plt.show()

    plotting only one column:
        >data["<VARIABLE NAME>"].plot()
        >plt.show()

    plotting different graphs:
        >data.plot.<GRAPH/PLOT TYPE>(parameters)
        >plt.shot()

        example:
        >data.plot.scatter(x = <VARIABLE 1>, y = <VARIABLE 2>, ...)
        >plt.show()


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
