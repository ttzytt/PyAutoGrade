


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
        





'''
# Play the game one turn at a time.
move = input('Choose your move: ')

while find_winner(board) == None and time < 9:  # The board isn't full & nobody wins

    if make_move(player, move, board) == True: 
    
        make_move(player,move,board)
        draw_board(board)
        player = next_player(player)
        time += 1

        move = input('Choose your move: ')
        
        
    elif make_move(player, move, board) == False: 
        print('That is not a valid move.')
        move = input('Choose your move again: ')
        






if find_winner(board) != None:
    if find_winner(board) == 'x':
        print('x wins')
    else:
        print('o wins')


if time == 9:
    draw_board(board)
    print('No player wins...')


    
    



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
time = 0




if (find_winner(board)) == 'x':
    draw_board(board)
    print('The x player wins!')

if (find_winner(board)) == 'o':
    draw_board(board)
    print('The o player wins!')

if time == 9:
    draw_board(board)
    print('No player wins...')


while not (find_winner(board) != None or time == 9):  
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    time += 1
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    
    
    player = next_player(player)

'''
