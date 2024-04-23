

"""
The following functions are for use in making a Form a Square game.

For all of the code below, a board 4 by 4 is a list of lists of the
form
        [ [' ', 'o', ' ', ' '],
          ['x', ' ', 'x', ' '],
          ['x', 'o', ' ', 'o']
          ['x', 'o', ' ', ' '] ]
(Each entry is an 'x', 'o', or ' '.)

For the user, a board will be printed in the form
  ┌───┬───┬───┬───┐ 
1 │   │   │   │   │ 
  ├───┼───┼───┼───┤ 
2 │   │   │   │   │ 
  ├───┼───┼───┼───┤ 
3 │   │   │   │   │ 
  ├───┼───┼───┼───┤ 
4 │   │   │   │   │ 
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




def find_winner(board):
    
    
    if board[0][0] == 'x' and board[0][2] == 'x' and board[2][0] == 'x' and board[2][2] == 'x' and board[1][1] != 'x':
        return 'x'
    elif board[0][1] == 'x' and board[0][3] == 'x' and board[2][1] == 'x' and board[2][3] == 'x' and board[1][2] != 'x':
        return 'x'
    elif board[1][0] == 'x' and board[1][2] == 'x' and board[3][0] == 'x' and board[3][2] == 'x' and board[2][1] != 'x':
        return 'x'
    elif board[1][1] == 'x' and board[1][3] == 'x' and board[3][1] == 'x' and board[3][3] == 'x' and board[2][2] != 'x':
        return 'x'
    elif board[0][1] == 'x' and board[1][0] == 'x' and board[1][2] == 'x' and board[2][1] == 'x' and board[1][1] != 'x':
        return 'x'
    elif board[0][2] == 'x' and board[1][1] == 'x' and board[1][3] == 'x' and board[2][2] == 'x' and board[1][2] != 'x':
        return 'x'
    elif board[1][1] == 'x' and board[2][0] == 'x' and board[2][2] == 'x' and board[3][1] == 'x' and board[2][1] != 'x':
        return 'x'
    elif board[1][2] == 'x' and board[2][1] == 'x' and board[2][3] == 'x' and board[3][2] == 'x' and board[2][2] != 'x':
        return 'x'

    elif board[0][0] == 'x' and board[0][2] == 'x' and board[2][0] == 'x' and board[2][2] == 'x' and board[1][1] == 'x':
        return 'o'
    elif board[0][1] == 'x' and board[0][3] == 'x' and board[2][1] == 'x' and board[2][3] == 'x' and board[1][2] == 'x':
        return 'o'
    elif board[1][0] == 'x' and board[1][2] == 'x' and board[3][0] == 'x' and board[3][2] == 'x' and board[2][1] == 'x':
        return 'o'
    elif board[1][1] == 'x' and board[1][3] == 'x' and board[3][1] == 'x' and board[3][3] == 'x' and board[2][2] == 'x':
        return 'o'
    elif board[0][1] == 'x' and board[1][0] == 'x' and board[1][2] == 'x' and board[2][1] == 'x' and board[1][1] == 'x':
        return 'o'
    elif board[0][2] == 'x' and board[1][1] == 'x' and board[1][3] == 'x' and board[2][2] == 'x' and board[1][2] == 'x':
        return 'o'
    elif board[1][1] == 'x' and board[2][0] == 'x' and board[2][2] == 'x' and board[3][1] == 'x' and board[2][1] == 'x':
        return 'o'
    elif board[1][2] == 'x' and board[2][1] == 'x' and board[2][3] == 'x' and board[3][2] == 'x' and board[2][2] == 'x':
        return 'o'

    elif board[0][0] == 'o' and board[0][2] == 'o' and board[2][0] == 'o' and board[2][2] == 'o' and board[1][1] == 'o':
        return 'x'
    elif board[0][1] == 'o' and board[0][3] == 'o' and board[2][1] == 'o' and board[2][3] == 'o' and board[1][2] == 'o':
        return 'x'
    elif board[1][0] == 'o' and board[1][2] == 'o' and board[3][0] == 'o' and board[3][2] == 'o' and board[2][1] == 'o':
        return 'x'
    elif board[1][1] == 'o' and board[1][3] == 'o' and board[3][1] == 'o' and board[3][3] == 'o' and board[2][2] == 'o':
        return 'x'
    elif board[0][1] == 'o' and board[1][0] == 'o' and board[1][2] == 'o' and board[2][1] == 'o' and board[1][1] == 'o':
        return 'x'
    elif board[0][2] == 'o' and board[1][1] == 'o' and board[1][3] == 'o' and board[2][2] == 'o' and board[1][2] == 'o':
        return 'x'
    elif board[1][1] == 'o' and board[2][0] == 'o' and board[2][2] == 'o' and board[3][1] == 'o' and board[2][1] == 'o':
        return 'x'
    elif board[1][2] == 'o' and board[2][1] == 'o' and board[2][3] == 'o' and board[3][2] == 'o' and board[2][2] == 'o':
        return 'x'

    elif board[0][0] == 'o' and board[0][2] == 'o' and board[2][0] == 'o' and board[2][2] == 'o' and board[1][1] != 'o':
        return 'o'
    elif board[0][1] == 'o' and board[0][3] == 'o' and board[2][1] == 'o' and board[2][3] == 'o' and board[1][2] != 'o':
        return 'o'
    elif board[1][0] == 'o' and board[1][2] == 'o' and board[3][0] == 'o' and board[3][2] == 'o' and board[2][1] != 'o':
        return 'o'
    elif board[1][1] == 'o' and board[1][3] == 'o' and board[3][1] == 'o' and board[3][3] == 'o' and board[2][2] != 'o':
        return 'o'
    elif board[0][1] == 'o' and board[1][0] == 'o' and board[1][2] == 'o' and board[2][1] == 'o' and board[1][1] != 'o':
        return 'o'
    elif board[0][2] == 'o' and board[1][1] == 'o' and board[1][3] == 'o' and board[2][2] == 'o' and board[1][2] != 'o':
        return 'o'
    elif board[1][1] == 'o' and board[2][0] == 'o' and board[2][2] == 'o' and board[3][1] == 'o' and board[2][1] != 'o':
        return 'o'
    elif board[1][2] == 'o' and board[2][1] == 'o' and board[2][3] == 'o' and board[3][2] == 'o' and board[2][2] != 'o':
        return 'o'

    
    return None




def get_move(player):
    return input(player + ' player, chose your move: ')


"""
Modify board by making player make the given move, and return True if
successful.

Inputs:
    player      must be either 'x' or 'o'
    move        must be a string, should be a number 1, 2, 3, or 4
                followed by a capital letter A, B, C, or D, such as
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
    elif move[0] != '1' and move[0] != '2' and move[0] != '3' and move[0] != '4':
        return False
    elif move[1] != 'A' and move[1] != 'B' and move[1] != 'C' and move[1] != 'D':
        return False
    
    
    row = int(move[0]) - 1
    
    
    
    
    column = ord(move[1]) - ord('A')

    
    if board[row][column] == 'x' or board[row][column] == 'o':
        return False
    else:
        board[row][column] = player
        return True





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'




























    

