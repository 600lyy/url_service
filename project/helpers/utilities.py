import datetime
import logging
from logging.handlers import RotatingFileHandler
from dateutil.tz import tzlocal
import pytz
from .settings import SETTINGS


tz_stockholm = pytz.timezone("Europe/Stockholm")


def get_logger():
    logger = logging.getLogger('root')
    FORMAT = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)s - " \
             "%(funcName)20s() ] %(message)s"
    logging.basicConfig(format=FORMAT)
    handler = RotatingFileHandler(
        'runtime.log', maxBytes=1e8,
        backupCount=10, encoding='utf-8'
    )
    handler.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(handler)
    logger.setLevel(SETTINGS['LOGGING_LEVEL'])
    return logger

logger = get_logger()


def get_current_datetime_in_sweden():
    return datetime.datetime.now(tzlocal()).astimezone(tz_stockholm)
