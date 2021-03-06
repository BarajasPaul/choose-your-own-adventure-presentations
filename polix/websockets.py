from flask_socketio import emit
from flask_socketio import join_room, leave_room

from . import socketio
from .views import broadcast_vote_count

@socketio.on('connect', namespace='/polix')
def ws_connect():
    pass

@socketio.on('disconnect', namespace='/polix')
def ws_disconnect():
    pass


@socketio.on('join', namespace='/polix')
def on_join(data):
    vote = data['vote']
    join_room(vote)
    broadcast_vote_count(vote)

