





from ttt_functions_part_2 import *

board = [ [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' '],
          [' ', ' ', ' ',' ',' ',' ',' ',' ',' ',' ']]
player = 'x'

which_one_move = 1

if which_one_move == 1: 
    draw_board(board)
    
print()
move = input('Choose your first move: ')
print()

import random
random.seed()





while find_winner(board) == None and is_full(board) == False:
     
    if which_one_move % 2 == 1: 
        if make_move(player,move,board) == True: 
            make_move(player,move,board)
            draw_board(board)
            player = next_player(player)
            if find_winner(board) is None and is_full(board) == False:
                print()
                automove = (random.choice(['1A','2A','3A','4A','5A','6A','7A','8A','9A','0A'
                           '1B','2B','3B','4B','5B','6B','7B','8B','9B','0B'
                           '1C','2C','3C','4C','5C','6C','7C','8C','9C','0C'
                           '1D','2D','3D','4D','5D','6D','7D','8D','9D','0D'
                           '1E','2E','3E','4E','5E','6E','7E','8E','9E','0E'
                           '1F','2F','3F','4F','5F','6F','7F','8F','9F','0F'
                           '1G','2G','3G','4G','5G','6G','7G','8G','9G','0G'
                           '1H','2H','3H','4H','5H','6H','7H','8H','9H','0H'
                           '1I','2I','3I','4I','5I','6I','7I','8I','9I','0I']))
                print()
            which_one_move += 1
        else:
            print('You made an invalid movement')
            print()
            move = input('Choose your next move: ')
            
    else: 
        if make_automove(player,automove,board) == True: 
            make_automove(player,automove,board)
            print('I choose ' + automove)
            print()
            draw_board(board)
            player = next_player(player)
            if find_winner(board) is None and is_full(board) == False:
                print()
                move = input('Choose your next move: ')
                print()
            which_one_move += 1
        else:
            automove = (random.choice(['1A','2A','3A','4A','5A','6A','7A','8A','9A','0A'
                           '1B','2B','3B','4B','5B','6B','7B','8B','9B','0B'
                           '1C','2C','3C','4C','5C','6C','7C','8C','9C','0C'
                           '1D','2D','3D','4D','5D','6D','7D','8D','9D','0D'
                           '1E','2E','3E','4E','5E','6E','7E','8E','9E','0E'
                           '1F','2F','3F','4F','5F','6F','7F','8F','9F','0F'
                           '1G','2G','3G','4G','5G','6G','7G','8G','9G','0G'
                           '1H','2H','3H','4H','5H','6H','7H','8H','9H','0H'
                           '1I','2I','3I','4I','5I','6I','7I','8I','9I','0I'
                           '1J','2J','3J','4J','5J','6J','7J','8J','9J','0J']))
                
    

if find_winner(board) == 'x' or find_winner(board) == 'o':
    print()
    if find_winner(board) == 'x':
        print('You win, congrats!') 
    else:
        print('I win, haha!') 




if is_full(board) == True:
    print()
    print('Nobody wins, we tie')
