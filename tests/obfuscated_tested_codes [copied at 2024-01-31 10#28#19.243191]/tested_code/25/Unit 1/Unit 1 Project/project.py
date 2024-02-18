

from project_functions import *

rounds = 0
piece_x = 0
piece_o = 0


board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'


while find_winner(board) is None:  
    draw_board(board)
    

    if piece_x < 3 or piece_o < 3:
        next_move = get_move(player)
        success = make_move(player, next_move, board)
        while not success:
            print('That is not a valid move.')
            next_move = get_move(player)
            success = make_move(player, next_move, board)


    else:
        next_move = get_pick_up_spot(player)
        success = delete_piece(player, next_move, board)
        while not success:
            print('That is not a valid move.')
            next_move = get_pick_up_spot(player)
            success = delete_piece(player, next_move, board)
        delete_piece(player, next_move, board)
        draw_board(board)
        next_move = get_move(player)
        success = make_move(player, next_move, board)
        while not success:
            print('That is not a valid move.')
            next_move = get_move(player)
            success = make_move(player, next_move, board)
        make_move(player, next_move, board)

    if player == 'x':
        piece_x = piece_x + 1
    if player == 'o':
        piece_o = piece_o + 1
        
    player = next_player(player)
    rounds = rounds + 1



winner = find_winner(board)
draw_board(board)
print()
print('The ' + winner + ' player wins!')

