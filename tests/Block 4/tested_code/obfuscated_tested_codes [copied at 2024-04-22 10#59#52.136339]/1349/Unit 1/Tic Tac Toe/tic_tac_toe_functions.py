

"""
The following functions are for use in making a Tic-Tac-Toe game.

For all of the code below, a board 3 by 3 is a list of lists of the
form
        [ [' ', 'o', ' '],
          ['x', ' ', 'x'],
          ['x', 'o', ' '] ]
(Each entry is an 'x', 'o', or ' '.)

For the user, a board will be printed in the form
      ┌───┬───┬───┐ 
    1 │   │ o │   │ 
      ├───┼───┼───┤ 
    2 │ x │   │ x │ 
      ├───┼───┼───┤ 
    3 │ x │ o │   │ 
      └───┴───┴───┘ 
        A   B   C

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
          + row[2] + ' │ ')



def draw_board(board):
    print('  ┌───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  └───┴───┴───┘ ')
    print('    A   B   C   ')



def find_winner(board):
    
    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) and board[row][0] != ' ':
            return board[row][0]
    
    for column in range(3):
        if (board[0][column] == board[1][column] and board[1][column] == board[2][column]) and board[0][column] != ' ':
            return board[0][column]
    
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != ' ':
        return board[0][0]
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) and board[1][1] != ' ':
        return board[0][2]
    return None




def get_move(player):
    return input(player + ' player, choose your move: ')


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
    
    
    if (not (1 <= int(move[0]) <= 3) or not (ord('A') <= ord(move[1]) <= ord('C'))):
        return False

    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    
    if board[row][column] == ' ':
        board[row][column] = player
        return True
    return False





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

