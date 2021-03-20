import os
from flask import Flask
from microblog.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()

login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please Login to Continue...'
login_manager.login_message_category = 'info'

# application factory function
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from microblog.blog import blog
    from microblog.auth import auth
    
    app.register_blueprint(blog)
    app.register_blueprint(auth)

    return app