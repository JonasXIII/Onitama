from consts import *
from move import *


class Board:
    def __init__(self):
        self.board = [[blue_small,blue_small,blue_big,blue_small,blue_small],
                      [space,space,space,space,space],
                      [space,space,space,space,space],
                      [space,space,space,space,space],
                      [red_small,red_small,red_big,red_small,red_small]]
    def clone(self):
        ret = Board()
        for i,row in enumerate(self.board):
            for j,peice in enumerate(row):
                ret.board[i][j] = peice
        return ret


class Board_state:
    
    def __init__(self, board = Board(), red_moves = [all_moves[0], all_moves[1]], blue_moves = [all_moves[2], all_moves[3]], extra_move = all_moves[4], turn = 0):
        self.board = board
        self.moves = generate_moves()
        self.red_moves = red_moves
        self.blue_moves = blue_moves
        self.extra_move = extra_move
        self.turn = turn

    def clone(self):
        ret = Board_state(self.board.clone(), self.red_moves.copy(), self.blue_moves.copy(), self.extra_move, self.turn)
        return ret

    def apply_move(self, move, move_transform, position):
        peice = self.board.board[position[0]][position[1]]
        if(peice == space):
            return False
        if(peice == red_big or peice == red_small):
            if(self.turn == 1):
                return False
        if(peice == blue_big or peice == blue_small):
            if(self.turn == 0):
                return False
        change = move.transforms[move_transform] if turn==0 else move.flipped[move_transform]
        new_position = [position[0] + change.x, position[1] + change.y]
        if(new_position[0] < 0 or new_position[0] > 4 or new_position[1] < 0 or new_position[1] > 4):
            return False
        self.board.board[new_position[0]][new_position[1]] = peice
        self.board.board[position[0]][position[1]] = space
        return True

