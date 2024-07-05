from flask import Flask
from flask_cors import CORS
from .module.createFrame import chatFrameBp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(chatFrameBp)
    return app