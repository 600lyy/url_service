"""
URL Shortener
Author: Andy Lu
Date: Feb 25 2018
"""

from flask import Flask
import time
from peewee import PostgresqlDatabase, OperationalError
from .helpers.settings import SETTINGS
from .helpers.settings import DB
from .helpers.models import create_tables
from .helpers.models import UrlTable
from .helpers.utilities import logger


"""
Configuration of the app
"""

app = Flask(__name__)
try:
    time.sleep(2) #  wait 2 seconds for the postgresql container to start properly
    create_tables(tables=[ UrlTable ])
except OperationalError as e:
    logger.warning("Cannot Create Table, Reason: {}".format(str(e)))


@app.before_request
def _db_connect():
    DB.connect()


@app.teardown_request
def _db_close(exc):
    if not DB.is_closed():
        DB.close()


from . import views
