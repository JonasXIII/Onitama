from consts import *

def print_board(board):
    print("+---+---+---+---+---+")
    for i in range(5):
        print(end="| ")
        for j in range(5):
            if(board[i][j] == space):
                print(" ", end=" | ")
            elif(board[i][j] == red_big):
                print(chr(30), end=" | ")
            elif(board[i][j] == red_small):
                print(chr(24), end=" | ")
            elif(board[i][j] == blue_big):
                print(chr(31), end=" | ")
            elif(board[i][j] == blue_small):
                print(chr(25), end=" | ")
        print("\n+---+---+---+---+---+")