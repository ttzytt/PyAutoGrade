

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
winner = None
is_full = False


while winner == None and not is_full: 
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board) 
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    winner = find_winner(board)
    player = next_player(player)
    
    
    is_full = True
    for i in range(3):
        for j in range(3): 
            if board[i][j] == ' ':
                is_full = False

draw_board(board)
print()
if is_full == True:
    print("It's a tie!")
else:
    print('The ' + winner + ' player wins!')

