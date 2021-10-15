class TicTacToe():
    """docstring for Board."""

    EMPTYSLOTCHAR = '-'
    PLAYER_MARKERS = ['X', 'O']

    def __init__(self, size):
        self.size = size
        self.board = self.create_board(size)

    def create_board(self, size):
        '''creates board'''
        return [[self.EMPTYSLOTCHAR for i in range(size)] for j in range(size)]

    def get_board(self):
        return self.board

    def make_move(self, move, player):
        '''place mark on board'''
        x, y = move
        self.board[x][y] = self.PLAYER_MARKERS[player]
        return self.board

    def check_win(self, player):
        '''check win'''
        for indexes in self.win_indexes():
            if all(self.board[r][c] == self.PLAYER_MARKERS[player] for r, c in indexes):
                print('Player '+str(player)+' wins!')
                return True

        if self.is_board_full():
            print('This round ended in a draw')
            return True

        return False

    def win_indexes(self):
        '''returns a generator containing the possible index combinations
           for winning in a few different patterns'''
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

    def validate_move(self, move):
        '''check if move is valid'''
        if not self.is_slot_open(move):
            print('That move has already been made')
            return False

        x, y = move
        if x < 0 or y < 0:
            print('Move can\'t contain negative values')
            return False
        elif x > self.size or y > self.size:
            print('Move can\'t be larger than board size')
            return False

        return True

    def is_slot_open(self, slot):
        '''check if slot on board is empty'''
        x, y = slot
        if self.board[x][y] == self.EMPTYSLOTCHAR:
            return True
        return False

    def is_board_full(self):
        '''check if board is full'''
        for row in self.board:
            if self.EMPTYSLOTCHAR in row:
                return False
        return True
