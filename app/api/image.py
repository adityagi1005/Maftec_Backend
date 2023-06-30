from flask import Blueprint, request

image = Blueprint("image_routs",__name__, url_prefix="/image")

@image.post("")
def index():
    action = request.args.get("action")
    if action == "upload":
        return "ye lo mere noods"
    
    return ""