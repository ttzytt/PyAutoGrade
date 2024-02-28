

from tic_tac_toe_functions import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
move_number=0
end_of_game = False


print('Welcome to Tic Tac Toe!')
print()
print('Two players will take turns placing an x or o on a 3 x 3 grid')
print()
print('Please enter your move as RowColumn (ex. 1A)')

while end_of_game == False:  
    draw_board(board)
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success: 
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)
    if move_number == 9:
        end_of_game = True

    move_number += 1

    if find_winner(board) != None or move_number == 9: 
        end_of_game = True
       

draw_board(board)
print()
if find_winner(board) != None:
    print(f'The {find_winner(board)} player wins!')
else:
    print("It's a tie!")

