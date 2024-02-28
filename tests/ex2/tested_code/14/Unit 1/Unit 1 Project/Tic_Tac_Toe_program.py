





from Tic_Tac_Toe_functions import *





print('Instruction: Enter the layer indicator, row number and then column number to play the 3D Tic Tac Toe game.')
print('Example: A24, C11')
print()
print('Tips: You can win this extremely hard 3D game by occupying'
      +' any of the lines, face diagonals or space diagonals in the 3D chess board.')
print()


board_1 = [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ]
board_2 = [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ]
board_3 = [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ]
board_4 = [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '] ]









player = 'x'
number_played = 0 


boards = [board_1, board_2, board_3, board_4] 
 

while find_winner_all(boards) is None and number_played < 64:
    draw_board(boards)
    next_move = get_move(player)
    success = make_move(player, next_move, boards)
    while success is not True: 
        print('That is not a valid move.')
        print()
        next_move = get_move(player) 
        
        success = make_move(player, next_move, boards)
    player = next_player(player)
    number_played += 1



draw_board(boards)
print()



if number_played == 64 and find_winner_all(boards) is None:
    print('The game ties.')
else:
    
    
    print('The '+ next_player(player) +' player wins!')
