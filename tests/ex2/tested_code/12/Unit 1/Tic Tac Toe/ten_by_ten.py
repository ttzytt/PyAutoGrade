






from ten_by_ten_functions import *



board = [ [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' ']]
player = 'x'
move = input('Choose your first move: ')




while find_winner(board) == None and is_full(board) == False: 

    if make_move(player,move,board) == True: 
        
        make_move(player,move,board) 
        draw_board(board)
        player = next_player(player)
        
        if find_winner(board) is None and is_full(board) == False:
            print()
            move = input('Choose your next move: ')
            print()
            
    else:
        print('You made an invalid movement')
        print()
        move = input('Choose your next move: ')



if find_winner(board) == 'x' or find_winner(board) == 'o': 
    print()
    if find_winner(board) == 'x':
        print('The x player wins!')
    else:
        print('The o player wins!')



if is_full(board) == True: 
    print()
    print('Nobody wins, we tie')


