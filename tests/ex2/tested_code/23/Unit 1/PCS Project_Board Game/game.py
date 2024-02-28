

from game_functions import *



board = [ [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '] ]
player = '1'

end = find_winner(board)

while not end:
    draw_board(board)
    next_number = get_number()
    next_move = get_move(player)
    if next_move == 'skip':
        player = next_player(player)
        next_move = get_move(player)
        player = next_player(player)
        success = make_move(next_number, next_move, board)
        continue
    success = make_move(next_number, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        if next_move == 'skip':
            player = next_player(player)
            next_move = get_move(player)
            success = make_move(next_number, next_move, board)
            break
        success = make_move(next_number, next_move, board)
    player = next_player(player)
    end = find_winner(board)
    

draw_board(board)
print()
print('Player ' + player + ' wins!')

