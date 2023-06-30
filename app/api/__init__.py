from flask import Blueprint
from flask import Flask
from .image import image

api = Blueprint("api",__name__,url_prefix="/api/v1")

def initialize(app: Flask):
    app.register_blueprint(api)

api.register_blueprint(image)