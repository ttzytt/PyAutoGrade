

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'


slots_filled = 0

winner = False


while not winner and not slots_filled == 9:
    draw_board(board)
    next_move = get_move(player)
    
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)
    
    
    slots_filled += 1

    winner = find_winner(board)
    

draw_board(board)
print()
if winner == None:
    print('There was a tie')
else:
    print('The ' + winner + ' player wins!')
