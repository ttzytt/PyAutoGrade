


from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
count = 1


while count != 10 and not (find_winner(board) == 'x' or find_winner(board) == 'o'):
    print(find_winner(board))
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    count += 1
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)



draw_board(board)
print()
if find_winner(board) is None:
    print('We draw ')
else:
    print('The ' + (find_winner(board)) + ' player wins! ')


