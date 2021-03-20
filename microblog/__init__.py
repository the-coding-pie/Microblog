import os
from flask import Flask

# application factory function
def create_app():
    app = Flask(__name__)
    
    from microblog.main import main
    
    app.register_blueprint(main)

    return app