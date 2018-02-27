"""
URL Shortener
Author: Andy Lu
Date: Feb 25 2018
"""

from flask import Flask
from peewee import PostgresqlDatabase
from .helpers.settings import SETTINGS
from .helpers.settings import DB
from .helpers.models import create_tables
from .helpers.models import UrlTable


"""
Configuration of the app
"""

app = Flask(__name__)
create_tables(tables=[ UrlTable ])

@app.before_request
def _db_connect():
    DB.connect()


@app.teardown_request
def _db_close(exc):
    if not DB.is_closed():
        DB.close()


from . import views
