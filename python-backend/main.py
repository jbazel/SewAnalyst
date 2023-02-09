# main.py

import csv

import pandas
import pandas as pd
import numpy as np
import matplotlib as plt
from flask import Blueprint, render_template, redirect, session, request, flash, Flask, send_from_directory, url_for
from wtforms import StringField, SubmitField
from flaskwebgui import FlaskUI
import os
from os.path import join, dirname, realpath

app = Flask(__name__)


@app.route("/")
def home():
    try:
        print("routing to home, attempting to render template")
        return render_template('index.html')
    except Exception:
        print("render template error")


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    try:
        if request.method == 'POST':
            print("here")
            f = request.files['csv file']
            f.save("test.csv")

            return render_template('index.html')

    except Exception as e:
        print(e)


@app.route("/download")
def download():
    try:
        print("routing to download, attempting to render template")
        return render_template('download.html')
    except Exception:
        print("render template error")


if __name__ == "__main__":
    # processData("sampleData.csv")
    try:
        FlaskUI(app=app, server="flask").run()
    except Exception as e:
        print("Flask UI failed to start")
        print(e)
