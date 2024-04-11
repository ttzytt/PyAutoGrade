



from unit_1_project_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'

move_count = 0  
                
big_X = 3  

big_O = 3


while not ((find_winner(board) == 'x' or find_winner(board) == 'o')and not
            (big_X == 0 and big_O == 0 and move_count == 15)):
    draw_board(board)
    next_move = get_move(player)
    
    
    
    if big_X == 0 and player == 'x':
        piece_size = 1
    elif big_O == 0 and player == 'o':
        piece_size = 1
    else:   
        piece_size = get_size(player)
        
    piece = make_piece(player, piece_size)
    
    if piece_size != 1 and piece_size != 2:
        success = False
    else:
        
        success = make_move(piece, next_move, board)
    
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)

        if big_X == 0 and player == 'x':
            piece_size = 1
        elif big_O == 0 and player == 'o':
            piece_size  = 1
        else:   
            piece_size = get_size(player)

        piece = make_piece(player, piece_size)
        if piece_size != 1 and piece_size != 2:
            success = False
        else:
        
            success = make_move(piece, next_move, board)
            
        
        
        
            
                
    
    
    if piece == 'X':
        big_X -= 1
    elif piece == 'O':
        big_O -= 1

    player = next_player(player)
    move_count += 1


    


draw_board(board)
print()
if find_winner(board) != None:
    print(f'The {find_winner(board)} player wins!')
else:
    print('We Draw')


