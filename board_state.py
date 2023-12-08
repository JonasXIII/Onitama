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
    
    def __init__(self, board = Board(), red_moves = [all_move_crads[0], all_move_crads[1]], blue_moves = [all_move_crads[2], all_move_crads[3]], extra_move = all_move_crads[4], turn = 0):
        self.board = board
        self.red_moves = red_moves
        self.blue_moves = blue_moves
        self.extra_move = extra_move
        self.turn = turn

    def generate_moves(self):
        ret = []
        for i,row in enumerate(self.board.board):
            for j,peice in enumerate(row):
                if(peice == space):
                    continue
                if(peice == red_big or peice == red_small):
                    if(self.turn == 1):
                        continue
                if(peice == blue_big or peice == blue_small):
                    if(self.turn == 0):
                        continue
                for move in self.red_moves if self.turn == 0 else self.blue_moves:
                    for transform in range(len(move.transforms)):
                        ret.append(Move(move, transform, [i,j]))
        return ret

    def is_legal(self, move):
        piece = self.board.board[move.position[0]][move.position[1]]
        if(piece == space):
            return False
        if(piece == red_big or piece == red_small):
            if(self.turn == 1):
                return False
        if(piece == blue_big or piece == blue_small):
            if(self.turn == 0):
                return False
        change = move.transforms[move.transform] if self.turn==0 else move.transforms_flipped[move.transform]
        new_position = [move.position[0] + change.x, move.position[1] + change.y]
        if(new_position[0] < 0 or new_position[0] > 4 or new_position[1] < 0 or new_position[1] > 4):
            return False
        if(self.board.board[new_position[0]][new_position[1]] == red_big or self.board.board[new_position[0]][new_position[1]] == red_small):
            if(self.turn == 0):
                return False
        if(self.board.board[new_position[0]][new_position[1]] == blue_big or self.board.board[new_position[0]][new_position[1]] == blue_small):
            if(self.turn == 1):
                return False
        return True

    def generate_legal_moves(self):
        all_moves = self.generate_moves()
        ret = []
        for move in all_moves:
            if(self.is_legal(move)):
                ret.append(move)
        return ret

    def clone(self):
        ret = Board_state(self.board.clone(), self.red_moves.copy(), self.blue_moves.copy(), self.extra_move, self.turn)
        return ret

    def apply_move(self, move, move_transform, position):
        peice = self.board.board[position[0]][position[1]]
        change = move.transforms[move_transform] if self.turn==0 else move.transforms_flipped[move_transform]
        new_position = [position[0] + change.x, position[1] + change.y]
        self.board.board[new_position[0]][new_position[1]] = peice
        self.board.board[position[0]][position[1]] = space

        used_move = move
        if self.turn == 0:
            self.red_moves.remove(move)
            self.red_moves.append(self.extra_move)
            self.extra_move = used_move
        else:
            self.blue_moves.remove(move)
            self.blue_moves.append(self.extra_move)
            self.extra_move = used_move
        self.turn = 1 - self.turn

