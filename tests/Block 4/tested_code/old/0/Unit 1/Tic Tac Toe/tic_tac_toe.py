

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
move_count = 1


while not (find_winner(board) == 'x' or find_winner(board) == 'o' and move_count == 10):
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    move_count += 1
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)


    


draw_board(board)
print()
if find_winner(board) != None:
    print(f'The {find_winner(board)} player wins!')
elif find_winner(board) == None or move_count == 10:
    print('We Draw')


