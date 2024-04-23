

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
winner = None

while winner is None:
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)
    winner = find_winner(board)




draw_board(board)
print()
if(winner != 'tie'):
    print('The ' + str(winner) + ' player wins!')

else:
    print('I\'m sorry, no one wins.')
    
