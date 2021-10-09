import socket

class Client():
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MSG = '!DISCONNECT'
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket (type of address, method)
        self.client.connect(self.ADDR)

    def send_move(self, move):
        msg = move.encode(self.FORMAT)
        msg_length = len(msg)
        msg_length = str(msg_length).encode(self.FORMAT)
        msg_length += b' ' * (self.HEADER - len(msg_length))
        self.client.send(msg_length)
        self.client.send(msg)
