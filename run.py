#! /usr/bin/env python

from project import app


app.debug = True


if __name__ == "__main__":
    app.run()