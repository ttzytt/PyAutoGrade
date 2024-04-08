



import random


from connect_four_functions import *



random.seed()

random_row = random.randint(0, 3)
random_column = random.randint(0, 3)

board = [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ]
board[random_row][random_column] = '@'
player = 'x'
count = 0


while find_winner(board) is None and count < 16:
    count += 1
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)


if count == 16 and find_winner(board) is None:
    print()
    print("It's a tie!")


if find_winner(board) is not None:
    draw_board(board)
    print()
    print('The ' + find_winner(board) + ' player wins!')

