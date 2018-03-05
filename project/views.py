from flask import render_template, request, redirect
from . import app
from .helpers.utilities import url_checker


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
        url = original_url if 'http://' in original_url else ''.join(['http://', original_url])
        is_valid = url_checker(url)
        if is_valid is True:
            return render_template('home.html', short_url=host)
        else:
            return render_template("home.html")
    return render_template("home.html")


@app.route('/<short_url>')
def redirect_short_url(short_url):
    """
    # this function is to redirect the short url to its long url
    # if the match is found in the database, otherwise it returns 403 error
    """
    return redirect("http://www.google.se")
