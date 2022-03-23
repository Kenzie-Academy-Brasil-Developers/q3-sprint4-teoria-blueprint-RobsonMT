from flask import Flask
from app.routes.hello_blueprint import bp as bp_hello
from app.routes.world_blueprint import bp as bp_world




def init_app(app: Flask):
    app.register_blueprint(bp_hello)
    app.register_blueprint(bp_world)
