


from tic_tac_toe_functions import *


board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
time = 0


while not (find_winner(board) != None or time == 9):  
    draw_board(board)
    
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    
    while not success: 
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
        
    player = next_player(player)
    time += 1


draw_board(board)


if (find_winner(board)) == 'x':
    print('The x player wins!')
elif (find_winner(board)) == 'o':
    print('The o player wins!')
else:
    print('No player wins!')
        






