




from tic_tac_toe_functions_part_2 import *





# ------------------------ GAME PRESET -------------------------

#R Great and Clear Instruction!
# Introduce the game and rules to player first
print('PLEASE READ THE INSTRUCTIONS BEFORE YOU START')
print()
print('We are going to play a board game little bit different from')
print('tic tac toe. The way to win is to have 5 consecutive blocks')
print('marked by you (either \'x\' or \'o\'). For each player\'s sake,')
print('the system will pop out a reminder if someone is about to win.')
print('Your input should be a number and a capitalized letter such as')
print('2C, 3F, 8H. You will be asked to input again if your input block')
print('is occupied or it\'s in the wrong format. If you wish to exit')
print('the game, please input \'quit\'. Enjoy your game!')
print()
print('Latest update: 1) Support undoing the last step 2) You can waive')
print('your 5 consecutive blocks and choose not to win, try them out!')
print()
print('About undo & waive: 1) you can undo your last move by inputing')
print('undo, then you can reselect your move, you can undo your last')
print('move ONLY; 2) your opponent can add a \'W\' on their 5th block')
print('to give you a chance, you must block the blocks with a \'R\' in')
print('your input. Please ask me if you still need explanations.')
print()
# W stands for waive and R stands for recover

# Start with an empty board and show it to the player
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
draw_board(board)

# Let X play first (then X and O play alternatively)
player = 'x'
print()
move = input('X player, choose your move: ')
print()

# Preset these 2 variables
last_step = '1A'
last_move = '1A'


# ------------------------ GAME PLAY -------------------------

# This happens for most of the time
while find_winner(board,move,last_move) == None and is_full(board,move,last_move) == False:
    # This happens in most cases (there are empty blocks and no winners)

    if move == 'quit':
        print('See you next time')
        break
        # Stop the game if someone input quit (break the loop)
    
    if make_move(player,move,board) == True:
        # If the player's move is legal, do the following operations
        
        if move != 'undo': 
            make_move(player,move,board) 
            if len(move) >= 3:
                
                
                if move[2] == 'W': 
                    last_move = move
                elif move[2] == 'R': 
                    last_move = 'NNN'
            last_step = move 
            
        elif move == 'undo': 
            undo_last_step(board,last_step,move,player) 
                        
        
        player = next_player(player) 
        
        if find_winner(board,move,last_move) == None:
            

            draw_board(board) 
            print()
            if about_to_win(board) != False:
                
                
                if about_to_win(board) == 'o':
                    print('O player is about to win!') 
                elif about_to_win(board) == 'x':
                    print('X player is about to win!') 
            print()
            
            if player == 'o':
                move = input('O player, choose your move/X player, undo your move: ')
            elif player == 'x':
                move = input('X player, choose your move/O player, undo your move: ')
            print()
            
    elif make_move(player,move,board) != True:
        
        
        print('You made an invalid movement because:')

        
        if make_move(player,move,board) == 'format':

            print('Your input format is incorrect')

        elif make_move(player,move,board) == 'occupied':

            print('This block is already occupied')

        print()
        move = input('Choose your move again: ')



if find_winner(board,move,last_move) != None:

    draw_board(board)
    print()
    if find_winner(board,move,last_move) == 'x':
        print('The X player wins, congratulations!')
    elif find_winner(board,move,last_move) == 'o':
        print('The O player wins, congratulations!')



if is_full(board,move,last_move) == True:

    print('The board is full, you guys draw the game')



