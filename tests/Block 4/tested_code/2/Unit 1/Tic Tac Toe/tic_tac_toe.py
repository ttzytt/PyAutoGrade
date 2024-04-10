

from tic_tac_toe_functions import *

rounds = 0


board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'


while find_winner(board) is None and rounds < 9:  
    draw_board(board)
    next_move = get_move(player)
    
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
        
    player = next_player(player)
    rounds = rounds + 1



winner = find_winner(board)
draw_board(board)
print()
print('The ' + winner + ' player wins!')

