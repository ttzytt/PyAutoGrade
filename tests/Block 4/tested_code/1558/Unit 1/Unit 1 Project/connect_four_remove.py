

"""
I did not receive help or look up
information other than from the teacher
and the course materials.
"""

from connect_four_remove_functions import *

board = [[' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ']]
player = 'x'
move_number = 0


print('Welcome to Connect Four Remove!')
print('Two players will take turns trying to get 4 of their chips')
print('in a line, either a row, column, or diagonal.')
print()
print('Every turn a player can either place their chip in a column and')
print('It will fall to the bottom, or they can remove one of their chips')
print('From the very bottom row of the grid.')
print()
print('Please enter your move as a number to place, or R number to remove')
print('Ex. R4, Ex. 3')


while find_winner(board) == None and move_number < 30:
    draw_board(board)
    
    next_move = get_move(player)
    
    
    if len(next_move) >= 1 and next_move[0] == 'R':
        column = int(next_move[1]) - 1
        
        success = remove_chip(player, next_move, board)  
        
    else: 
        success = make_move(player, next_move, board)  

    while not success:  
        print('That is not a valid move.')
        next_move = get_move(player)
        
        if len(next_move) >= 1 and next_move[0] == 'R':
            column = int(next_move[1]) - 1
            success = remove_chip(player, next_move, board)
            
        else: 
            success = make_move(player, next_move, board)

    player = next_player(player) 
    move_number += 1

    

draw_board(board)
print()
if find_winner(board) != None:
    print(f'The {find_winner(board)}')
else:
    print("It's a tie!")

