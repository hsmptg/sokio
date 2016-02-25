import os
from app import create_app
from flask.ext.script import Manager
from flask_socketio import SocketIO
import eventlet
eventlet.monkey_patch()


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
socketio = SocketIO(app, async_mode='eventlet')
manager = Manager(app)


# Works fine!!!
@socketio.on('connect', namespace='/test')
def test_connect():
    print("Connected (msg from manage.py)")
    # Works fine!!!
    socketio.emit('my response', {'data': 'Connected', 'count': 33}, namespace='/test')


@socketio.on('my event', namespace='/test')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@manager.command
def run():
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False)


if __name__ == '__main__':
    manager.run()
