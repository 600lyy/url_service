from flask import render_template, request, redirect
from datetime import datetime
from . import app
from .helpers.utilities import url_checker, logger, short_string_generator
from .helpers.models import UrlTable


host = 'http://localhost:5000/'


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    # This function handls imcoming request to visit the main page
    # It returns the short url if the long url match is found in database, 
    # otherwise it returns the home page
    """
    if request.method == "POST":
        original_url = str(request.form.get('url'))
        stored_url = (
            UrlTable
            .select()
            .where(UrlTable.long_url == original_url)
        )
        if not stored_url.exists(): 
            if 'http://' in original_url or'https://' in original_url:
                url = original_url
            else:
                url = ''.join(['http://', original_url])
            is_valid = url_checker(url)
            if is_valid is True:
                short_url = short_string_generator()
                try:
                    UrlTable.create(
                        long_url=original_url,
                        short_url=short_url,
                        created_utc=datetime.utcnow()
                    )
                    return render_template('home.html', short_url=short_url)
                except Exception as e:
                    logger.warning("Cannot save {} to the database".format(original_url))
                    return render_template('home.html')
            else:
                return render_template("home.html", error_msg=True)
        else:
            short_url = stored_url[0].short_url
            logger.info("{} found in the database, no need to insert again".format(short_url))
            return render_template('home.html', short_url=short_url)
    return render_template("home.html")


@app.route('/<short_url>')
def redirect_short_url(short_url):
    """
    # this function is to redirect the short url to its long url
    # if the match is found in the database, otherwise it returns 403 error
    """
    stored_url = (
        UrlTable
        .select()
        .where(UrlTable.short_url == short_url)
    )
    if not stored_url.exists():
        logger.warning("{} not found in the database".format(short_url))
        return render_template("404.html")
    long_url = stored_url[0].long_url
    if 'http://' in long_url or 'https://' in long_url:
        url = long_url
    else:
        url = ''.join(['http://', long_url])
    logger.info("{} found in the database, redirecting to {}".format(short_url, url))
    return redirect(url)
