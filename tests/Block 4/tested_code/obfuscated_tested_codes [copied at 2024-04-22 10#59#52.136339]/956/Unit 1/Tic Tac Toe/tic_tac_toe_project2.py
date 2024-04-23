



print('This game is an improved versioon from Gomoku.'+
      'Players alternate turns putting their "x" or "o" in the blank square.'+
      'You can win by connect five "x" or "o" in the same roll'+
      'Vertically, Horizontally or Diagonally.'+
      'In my improved version, we can also win by'+
      'Placing the "x" or "o" into a diagram like "➕"')
from tic_tac_toe_project2_functions import *
times = 0


board = [ [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '] ]
player = 'x'


while True:
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    times += 1
    if(find_winner(board) is True):

        print('True')
        break
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)
    
print(player + ', you win.')
print('game over')
draw_board(board)
