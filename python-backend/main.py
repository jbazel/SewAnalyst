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
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    processData("sampleData.csv")

    FlaskUI(app=app, server="flask").run()

   
