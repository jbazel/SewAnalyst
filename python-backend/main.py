# main.py

import csv

import pandas
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




@app.route("/")
def home():
    try:
        return render_template('index.html')
    except Exception:
        print("render template error")

@app.route("/upload")
def upload():
    try:
        return render_template('upload.html')
    except Exception:
        print("render template error")

@app.route("/download")
def download():
    try:
        return render_template('download.html')
    except Exception:
        print("render template error")


if __name__ == "__main__":
    #processData("sampleData.csv")
    try:
        FlaskUI(app=app, server="flask").run()
    except Exception as e:
        print("Flask UI failed to start")
        print(e)




   
