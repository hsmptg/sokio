import time
from threading import Thread
from flask import render_template
from app.main import main
from .. import db, socketio
from app.models import User


thread = None


# This thread works!!!
def background_thread_ok():
    count = 0
    while True:
        time.sleep(5)
        count += 1
        print(count)
        socketio.emit('counter', {'data': 'Thread', 'count': count},
                      namespace='/test')


# This thread makes socketio stop emitting!!!
def background_thread_ko():
    # I need the following line to instantiate app
    from manage import app
    count = 0
    while True:
        time.sleep(5)
        count += 1
        print(count)
        # I need the following line to avoid runtime error:
        # "application not registered on db instance and no application bound to current context"
        with app.app_context():
            user = User.query.filter_by(rfid="test").first()
        if user is None:
            print("no user")
        # But now this emit do not work!!! :(
        socketio.emit('counter', {'data': 'Thread', 'count': count},
                      namespace='/test')


@socketio.on('echo', namespace='/test')
def echo(json):
     print('received json: ' + str(json))


@main.route('/')
def index():
    global thread
    if thread is None:
        # change the target in the following line to try both versions:
        #   target=background_thread_ok - socketio.emit() works OK!
        #   target=background_thread_ko - socketio.emit() do no work!!! :(
        thread = Thread(target=background_thread_ko)

        thread.daemon = True
        thread.start()
    return render_template('index.html')
