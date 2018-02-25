"""
URL Shortener
Author: Andy Lu
Date: Feb 25 2018
"""

from flask import Flask


app = Flask(__name__)
from . import views