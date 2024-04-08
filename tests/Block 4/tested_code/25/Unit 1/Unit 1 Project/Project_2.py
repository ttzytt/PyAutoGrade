

from Project_2_Functions import *



board = [ [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ']]
player = 'x'


while True:  
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)



draw_board(board)
print()
print('The x player wins!')

all_equal()
