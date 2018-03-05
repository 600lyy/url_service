import datetime
import logging
import requests
from requests import (HTTPError, ConnectionError, Timeout, RequestException)
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


def url_checker(long_url):
    """
    # This function checks URL whether it's a valid URL or not. It sends a
    # request to the URL with a defined Header. If the URL response code is
    # below 400, something like 200, 301 etc then it's valid. Otherwise, the
    # URL is treated as invalid
    """
    try:
        r = requests.get(long_url, timeout=15)
        return (r.status_code < 400)
    except ConnectionError:
        logger.warning("HTTP towards {} encounters connectionEoor".format(long_url))
        return False
    except HTTPError:
        logger.warning("HTTP towards {} encounters HTTPError".format(long_url))
        return False
    except Timeout:
        logger.warning("HTTP towards {} encounters Timeout".format(long_url))
        return False
    except RequestException as e:
        logger.warning("HTTP towards {} encouunters {}".format(long_url, str(e)))
