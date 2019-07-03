from aiohttp import web
import socketio
import shlex
from subprocess import PIPE, Popen

# Server
PROJECT_ROOT = 'audioberry/web'
HOST = 'localhost'
PORT = 8882

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

# radio
stream_drs1 = "http://stream.srg-ssr.ch/drs1/mp3_128.m3u"
stream_drs2 = "http://stream.srg-ssr.ch/drs2/mp3_128.m3u"
stream_drs3 = "http://stream.srg-ssr.ch/drs3/mp3_128.m3u"


def get_exitcode_stdout_stderr(cmd):
    """
    Execute the external command and get its exitcode, stdout and stderr.
    """
    args = shlex.split(cmd)

    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode
    #
    return exitcode, out, err


# Server
async def index(request):
    """Serve the client-side application."""
    with open('web/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.event
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('message', room=sid)


@sio.on('message')
def another_event(sid, data):
    print("message ", data)
    pass


@sio.on('play-station')
def play_drs1(sid, data):
    URL = stream_drs1
    print("play-station ", data)
    cmd = "mplayer -playlist {url}".format(url=URL)
    out = get_exitcode_stdout_stderr(cmd)[1]
    pass


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


# app.router.add_static('/static/', path=PROJECT_ROOT + '/static',                     name='static')
# app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, host=HOST, port=PORT)
