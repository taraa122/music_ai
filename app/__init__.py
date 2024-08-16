from flask import Flask
from app.routes import bp as routes_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes_bp, url_prefix='/')  # Register with URL prefix
    return app


