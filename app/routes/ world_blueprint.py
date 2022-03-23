from flask import Blueprint
from app.controllers import world_controller

bp = Blueprint("world", __name__, url_prefix="/api")

bp.get("/world")(world_controller.return_world)
