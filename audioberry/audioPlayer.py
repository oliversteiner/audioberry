import os
import subprocess
import shlex

"""
based on https://www.hackster.io/phfbertoleti/on-line-radio-receiver-in-linux-45c028

"""

# Global variables

PathToControlFile = "/tmp/RadioControl"
MPlayerCommand = "mplayer -input file=/tmp/RadioControl -slave -playlist "

# Playslists' global variables
Playlists = []
NumberOfPlaylists = 0
RadioNames = []
PlaylistTarget = 0


# Function: init of playlists' list
# Params: none
# Return: none
def init_playlist_list():
    global Playlists
    global RadioNames
    global NumberOfPlaylists

    Playlists = []
    NumberOfPlaylists = 0
    RadioNames = []

    # playlist 1
    Playlists.append("http://stream.srg-ssr.ch/drs1/mp3_128.m3u")
    RadioNames.append("DRS 1 SO/AG")

    # playlist 2
    Playlists.append("http://stream.srg-ssr.ch/drs2/mp3_128.m3u")
    RadioNames.append("DRS 2")

    # playlist 3
    Playlists.append("http://stream.srg-ssr.ch/drs3/mp3_128.m3u")
    RadioNames.append("DRS 3")

    NumberOfPlaylists = 3
    return


# Function: play choosen playlst / target playlist
# Params: none
# Return: none
def play_playlist(TgtPlaylist):
    global Playlists
    global MPlayerCommand

    os.system("pkill -f mplayer")
    playlist_cmd = MPlayerCommand + Playlists[TgtPlaylist]

    # starts mplayer process and e direct its stdout to /dev/null
    # (so nothing of mplayer will be displayed, except errors)
    fnull = open(os.devnull, 'w')
    args = shlex.split(playlist_cmd)
    interface_m_player = subprocess.Popen(args, shell=False, stdin=subprocess.PIPE, stdout=fnull,
                                          stderr=subprocess.STDOUT)

    # volume set to 50%
    os.system('echo "volume 50" >' + PathToControlFile)

    return


# Function: create control file of mplayer (fifo file)
# Params: none
# Return: none
def create_control_file():
    if os.path.exists(PathToControlFile):
        return
    try:
        os.mkfifo(PathToControlFile)
    except :
        print("[ERROR] Failed to create control file. Please, check path to this file.")
        exit(1)


# Function:
#
#
def radio_action(data):
    init_playlist_list()
    # play_pause()
    if data['active']:
        if data['id'] == 'button-1':
            play_station(0)
        elif data['id'] == 'button-2':
            play_station(1)
        elif data['id'] == 'button-3':
            play_station(2)
        else:
            print(' - Bluetooh Mode')
    else:
        play_pause()


# Function: play_station
#
#
def play_station(PlaylistTarget):
    create_control_file()
    play_playlist(PlaylistTarget)
    print("-- Playing now: " + RadioNames[PlaylistTarget])


# Function: stop_playing
#
#
def play_pause():
    os.system('echo "pause" > ' + PathToControlFile)
    print('-- stop playing')


def volume_up():
    os.system('echo "volume +10" > ' + PathToControlFile)


def volume_down():
    os.system('echo "volume -10" > ' + PathToControlFile)


def exit():
    os.system('echo "quit 0" > ' + PathToControlFile)
    os.system("pkill -f mplayer")
    exit(1)
