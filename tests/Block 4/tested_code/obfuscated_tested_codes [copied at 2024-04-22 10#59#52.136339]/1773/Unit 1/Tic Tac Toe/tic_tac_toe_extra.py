

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'



board[0][0] = 'x'



board[1][2] = 'x'


draw_board(board)



board[0][2] = 'o'
board[1][1] = 'o'
board[2][0] = 'o'



if (board[1][1] != 'x') and (board[1][1] != 'o'):
    board[1][1] = 'x'



draw_board(board) 


print()
print('The x player wins!')

