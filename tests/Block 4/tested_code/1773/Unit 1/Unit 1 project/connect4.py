


from connect4_functions import *

grid = [ [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', '█', ' ', '█', ' ', '█', ' '] ] 

player = 'x'

while True:
    draw_grid(grid)
    next_move = get_move(player)
    success = make_move(player, next_move, grid)
    while not success:s
        print('That aint a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, grid)
    player = next_player(player)
