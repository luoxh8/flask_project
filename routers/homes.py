from flask import (Blueprint, render_template, request, session)
from flask_socketio import close_room, disconnect, emit, join_room, leave_room, rooms

from core.extra import io, thread_lock

homes = Blueprint('homes', __name__, url_prefix='/homes')
thread = None


@homes.route('/')
def index():
    return render_template('index.html', async_mode=io.async_mode)


def background_thread():
    """
        Example of how to send server generated events to clients.
    """
    count = 0
    while True:
        io.sleep(10)
        count += 1
        io.emit('my_response', {'data': 'Server generated event',
                                'count': count},
                namespace='/test')


@io.on('my_event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': message['data'],
                         'count': session['receive_count']})


@io.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': message['data'],
                         'count': session['receive_count']},
         broadcast=True)


@io.on('join', namespace='/test')
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'In rooms: ' + ', '.join(rooms()),
                         'count': session['receive_count']})


@io.on('leave', namespace='/test')
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'In rooms: ' + ', '.join(rooms()),
                         'count': session['receive_count']})


@io.on('', namespace='/test')
def close(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         room=message['room'])
    close_room(message['room'])


@io.on('my_room_event', namespace='/test')
def send_room_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': message['data'],
                         'count': session['receive_count']},
         room=message['room'])


@io.on('disconnect_request', namespace='/test')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response', {'data': 'Disconnected!',
                         'count': session['receive_count']})
    disconnect()


@io.on('my_ping', namespace='/test')
def ping_pong():
    emit('my_pong')


@io.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = io.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected',
                         'count': 0})


@io.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


@io.on('message')
def handle_message(message):
    print('received message: ' + message)
