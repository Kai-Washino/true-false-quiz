from flask import Flask
"""
from pathlib import Path
from flask_migrate import Migrate
from flask_splalchemy import SQLAlchemy

db = SQLAlchemy()
"""

def create_app():    
    app = Flask(__name__)
    # app.config.from_mapping(
    #     SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ"
    #     SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path(__file__) / 'local.sqlite'}"
    #     SQLALCHEMY_TRACK_MODIFICATIONS = False
    # )
    
    # db.init_app(app)
    # Migrate(app, db)

    from apps.answer import views as answer_views
    app.register_blueprint(answer_views.answer, url_prefix="/answer")

    return app
