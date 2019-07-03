import audioberry.socketServer as socketServer

HOST = 'localhost'
PORT = 8882


def welcomeMessage():
    print("")
    print("===========================")
    print("==   AudioBerry v0.1.0   ==")
    print("===========================")
    print("")


def main():
    welcomeMessage()

    # run Socket-IO Server
    socketServer.web.run_app(socketServer.app, host=HOST, port=PORT)
    print("")


main()
print("")
print("bye ")
print("")
