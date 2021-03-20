from flask import Blueprint

blog = Blueprint('blog', __name__)

from microblog.blog import routes, forms