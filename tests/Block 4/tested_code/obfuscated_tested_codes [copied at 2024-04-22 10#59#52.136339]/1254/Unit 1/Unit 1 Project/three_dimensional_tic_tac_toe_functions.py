


"""
The following functions are for use in making a Tic-Tac-Toe game.

For all of the code below, a board 3 by 3 by 3 is a list of lists of the
form
       [[ [' ', 'x', ' '],
          ['&', ' ', ' '],
          ['x', ' ', ' ']],
        [ [' ', ' ', ' '],
          [' ', 'x', ' '],
          [' ', ' ', 'o']],
        [ [' ', 'o', ' '],
          ['&', ' ', ' '],
          [' ', ' ', ' ']]]
          
(Each entry is an 'x', 'o', '&', or ' '.)

For the user, a board will be printed in the form
  ┌───┬───┬───┐ 
1 │   │   │   │ 
  ├───┼───┼───┤ 
2 │   │   │   │ 
  ├───┼───┼───┤ 
3 │   │   │   │ 
  └───┴───┴───┘ 
    A   B   C   
       ┌───┬───┬───┐ 
     1 │   │   │   │ 
       ├───┼───┼───┤ 
     2 │   │   │   │ 
       ├───┼───┼───┤ 
     3 │   │   │   │ 
       └───┴───┴───┘ 
         D   E   F  
            ┌───┬───┬───┐ 
          1 │   │   │   │ 
            ├───┼───┼───┤ 
          2 │   │   │   │ 
            ├───┼───┼───┤ 
          3 │   │   │   │ 
            └───┴───┴───┘ 
              G   H   I   

Moves/spaces are referred to by strings such as '1A' or '2C'.
""" 


"""
Print the given row to the screen.
Input:
    row            a list representing one row of the board
    row_number     int to be printed before the row
"""

def draw_row(row, row_number, num_spaces):
    print(' ' * num_spaces + str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ ')






def draw_board(board):
    print('  ┌───┬───┬───┐ ')
    draw_row(board[0][0], 1, 0)
    print('  ├───┼───┼───┤ ')
    draw_row(board[0][1], 2, 0)
    print('  ├───┼───┼───┤ ')
    draw_row(board[0][2], 3, 0)
    print('  └───┴───┴───┘ ')
    print('    A   B   C   ')
    print('       ┌───┬───┬───┐ ')
    draw_row(board[1][0], 1, 5)
    print('       ├───┼───┼───┤ ')
    draw_row(board[1][1], 2, 5)
    print('       ├───┼───┼───┤ ')
    draw_row(board[1][2], 3, 5)
    print('       └───┴───┴───┘ ')
    print('         D   E   F  ')
    print('            ┌───┬───┬───┐ ')
    draw_row(board[2][0], 1, 10)
    print('            ├───┼───┼───┤ ')
    draw_row(board[2][1], 2, 10)
    print('            ├───┼───┼───┤ ')
    draw_row(board[2][2], 3, 10)
    print('            └───┴───┴───┘ ')
    print('              G   H   I   ')




def find_winner(board):
    
    for i in range (3):
        row_check = 0
        while row_check < 3:
            if board[i][row_check][0] == board[i][row_check][1] == board[i][row_check][2]:
                if board[i][row_check][0] == 'x':
                    return 'x'
                elif board[i][row_check][0] == 'o':
                    return 'o'
                elif board[i][row_check][0] == '&':
                    return '&'
            row_check += 1


    
    for i in range (3):
        column_check = 0
        while column_check < 3:
            if board[i][0][column_check] == board[i][1][column_check] == board[i][2][column_check]:
                if board[i][0][column_check] == 'x':
                    return 'x'
                elif board[i][0][column_check] == 'o':
                    return 'o'
                elif board[i][0][column_check] == '&':
                    return'&'
            column_check += 1
            
    
    for i in range (3):
        layer_check = 0
        while layer_check < 3:
            if board[0][i][layer_check] == board[1][i][layer_check] == board[2][i][layer_check]:
                if board[0][i][layer_check] == 'x':
                    return 'x'
                elif board[0][i][layer_check] == 'o':
                    return 'o'
                elif board[0][i][layer_check] == '&':
                    return'&'
            layer_check += 1


    
    for i in range (3):
        if board[i][0][0] == board[i][1][1] == board[i][2][2] or board[i][0][2] == board[i][1][1] == board[i][2][0]:
            if board[i][1][1] == 'x':
                return 'x'
            elif board[i][1][1] == 'o':
                return 'o'
            elif board[i][1][1] == '&':
                return '&'
            
    
    if board[0][0][0] == board[1][1][1] == board[2][2][2] or board[0][0][2] == board[1][1][1] == board [2][2][0]:
        if board[1][1][1] == 'x':
            return 'x'
        elif board[1][1][1] == 'o':
            return 'o'
        elif board[1][1][1] == '&':
            return '&'




            
    return None

'''
Do you think it's possible to do something like this to replace the 3 different cases
if board[1][1][1] == n:
        return n

'''
           

# Ask the player for their move and return the string they enter.
# (Does not check if this string is valid.)
def get_move(player):
    return input(player + ' player, chose your move: ')


"""
Modify board by making player make the given move, and return True if
successful.

Inputs:
    player      must be either 'x' or 'o' or '&'
    move        must be a string, should be a number 1, 2, or 3
                followed by a capital letter A, B, C, D, E, F, G, H, I, or J such as
                '2C'
    board       see top of file
Output:
    If move is valid, then board is modified accordingly and the function
    returns True.
    If move is an invalid string or if the space is already occupied,
    then the board will not be modified and the function returns False.
"""
def make_move(player, move, board):
    # Check that move is in the right format.
    if len(move) < 2:
        return False
    elif len(move) > 2:
        return False
#Try if len(move) != 2:
#    return False
    if not ('1' <= move[0] <= '3'):
        return False
    if not ('A' <= move[1] <= 'J'):
        return False


    if ord(move[1]) - ord('A') > 2:
        if ('D' <= move[1] <= 'F'): # column is D - F
            layer = 1
            column = ord(move[1]) - ord('D')
        else: # column is G - I
            layer = 2
            column = ord(move[1]) - ord('G')
    else: # column is A - C
        layer = 0
        column = ord(move[1]) - ord('A')

    # Subtract 1 from the row indicated by move.
    row = int(move[0]) - 1



    if board[layer][row][column] != ' ':
        return False

    # Move to the space if it is empty.
    board[layer][row][column] = player
    return True


# Returns the next player to move.
#   next_player('x') == 'o'
#   next_player('o') == 'x'
#   next_player('&') == '&'
def next_player(player):
    if player == 'x':
        return 'o'
    elif player == 'o':  # player == 'o'
        return '&'
    elif player == '&': # player == '&'
        return 'x'

