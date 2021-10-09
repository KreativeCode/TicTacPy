import socket
import threading
from game import Game

class Server:
    HEADER = 64 # amount of bytes that the server will receive stating the bytes that the next message would be
    FORMAT = 'utf-8'
    DISCONNECT_MSG = '!DISCONNECT'

    def __init__(self, port):
        self.port = port # select port that isn't being used
        self.server_ip = socket.gethostbyname(socket.gethostname()) # get IP of current machine
        self.addr = (self.server_ip, self.port) # used to bind the socket. needs to be in tuple

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected...")
        connected = True
        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT) # get length of message that's going to be sent
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)
                if msg == self.DISCONNECT_MSG:
                     connected = False
                print(f'[{addr}] -> {msg}')

        conn.close()

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket (type of address, method)
        self.server_socket.bind(self.addr) # bind socket to address. anything using address will use socket
        print('Server is starting....')
        self.server_socket.listen()
        print(f'[LISTENING] Server is listening on {self.server_ip}')
        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
