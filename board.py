class Board:
    """docstring for Board."""

    EMPTYSLOTCHAR = '-'

    def __init__(self, dimensions):
        self.height, self.width = dimensions
        self.board = ''
        self.board = self.create_board()

    def create_board(self):
        '''creates board'''
        self.board = [[self.EMPTYSLOTCHAR for i in range(self.height)] for j in range(self.width)]
        return self.board

    def print_board(self):
        '''print board'''
        for row in self.board:
            print(row)
        print('\n')

    def place_mark(self, coordinates):
        '''place mark on board'''
        if self.is_slot_open(coordinates):
            x, y = coordinates
            self.board[x][y] = 'X'
        else:
            print('Slot not empty')

    def is_board_full(self):
        '''check if board is full'''
        for row in self.board:
            if self.EMPTYSLOTCHAR in row:
                return False
        return True

    def is_slot_open(self, coordinates):
        '''check if slot on board is empty'''
        x, y = coordinates
        if self.board[x][y] == self.EMPTYSLOTCHAR:
            return True
        return False

    def check_win(self):
        '''check win'''
        pass
