# Microblog

A simple microblog built using Flask. Made to refresh my Flask knowledge ;)

<img src="https://i.ibb.co/HH42FpT/rsz-screenshot-from-2021-03-21-13-12-10.png" width="50%"/>

## Technologies Used:

- Flask
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy
- Jinja2
- Bootstrap etc.

## Features:

- Login
- Register
- Create, Read, Update, and Delete Post
- Account Management (Read, Update)
- View posts of other users
- Logout

## How to use it

- Click on `Code` > `Download ZIP`
- Unzip it and open Terminal (I am using `bash`)
- `cd` to the root folder (ie, `cd` to `Microblog-main/` from where you are standing.)
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `export FLASK_APP='manage.py'`
- `flask db init`
- `flask db migrate`
- `flask db upgrade`
- Finally, `python manage.py`
- Visit http://localhost:8000 in your browser and `Register` an account an create `New Post`!

# For Interesting Python & JS project based tutorials, visit https://thecodingpie.com
