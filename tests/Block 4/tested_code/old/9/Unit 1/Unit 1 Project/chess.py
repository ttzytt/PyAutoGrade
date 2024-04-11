
from chess_functions import *

board = [ ['r', 'n', 'b','q','k','b','n','r'],
          ['p', 'p', 'p','p','p','p','p','p'],
          [' ', ' ', ' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' '],
          ['P', 'P', 'P','P','P','P','P','P'],
          ['R', 'N', 'B','Q','K','B','N','R']]
draw_board(board) 

move = input('Input your move: ')
ori = move[0:2]
des = move[2:4]

while move != 'quit':
    if move != 'undo':
        make_move(board,ori,des)
        last_move = move
    elif move == 'undo':
        undo_last_step(board,last_move)
    draw_board(board)
    move = input('Input your move: ')
    ori = move[0:2]
    des = move[2:4]






if move == 'quit':
    print('See you next time')
