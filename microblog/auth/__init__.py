from flask import Blueprint

auth = Blueprint('auth', __name__)

from microblog.auth import routes, forms