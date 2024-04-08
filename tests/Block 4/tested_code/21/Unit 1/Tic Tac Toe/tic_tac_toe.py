

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'


def is_board_full(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == ' ':
                return False

    return True



while find_winner(board) is None   and   not is_board_full(board):  
    draw_board(board)
    next_move = get_move(player)
    
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)

    player = next_player(player)



draw_board(board)


if find_winner(board):
    print('The ' + find_winner(board) + ' player wins!')
else:
    print('It is a draw!')

