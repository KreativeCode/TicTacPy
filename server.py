import socket
import threading
import pickle
from TicTacToe import TicTacToe

class Server:
    HEADER = 4096 # amount of bytes that the server will receive stating the bytes that the next message would be
    FORMAT = 'utf-8'
    DISCONNECT_MSG = '!DISCONNECT'

    def __init__(self, port):
        self.port = port # select port that isn't being used
        self.server_ip = socket.gethostbyname(socket.gethostname()) # get IP of current machine
        print(self.server_ip)
        self.addr = (self.server_ip, self.port) # used to bind the socket. needs to be in tuple

    def start_subserver(self, client1_sock, client2_sock):
        '''
        Method to create a subserver that will handle each game
        '''
        curr_sock = client1_sock
        waiting_sock = client2_sock
        curr_player = 0
        waiting_player = 1

        game = TicTacToe(3)
        board = game.get_board()

        while True:
            self.send_move_msg(curr_sock, board)
            self.send_wait_msg(waiting_sock, board)

            move = self.recv_move(curr_sock)
            print(move)
            if game.validate_move(move):
                board = game.make_move(move, curr_player)
                if game.check_win(curr_player):
                    self.send_game_over_msg(curr_sock, board, 0)
                    self.send_game_over_msg(waiting_sock, board, 1)
                    break
                else:
                    curr_sock, waiting_sock = waiting_sock, curr_sock;
                    curr_player, waiting_player = waiting_player, curr_player;
            else:
                self.send_invalid_msg(curr_sock, board)

    def send_wait_msg(self, socket, board):
        msg = []
        msg.append(0)
        msg.append(board)
        msg = pickle.dumps(msg)
        msg = bytes(f"{len(msg):<{self.HEADER}}", 'utf-8') + msg
        socket.send(msg)

    def send_move_msg(self, socket, board):
        msg = []
        msg.append(1)
        msg.append(board)
        msg = pickle.dumps(msg)
        msg = bytes(f"{len(msg):<{self.HEADER}}", 'utf-8') + msg
        socket.send(msg)

    def send_invalid_msg(self, socket, board):
        msg = []
        msg.append(2)
        msg.append(board)
        msg = pickle.dumps(msg)
        msg = bytes(f"{len(msg):<{self.HEADER}}", 'utf-8') + msg
        socket.send(msg)

    def send_game_over_msg(self, socket, board, flag):
        msg = []
        msg.append(3)
        msg.append(board)
        msg.append(flag)
        msg = pickle.dumps(msg)
        msg = bytes(f"{len(msg):<{self.HEADER}}", 'utf-8') + msg
        socket.send(msg)

    def recv_move(self, socket):
        data = socket.recv(self.HEADER)
        data_array = pickle.loads(data)
        print(data_array)
        return data_array

    def start(self):
        print('Server is starting....')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # create socket (type of address, method)
            s.bind(self.addr) # bind socket to address. anything using address will use socket

            s.listen()
            print(f'[LISTENING] Server is listening on {self.server_ip}')

            client1_sock = 0
            client2_sock = 0

            while True:
                if client1_sock == 0:
                    client1_sock, addr = s.accept()
                    print('Received connection from first client.')

                    # TODO: Tell client 1 to wait for second client
                else:
                    client2_sock, addr = s.accept()
                    print('Received connection from second client.')

                    thread = threading.Thread(target=self.start_subserver, args=(client1_sock, client2_sock))
                    thread.start()
                    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

                    client1_sock, client2_sock = (0, 0)


server = Server(5050)
server.start()
