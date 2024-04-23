

from three_dimensional_tic_tac_toe_functions import *


print('Welcome to 3-Dimensional Tic-Tac-Toe! :D')
print()
print('Reminder: This is a THREE person game, so grab a friend, and grab another!')
print()
print("Before the game starts, let's establish some rules.")
print()
print('1. All players make ONE move each turn')
print('2. Your objective is to get THREE in a row')
print('3. The three in a row can be on one layer or across multiple layers')
print('4. Most importantly ... HAVE FUN!!!!')
print()


board = [[ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']],
        [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']],
        [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]]
player = 'x'
count = 0

while find_winner(board) == None and count < 27:
    count += 1
    draw_board(board)
    
    next_move = get_move(player)
    success = make_move(player, next_move, board)
    while not success:
        print('That is not a valid move.')
        next_move = get_move(player)
        success = make_move(player, next_move, board)
    player = next_player(player)

if count == 27 and find_winner(board) == None: 
    print()
    print("It's a tie!")


if find_winner(board) != None:
    draw_board(board)
    print()
    print('The ' + find_winner(board) + ' player wins!')


    
    

    

