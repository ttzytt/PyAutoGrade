




from Unit_1_project_functions import *

board = [[' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ']]
player = 'x'


move_count = 1
count_X = 4
count_O = 4


move_piece = True

while move_count != 22 and not (find_winner(board) == 'x' or find_winner(board) == 'o'):
    draw_board(board)
    move = find_move(player)

    
    if make_move(player, move, board) == True:
        move_piece = True
    else:
        move_piece = False

    
    if count_X < 0 or count_O < 0:
        print('You do not have any big pieces left.')
        move_piece = False
        
        make_move(player, move, board)

    
    while move_piece == False:
        print('That is not a valid move, please try again.')
        move = find_move(player)

        if make_move(player, move, board) == False:
            move_piece = False
        else:
            move_piece = True
            

    
    if move[3] == 'X':
        count_X -= 1
    elif move[3] == 'O':
        count_O -= 1
            
    
    if move_piece == True:
        if player == 'x':
            print('You have ' + str(count_X) + ' big X pieces left. ')
        elif player == 'o':
            print('You have ' + str(count_O) + ' big O pieces left. ')

    player = next_player(player)
    move_count += 1
        
    
draw_board(board)
print()
if find_winner(board) != None:
    print('The ' + (find_winner(board)) + ' player wins! ')
else:
    print('We draw ')
