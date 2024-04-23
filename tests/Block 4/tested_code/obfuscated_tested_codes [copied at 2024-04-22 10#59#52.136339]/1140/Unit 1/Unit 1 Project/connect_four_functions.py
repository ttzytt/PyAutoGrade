



"""
The following functions are for use in making a Connect4 game.

For all of the code below, a board 4 by 4 is a list of lists of the
form
        [ [' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' '],
          ['o', ' ', 'o', ' '],
          ['x', 'o', 'x', 'x'] ]
(Each entry is an 'x', 'o', '@', or ' '.)

For the user, a board will be printed in the form
      ┌───┬───┬───┬───┐
    1 │   │   │   │   │
      ├───┼───┼───┼───┤
    2 │   │   │   │   │
      ├───┼───┼───┼───┤ 
    3 │ o │   │ o │   │
      ├───┼───┼───┼───┤
    4 │ x │ o │ x │ x │
      └───┴───┴───┴───┘
        A   B   C   D

Moves/spaces are referred to by strings such as '1A' or '2C'.
"""


"""
Print the given row to the screen.
Input:
    row            a list representing one row of the board
    row_number     int to be printed before the row
"""
def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ ')




def draw_board(board):
    print('  ┌───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  └───┴───┴───┴───┘ ')
    print('    A   B   C   D   ')

    




'''
def find_winner(board):
    # Win by row
    for row in range (4):
        if board[row][0] == board[row][1] and board[row][0] == board[row][2] and board[row][0] == board[row][3]:
            if board[row][0] == 'x':
                return 'x'
            elif board[row][0] == 'o':
                return 'o'

    # Win by column
    for column in range (4):
        if board[0][column] == board[1][column] and board[0][column] == board[2][column] and board[0][column] == board[3][column]:
            if board[0][column] == 'x':
                return 'x'
            elif board[0][column] == 'o':
                return 'o'

    # Win by diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == board[3][3]:
        if board [0][0] == 'x':
            return 'x'
        elif board[0][0] == 'o':
            return 'o'
    elif board[0][3] == board[1][2] and board[1][2] == board[2][1] and board[2][1] == board[3][0]:
        if board [0][3] == 'x':
            return 'x'
        elif board[0][3] == 'o':
            return 'o'
        
    return None
'''



def find_winner_in_list(line):
    if ((line[0] == 'x' or line[0] == '@')
            and (line[1] == 'x' or line[1] == '@')
            and (line[2] == 'x' or line[2] == '@')
            and (line[3] == 'x' or line[3] == '@')):
        return 'x'
    elif ((line[0] == 'o' or line[0] == '@')
            and (line[1] == 'o' or line[1] == '@')
            and (line[2] == 'o' or line[2] == '@')
            and (line[3] == 'o' or line[3] == '@')):
        return 'o'
    else:
        return None



"""
find_winner_in_list(['x', 'x', 'x', '@']) returns 'x'
find_winner_in_list(['x', 'o', ' ', '@']) returns None
"""

"""
parameter
argument
function
calling a function
"""





def get_move(player):
    return input(player + ' player, chose your move: ')


"""
Modify board by making player make the given move, and return True if
successful.

Inputs:
    player      must be either 'x' or 'o'
    move        must be a string, should be a letter A, B, C, or D
    board       see top of file
Output:
    If move is valid, then board is modified accordingly and the function
    returns True.
    If move is an invalid string or if the space is already occupied,
    then the board will not be modified and the function returns False.
"""
def make_move(player, move, board):
    
    if len(move) != 1:
        return False
    elif not ('A' <= move[0] <= 'D'):
        return False

    
    
    
    
    column = ord(move[0]) - ord('A')

    
    

    
    if board[0][column] != ' ':
        return False
    
    
    row = 3
    while not (board[row][column] == ' '):
        row = row - 1
    board[row][column] = player
    return True




def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

