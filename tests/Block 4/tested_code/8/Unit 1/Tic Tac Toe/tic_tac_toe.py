

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'

turns_played = 0


while not (find_winner(board) == 'x' or find_winner(board) == 'o' or turns_played == 9):  
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)
    turns_played += 1

        

draw_board(board)
print()

if turns_played < 9:
    print('The ' + str(find_winner(board)) + ' player wins!')
else:
    print('Tie!')


