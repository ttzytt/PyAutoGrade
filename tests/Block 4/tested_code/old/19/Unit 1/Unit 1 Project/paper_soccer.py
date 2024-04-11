


import time

from paper_soccer_functions import *


board = []
ball_pos = [4, 2]

player = '⊙'

is_format = 0

num_rows = 9
num_columns = 5


create_board(num_rows, num_columns, board)

board[ball_pos[0]][ball_pos[1]][1][1] = '⊙'

draw_board(board, num_rows, num_columns)


switch = 0

counter = 0


while not(find_winner(board, num_rows)):

    erase_border(board, num_columns, num_rows)

    show_border(board, num_columns, ball_pos)
    
    if counter == 0:
        player = player

    elif extra_turn(board, ball_pos, num_columns):
        player = player

    elif player == '⊙':
        player = 'x'

    elif player == 'x':
        player = '⊙'

    if counter != 0 and not(extra_turn(board, ball_pos, num_columns)):
        
        fun_time(switch, 0.5)
        print("switching player...")
        fun_time(switch, 0.75)
        
    elif counter != 0:
        print("player " + player + " gets aznd extra turn.")

    draw_board(board, num_rows, num_columns)

    print('It is currently player ' + player + "'s turn") 
    print()
    direction = input('Where do you want to move(north, south, west, northeast, etc. : ')
    print()
    legal = make_move(direction, ball_pos, board, player)

    while legal != 'legal':
        print()
        if legal == 'wrong format':
            print("You're input is in the wrong format")
        else:
            print("You're move was not legal")
        print('Please try again')
        print()
        direction = input('Where do you want to move(north, south, west, northeast, etc. : ')
        legal = make_move(direction, ball_pos, board, player)

    print()
    draw_board(board, num_rows, num_columns)

    counter += 1

print()
print('The winner is...')
print('player ' + find_winner(board, num_rows) + '!!!')
