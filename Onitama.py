from move import *
from board_state import *
from consts import *
from out_put import *

def main():

    board = Board_state()
    print_board(board.board.board)
    legal_moves = board.generate_legal_moves()
    board = board.apply_move(legal_moves[0])
    print_board(board.board.board)








if __name__ == '__main__':
    main()
