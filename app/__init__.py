from flask import Flask

def create_app():
    app = Flask(__name__)
    initialize_controllers(app)
    return app

def initialize_controllers(app: Flask):
    from app import api
    api.initialize(app)