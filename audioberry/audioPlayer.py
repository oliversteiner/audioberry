import os
import subprocess
import shlex

import limit as limit

from audioberry.helpers import debounce

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
    Playlists.append("http://stream.srg-ssr.ch/regi_ag_so/aacp_96.asx")
    RadioNames.append("DRS 1:SO/AG")

    # playlist 2
    # Playlists.append("http://stream.srg-ssr.ch/drs2/mp3_128.m3u")
    Playlists.append("http://stream.srg-ssr.ch/drs2/aacp_96.asx")
    RadioNames.append("DRS 2")

    # playlist 3
    # Playlists.append("http://stream.srg-ssr.ch/drs3/mp3_128.m3u")
    Playlists.append("http://stream.srg-ssr.ch/drs3/aacp_96.asx")
    RadioNames.append("DRS 3")

    NumberOfPlaylists = 3
    return


# Function: play choosen playlst / target playlist
# Params:
# Return:
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
    except:
        print("[ERROR] Failed to create control file. Please, check path to this file.")
        exit(1)


# Function:
#
#
def radio_action(data):
    global RadioNames
    # set Radio Stations
    init_playlist_list()
    active_button = 0
    display_message = ''

    # Which button was pressed?
    # Is Button set to On or Off?
    if data['active']:
        # Button is set to on:
        # Button 1
        if data['id'] == 'button-1':
            active_button, display_message = play_station(0)

        # Button 2
        elif data['id'] == 'button-2':
            active_button, display_message = play_station(1)

        # Button 3
        elif data['id'] == 'button-3':
            active_button, display_message = play_station(2)

        # Button Bluetooth
        else:
            stop_playing()
            active_button = '4'
            display_message = "Bluetooth"

    # Button is set to Off -> Stop Playing
    else:
        stop_playing()
        display_message = "Stop"

    return active_button, display_message


def play_station(PlaylistTarget):
    create_control_file()
    play_playlist(PlaylistTarget)
    radioname = RadioNames[PlaylistTarget]
    display_message = radioname
    print("-- Playing now: " + radioname)
    return PlaylistTarget + 1, display_message


def stop_playing():
    os.system('echo "pause" > ' + PathToControlFile)
    print('-- stop playing')


@debounce(wait=0.1)
def set_volume(data):
    print("-- volume_action-", data)
    volume_value = str(data)
    os.system('echo "set_property volume ' + volume_value + '" > ' + PathToControlFile)
    pass


def volume_up():
    os.system('echo "volume +10" > ' + PathToControlFile)


def volume_down():
    os.system('echo "volume -10" > ' + PathToControlFile)


def exit():
    os.system('echo "quit 0" > ' + PathToControlFile)
    os.system("pkill -f mplayer")
    exit(1)
