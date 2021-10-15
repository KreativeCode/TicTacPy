import socket
import pickle

class Client():
    '''
    Class to handle client
    '''
    HEADER = 4096
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MSG = '!DISCONNECT'
    SERVER = '192.168.86.42'
    ADDR = (SERVER, PORT)

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def make_move(self):
        row = int(input('Enter row of move:'))
        col = int(input('Enter column of move:'))

        move = pickle.dumps((row, col))
        move_string = bytes(f"{len(move):<{self.HEADER}}", 'utf-8') + move
        print(move_string)
        self.client.send(move)

    def invalid_turn(self):
        print("bad move")

    def game_over(self, result):
        if result == 0:
            print("You Win!")
        else:
            print("You Lose!")

    def get_server_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # create socket (type of address, method)
            self.client = s
            s.connect(self.ADDR)

    def play_game(self):
        while self.client.recv(self.HEADER):
            msg = self.client.recv(self.HEADER)
            msg = pickle.loads(msg)
            print(msg)
            flag = msg[0]
            board = msg[1]

            print(board)
            if flag == 0: #P_WAIT:
                print("Waiting for the other player...")
            elif flag == 1: #P_YOUR_TURN:
                print("Your move...")
                self.make_move()
            elif flag == 2: #P_INVALID;
                self.invalid_turn()
            elif flag == 3: #P_GAME_OVER;
                result = msg[2]
                self.game_over(result)
