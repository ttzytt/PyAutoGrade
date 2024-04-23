


"""
The following functions are for use in making a connect four game.

For all of the code below, a board 4 by 4 is a list of lists of the
form
        [ [' ', ' ', ' ', ' '],
          ['o', ' ', 'x', ' '],
          ['x', '∆', 'o', 'o'],
          ['x', 'o', 'o', 'x']]
          
(Each entry is an 'x', 'o', '∆' or ' '.)

For the user, a board will be printed in the form:
      ┌───┬───┬───┬───┐
    1 │   │   │   │   │
      ├───┼───┼───┼───┤
    2 │ o │   │ x │   │
      ├───┼───┼───┼───┤
    3 │ x │ ∆ │ o │ o │
      ├───┼───┼───┼───┤
    4 │ x │ o │ o │ x │
      └───┴───┴───┴───┘ 
        A   B   C   D

Moves/spaces are referred to by strings such as '1A' or '4D'.
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





def find_winner(board):
    
    for row in range (4):
        if board[row][0] == board[row][1] and board[row][0] == board[row][2] and board[row][0] == board[row][3]:
            if board[row][0] == 'x':
                return 'x'
            elif board[row][0] == 'o':
                return 'o'

    
    for column in range (4):
        if board[0][column] == board[1][column] and board[0][column] == board[2][column] and board[0][column] == board[3][column]:
            if board[0][column] == 'x':
                return 'x'
            elif board[0][column] == 'o':
                return 'o'

    
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == board[2][2] and board[0][0] == board[3][3]:
        if board [0][0] == 'x':
            return 'x'
        elif board[0][0] == 'o':
            return 'o'
    elif board[0][3] == board[1][2] and board[0][3] == board[2][1] and board[0][3] == board[3][0]:
        if board [0][3] == 'x':
            return 'x'
        elif board[0][3] == 'o':
            return 'o'
        
    return None




def get_move(player):
    return input(player + ' player, chose your move: ')


"""
Modify board by making player make the given move, and return True if
successful.

Inputs:
    player      must be either 'x' or 'o'
    move        must be a string, should be a number 1, 2, or 3
                followed by a capital letter A, B, or C, such as
                '2C'
    board       see top of file
Output:
    If move is valid, then board is modified accordingly and the function
    returns True.
    If move is an invalid string or if the space is already occupied,
    then the board will not be modified and the function returns False.
"""
def make_move(player, move, board):
    
    if len(move) != 2:
        return False
    elif not ('1' <= move[0] <= '4'):
        return False
    elif not ('A' <= move[1] <= 'D'):
        return False

    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    
    if board[row][column] == (' '):
        board[row][column] = player
        return True
    else:
        return False




def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

