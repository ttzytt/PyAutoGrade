

from tic_tac_toe_functions import *




board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
count = 1
winner = None


while count < 10 and winner == None:
    draw_board(board)
    
    
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
        
    player = next_player(player)
    winner = find_winner(board)
    count = count + 1
    


draw_board(board)
print()
if winner == None:
    print("You tied.")
else:
    print('The winner is player ' + str(winner) + '!')

