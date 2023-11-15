from move import *
from board_state import *
from consts import *

def main():

    board = generate_board()
    print_board(board)


def apply_move(board, move, move_transform, position):
    peice = board[position[0]][position[1]]
    if(peice == 0):
        return False
    if(peice < 3):
        change = move.transforms[move_transform]
    else:
        change = move.flipped[move_transform]
    new_position = [position[0] + change.x, position[1] + change.y]
    if(new_position[0] < 0 or new_position[0] > 4 or new_position[1] < 0 or new_position[1] > 4):
        return False
    board[new_position[0]][new_position[1]] = peice
    board[position[0]][position[1]] = 0
    return True


def generate_board():
    ret = [ [4,4,3,4,4],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [2,2,1,2,2]]
    return ret

def print_board(board):
    print("+---+---+---+---+---+")
    for i in range(5):
        print(end="| ")
        for j in range(5):
            if(board[i][j] == 0):
                print(" ", end=" | ")
            elif(board[i][j] == 1):
                print(chr(30), end=" | ")
            elif(board[i][j] == 2):
                print(chr(24), end=" | ")
            elif(board[i][j] == 3):
                print(chr(31), end=" | ")
            elif(board[i][j] == 4):
                print(chr(25), end=" | ")
        print("\n+---+---+---+---+---+")




if __name__ == '__main__':
    main()
