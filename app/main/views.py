import time
from threading import Thread
from flask import render_template
from app.main import main

# Is this correct???
from manage import socketio

thread = None


def background_thread():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(count)
        # Do not work!!!
        socketio.emit('my response', {'data': 'Thread', 'count': count},
                      namespace='/test')


# Do not work!!!
@socketio.on('connect', namespace='/test')
def test_connect():
    print("Connected (msg from views.py)")


@main.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.daemon = True
        thread.start()
    return render_template('index.html')
