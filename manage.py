import os
from app import create_app, socketio
from flask.ext.script import Manager


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


@manager.command
def run():
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False)


if __name__ == '__main__':
    manager.run()
