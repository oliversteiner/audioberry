from aiohttp import web
import socketio

# Server
from audioberry.audioPlayer import radio_action


sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


@sio.event
def connect(sid, environ):
    print("connect ", sid, "\n")


@sio.event
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('message', room=sid)


@sio.on('message')
def another_event(sid, data):
    pass


@sio.on('buttonAction')
def buttonAction(sid, data):
    radio_action(data)
    pass


@sio.event
def disconnect(sid):
    print('disconnect ', sid)