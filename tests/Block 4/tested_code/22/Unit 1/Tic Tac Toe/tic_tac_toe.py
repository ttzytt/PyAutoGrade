

from tic_tac_toe_functions import *








board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
move_number = 0 
player = 'x'


while True:  
    draw_board(board)


    
    next_move = get_move(player)
    
    success = make_move(player, next_move, board)
    
    
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)


    move_number = move_number + 1 

    print(find_winner(board))
    if find_winner(board) == 'x':
        print('The x player wins!')
        break
    if find_winner(board) == 'o':
        print('The o player wins!')
        break
    if find_winner(board) == None and move_number == 9:
        print('No winner')
        break
        

    
    player = next_player(player)





