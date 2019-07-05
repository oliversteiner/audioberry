import audioberry.socketServer as socketServer
import socket

from audioberry.rasperryPyIO import run

PORT = 8882


# Function to display hostname and
# IP address
def get_Host_IP():
    host_ip = 'localhost'
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    except:
        print("Unable to get Hostname and IP")
    return host_ip


#
#
def welcomeMessage():
    print("\n===========================")
    print("==   AudioBerry v0.1.0   ==")
    print("===========================\n")


#
#
def byeMessage():
    print("\n Bye ")
    print("===========================")
    print("\n")


#
#
def main():
    welcomeMessage()
    run()

    # run Socket-IO Server
  #  socketServer.web.run_app(socketServer.app, host=get_Host_IP(), port=PORT)
    print("")


# start
main()
byeMessage()
