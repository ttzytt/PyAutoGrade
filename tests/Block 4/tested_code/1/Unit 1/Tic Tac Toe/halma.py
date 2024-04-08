







from halmaDr import *
board = [['x','x','x',' ',' ',' '],
         ['x','x',' ',' ',' ',' '],
         ['x',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ','o'],
         [' ',' ',' ',' ','o','o'],
         [' ',' ',' ','o','o','o']]
player = 'x'
while not find_winner_x == True or find_winner_o == True:
    draw_board(board)
    next_piece = get_piece(player)
    next_move = get_move(player)
    success = make_move(player, next_piece, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_piece = get_piece(player)
        next_move = get_move(player)
        success = make_move(player, next_piece, next_move, board)
    player = next_player(player)

    


draw_board(board)
print()
print('The ' + find_winner(board) + ' player wins!')

