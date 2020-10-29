from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = MongoEngine()
login_manager = LoginManager()
bcrypt = Bcrypt()

from flask_app.main.routes import main  # Blueprint class
from flask_app.users.routes import users

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py", silent=False)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(users)

    login_manager.login_view = "users.login"

    return app
