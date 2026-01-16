
from flask import Flask
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/todo_api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Model import
    from . import models

    # Blueprint
    from app.api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api") 

    return app

