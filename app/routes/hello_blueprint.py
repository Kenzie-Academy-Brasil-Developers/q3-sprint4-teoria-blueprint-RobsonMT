from flask import Blueprint
from app.controllers import hello_controller

bp = Blueprint("hello", __name__, url_prefix="/api")

bp.get("/hello")(hello_controller.return_hello)