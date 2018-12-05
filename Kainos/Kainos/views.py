"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Kainos import app
from flask import redirect, url_for, request
import pandas as pd
import matplotlib as mpl
import numpy as np
import os.path

names = ['Luke', 'Zoe']
dtasets = []
dtaset_name = []

@app.route('/login')
def login():
    """Renders the contact page."""
    return render_template(
        'login.html',
    )
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
    )

@app.route('/upload')
def upload():
    """Renders the contact page."""
    return render_template(
        'upload.html',
    )

@app.route('/download')
def download():
    """Renders the about page."""
    return render_template(
        'download.html',
    )

@app.route('/manipulate')
def manipulate():
    """Renders the about page."""
    return render_template(
        'manipulate.html',
    )

@app.route('/visualise')
def visualise():
    """Renders the about page."""
    return render_template(
        'visualise.html',
    )
# Route for handling the login page logic
def log_in(name):
    for x in range(len(names)):
        if names[x] == name:
            url_for('home')
    
@app.route('/own_csv_exists/<string:csv>') 
def own_csv_exists(csv):
    if os.path.exists(csv + '.csv'):
        dtaset_name.append(csv)
        csv1 = pd.read_csv(csv + '.csv')
        dtasets.append(csv1)
        print("Uploaded")
    else:
        print("Not found")

@app.route('/download_csv/<string:csv_name><string:f_name>')
def download_csv(csv_name, f_name):
    for i in range(len(dtaset_name)):
        if dtaset_name[i] == csv_name + '.csv':
            x = dtasets[i]
            x.to_csv(f_name +'.csv')


