"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Kainos import app

@app.route('/')
@app.route('/login')
def login():
    """Renders the contact page."""
    return render_template(
        'login.html',
    )

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


