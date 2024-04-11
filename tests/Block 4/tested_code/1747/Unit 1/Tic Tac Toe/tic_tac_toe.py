

from tic_tac_toe_functions import *


board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'

steps = 0


while not (find_winner(board) != None or steps > 8):  
    draw_board(board)

    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
        
    player = next_player(player)
    steps += 1




draw_board(board)
print()

if find_winner(board) == 'x':
    print('The x player wins!')
elif find_winner(board) == 'o':
    print('The o player wins!')
else:
    print('This is a tie.')
