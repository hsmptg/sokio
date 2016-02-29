import time
from threading import Thread
from flask import render_template
from app.main import main
from .. import socketio


thread = None


def background_thread():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(count)
        socketio.emit('counter', {'data': 'Thread', 'count': count},
                      namespace='/test')


@socketio.on('echo', namespace='/test')
def echo(json):
     print('received json: ' + str(json))


@main.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.daemon = True
        thread.start()
    return render_template('index.html')
