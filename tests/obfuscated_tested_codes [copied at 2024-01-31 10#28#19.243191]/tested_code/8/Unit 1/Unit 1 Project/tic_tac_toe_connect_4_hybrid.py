




from tic_tac_toe_connect_4_hybrid_functions import *





 
connect4_board = [
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ']
         ]


all_column_heights = [ [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]
                     ]


board_of_winners = [[' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']]

         
tic_tac_toe_board = []


# Creates the tic tac toe board
for i in range(9):
    tic_tac_toe_board.append(
        [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ']])


        
draw_whole_board(tic_tac_toe_board) # Draws the tic tac toe board
player = 'x' # Assigns the first player to x
winner = None # assigns the winner to None
full = None
while((winner == None) and (full == None)): # makes sure that while there is no winner, the game
    # continues to be played.

    # Gets the players board selection, making sure it is an int from 1-9
    board_selection = get_valid_board_selection(player, all_column_heights)
    # Changes the board selection to the index, as the human enters in a number
    # from a range that begins with 1
    board_index = int(board_selection) - 1
    # Gets the players column selection, making sure it is an int from 1-7
    column_move = c4_get_valid_column(player, all_column_heights[board_index])
    # Changes the column selection to the index, as the human enters in a number
    # from a range that begins with 1
    column_index = int(column_move) - 1
    # Makes the move
    c4_make_move(player, column_index,
                 all_column_heights[board_index],
                 tic_tac_toe_board[board_index])
    # Switches from 1 - 9 to a 3x3 list. If there is a winner on the connect 4
    # board adds that to board_of_winners
    switch_between_styles(tic_tac_toe_board, board_index, board_of_winners,
                          all_column_heights)
    # Draws the board
    draw_whole_board(tic_tac_toe_board)
    # Checks if the whole game board is full.
    full = find_if_game_full(all_column_heights)
    # Finds if there is a winner, and assigns winner to that value.
    winner = find_winner(board_of_winners)
    # Switches to the next player
    player = next_player(player)

# Prints the winner
if ((winner == 'tie') or (full == 'tie')):
    print('It\'s a tie!')

else:
    print('Player ' + winner + ' is the winner!')



























