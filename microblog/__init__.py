import os
from flask import Flask
from microblog.config import Config

# application factory function
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from microblog.blog import blog
    
    app.register_blueprint(blog)

    return app