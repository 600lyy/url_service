# url_shortener
Building docker-compose based Microservices for a Flask web application

# Requirements

To build a user-facing web service that takes a URL and provides a shorter URL, when possible. When resolved, that URL should redirect the user to the original URL.

- The service should have a user-facing website (but the graphical design won't matter)
- When given a long URL, the service should shorten it and return the shortened URL
- Visiting the shortened URL should redirect the visitor to the long URL
- You should provide source code as well as a link to a running instance of your service
- You do, of course, not need to register a short domain name


## Database Setup:

- Alternative 1: Follow this tutorial to set up your PostgreSQL role & database
		[https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
```
#!bash

# To solve the issue regarding 'password authentication failed for user postgres' when running models.py
# a password must be assigned to the user postgres
$ sudo -u postgres psql
$ ALTER USER postgres PASSWORD 'passwd'
```

# Running the environment

Docker and docker-compose must be installed in your machine, after that, run this command `docker-compose build && docker-compose up -d`.
Wait 2 seconds for postgresql container to be ready.
The url shortener can be accessed via http://localhost:5000/