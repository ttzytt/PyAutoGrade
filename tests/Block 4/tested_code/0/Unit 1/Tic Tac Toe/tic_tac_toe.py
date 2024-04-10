

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'


while find_winner(board) == None and all_filled(board) != True:  
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)




draw_board(board)
if all_filled(board) == True:
    print()
    print('Its a tie!')
else:
    print()
    print('The ' + find_winner(board) + ' player wins!')

