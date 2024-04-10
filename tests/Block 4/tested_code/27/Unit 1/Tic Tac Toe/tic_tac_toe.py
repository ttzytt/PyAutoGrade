

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
number_played = 0


while find_winner(board) is None and number_played < 9:
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while success is not True:
        print('That is not a valid move.')
        print()
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)
    number_played += 1



draw_board(board)
print()



if number_played == 9:
    print('The game ties.')
else:
    print('The '+ next_player(player) +' player wins!')

