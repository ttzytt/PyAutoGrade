

from tic_tac_toe_functions import *
i = 0


board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'


while (find_winner(board)) != 'x' and (find_winner(board)) != 'o' and i<9 :
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    i += 1
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)
    


if find_winner(board) == 'x':
    draw_board(board)
    print("x player wins")
elif find_winner(board) == 'o':
    draw_board(board)
    print("o player wins")
elif find_winner(board) is None:
    draw_board(board)
    print("no player wins")





