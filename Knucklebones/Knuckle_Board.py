#Define board for knucklebones as a series of columns in a single 2d array
# library imports
import numpy as np

class Knuckle_Board:
    #Constructor
    def __init__(self, size):
        self.size = size
        self.board = self.k_board_init(size)

    #Public Methods
    #place a die

    #print the board

    #get the current board score for a given player
    def get_score(board_curr, player_curr):
        return 0

    #Private Methods
    def k_board_init(self, size):
        k_board = []
        for i in range(2*size):
            if i < (size/2):
                player_new = 0
            else:
                player_new = 1
            column_new = Knuckle_Column(size, player_new)
            k_board.append(column_new)
        return k_board

class Knuckle_Column:
    #Constructor
    def __init__(self, size, player):
        self.size = size
        self.player = player
        self.content = []

    #Public Methods
    #place a die in a column

    #remove a die from a column

    #Private Methods





