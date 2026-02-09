from flask import Flask
from app.extensions import db, migrate, jwt, bcrypt
from app.config import Config
from app.routes.todo_routes import api_bp
import os
from app.models.user import User
from app.models.todo import Task

from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(api_bp, url_prefix="/api")

    return app