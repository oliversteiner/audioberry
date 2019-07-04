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
    print("chat_message ", data)
    await sio.emit('chat_message', room=sid)


@sio.on('message')
def another_event(sid, data):
    pass


@sio.on('button_action')
async def button_action(sid, data):
    # print(data)
    active_button, display_message = radio_action(data)
    await sio.emit('audioberry_button', active_button, room=sid)
    await sio.emit('audioberry_display', display_message, room=sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)
