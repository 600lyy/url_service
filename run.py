#! /usr/bin/env python

from project import app
from project import SETTINGS


app.debug = SETTINGS['DEBUG']


if __name__ == "__main__":
    app.run()
