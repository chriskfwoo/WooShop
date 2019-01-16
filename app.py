from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import api_bp


db = SQLAlchemy()

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    return app
