import socket


def response():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    clientsocket, address = s.accept()
    print(f'Connected from {address} established')

    # this is a sample message. look up link below for sending hex over socket
    # https://stackoverflow.com/questions/8904092/how-can-i-send-anything-other-than-strings-through-python-sock-send
    data = bytes.fromhex('01AF23')

    clientsocket.send(data)
    clientsocket.close()


response()
