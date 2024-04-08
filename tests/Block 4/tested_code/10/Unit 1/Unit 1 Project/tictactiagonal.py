




from tictactiagonal_functions import *


board =  [['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
          [' ', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
          ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#']]
draw_board(board)
turns_played = 0
player = 'x'
print("Welcome to TicTacTiagonal! This game is pretty much tic-tac-toe but on the diagonals and you have to get 5 in a row instead of 3. Ok it's not that similar to tic-tac-toe.")

while not (turns_played == 81) and check_winner(board) == None:
    player_input = input(player + ' player, chose your move:')
    while make_move(player, player_input, board) != True:
        print('Please input a valid move.')
        player_input = input(player + ' player, chose your move:')
        
    make_move(player, player_input, board)
    turns_played += 1

    check_winner(board)

    
    if player == 'x':
        player ='o'
    else:
        player = 'x'
        
    draw_board(board)

print('The ' + check_winner(board) + ' player wins!')


        
        
