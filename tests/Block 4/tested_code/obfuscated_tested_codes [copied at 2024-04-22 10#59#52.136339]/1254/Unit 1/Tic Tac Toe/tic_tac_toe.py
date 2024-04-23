

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
count = 0

while find_winner(board) == None and count < 9:
    count += 1
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)

if count == 9 and find_winner(board) == None:
    print()
    print("It's a tie!")


if find_winner(board) != None:
    draw_board(board)
    print()
    print('The ' + find_winner(board) + ' player wins!')

    
    

    

