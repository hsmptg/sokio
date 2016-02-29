from flask import Flask
from config import config
from flask.ext.sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch()


db = SQLAlchemy()
socketio = SocketIO()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    socketio.init_app(app, async_mode='eventlet')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
