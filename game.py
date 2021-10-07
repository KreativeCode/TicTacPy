from board import Board
from player import Player

class Game:
    def __init__(self):
        size = int(input('Enter board size: '))
        self.board = Board(size)
        self.player1 = 0
        self.player2 = 1

    def get_next_move(self, player):
        move_is_valid = False
        while move_is_valid == False:
            coordinates_string = input('Enter marker coordinates (\'row, column\'): ')
            coordinates = tuple(int(x) for x in coordinates_string.split(','))

            move_is_valid = self.board.is_input_valid(coordinates)

        return coordinates

    def display_board(self):
        self.board.print_board()

    def make_move(self, player, coordinates):
        self.board.place_mark(player, coordinates)

    def start(self):
        game_over = False
        curr_player = self.player1
        while game_over == False:
            mark_coordinates = self.get_next_move(curr_player)

            self.board.place_mark(mark_coordinates, curr_player)
            self.display_board()
            game_over = self.board.check_win(curr_player)

            if curr_player == self.player1:
                curr_player = self.player2
            else:
                curr_player = self.player1
