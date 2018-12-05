"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Kainos.views
from flask import Flask, render_template, redirect, url_for, request


