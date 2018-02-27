#!/usr/bin/env python3

import datetime
import os
import sys

from peewee import CharField, TextField, BooleanField
from peewee import DateTimeField, TimeField
from peewee import Model
from peewee import PrimaryKeyField
from peewee import fn

from .settings import SETTINGS
from .settings import DB
from .utilities import logger


class BaseModel(Model):
    class Meta:
        database = SETTINGS['DB']


class UrlTable(BaseModel):
    """Url table
    """
    id = PrimaryKeyField()
    short_url = CharField(max_length=200, unique=True)
    long_url = CharField(max_length=200, unique=True)
    created_utc = DateTimeField(default=datetime.datetime.utcnow)
    modified_utc = DateTimeField(null=True)


def create_tables(tables=None, reset=False):
    if tables is None:
        logger.warn('No table to create')
        return
    for table in tables:
        if not table.table_exists():
            table.create_table()
            logger.info("Table {0} is created".format(table.__name__))
        elif reset:
            table.drop_table(cascade=True)
            logger.info("Existing Table {0} is dropped".format(table.__name__))
            table.create_table()
            logger.info("Table {0} is re-created".format(table.__name__))
        else:
            logger.info("Table {0} already existed, skipping recreation".format(table.__name__))


if __name__ == '__main__':
    r = input(
        'Deleting and initializing tables, press Enter to continue...\n')
    if r:
        print('Aborted')
        sys.exit(1)
    tables = [ UrlTable ]
    create_tables(tables=tables, reset=True)
    DB.close()
    