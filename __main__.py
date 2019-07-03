import audioberry.socketServer as socketServer


def welcomeMessage():
    print("")
    print("===========================")
    print("==   AudioBerry v0.1.0   ==")
    print("===========================")
    print("")


def main():
    welcomeMessage()

    # run Socket-IO Server
    socketServer.web.run_app(socketServer.app)
    print("")


main()
print("")
print("bye ")
print("")
