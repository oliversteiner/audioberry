import audioberry.socketServer as socketServer

HOST = '10.0.1.30'
PORT = 8882


def welcomeMessage():
    print("")
    print("===========================")
    print("==   AudioBerry v0.1.0   ==")
    print("===========================")
    print("")

def byMessage():
    print("\n Bye ")
    print("===========================")
    print("\n \n")

def main():
    welcomeMessage()

    # run Socket-IO Server
    socketServer.web.run_app(socketServer.app, host=HOST, port=PORT)
    print("")


main()
byMessage()
