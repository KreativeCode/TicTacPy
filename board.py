class Board:
    """docstring for Board."""

    EMPTYSLOTCHAR = '-'

    def __init__(self, size):
        self.size = size
        self.board = self.create_board()

    def create_board(self):
        '''creates board'''
        return [[self.EMPTYSLOTCHAR for i in range(self.size)] for j in range(self.size)]

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

    def check_win(self, decorator):
        '''check win'''
        for indexes in self.win_indexes(self.size):
            if all(self.board[r][c] == decorator for r, c in indexes):
                return True
        return False


    def win_indexes(self):
        '''returns a generator containing the possible index combinations
           for winning in a a few different patterns'''

        #check rows
        for r in range(self.size):
            yield [(r, c) for c in range(self.size)]
        #check columns
        for c in range(self.size):
            yield [(r, c) for r in range(self.size)]

        #check diagonal top left to bottom right
        yield [(i, i) for i in range(self.size)]
        #check diagonal top right to bottom left
        yield [(i, self.size - 1 - i) for i in range(self.size)]
