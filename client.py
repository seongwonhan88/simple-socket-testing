import socket


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))

    msg = s.recv(1024)
    # msg received is in bytes. convert this into hex after allocation
    # check the document for handling hex form
    # https://docs.python.org/3/library/stdtypes.html#bytes.hex

    print(msg) # bytes form
    print(msg.hex()) # hex form


connect()

