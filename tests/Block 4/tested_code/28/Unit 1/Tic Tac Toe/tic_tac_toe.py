

from tic_tac_toe_functions import *





board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
is_tie = False


while find_winner(board) is None and not is_tie:
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)  
    player = next_player(player)
    
    
    is_tie = True
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == ' ':
                is_tie = False


draw_board(board)
print()
if is_tie:
    print("It's a tie haha")
else:
    print('The ' + find_winner(board) + ' player wins!')

