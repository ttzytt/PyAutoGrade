

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
    print('  ┌───┬───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[5], 6)
    print('  ├───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[6], 7)
    print('  └───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   ')
    



def all_equal(my_list):
    if len(my_list) == 0: 
        return None
    for i in range(len(my_list) - 1):
        
        if my_list[i] != my_list[i + 1]:
           return False
    return True 





def find_winner(board):
    
    if (all_equal([board[0][0], board[1][1], board[2][2]])
            or all_equal([board[2][0], board[1][1], board[0][2]])):
        if board[1][1] == ' ':
            return None
        
        return board[1][1]
    
    
    
    for row in range(len(board)):
        if all_equal(board[row]) and board[row][0] != ' ':
            return board[row][0]

    
    for column in range(len(board)):
        new_list = []
        for row in range(len(board[0])):
            new_list.append(board[row][column]) 
        if all_equal(new_list):
            return board[0][column]
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
    if not ('1' <= move[0] <= '3' and 'A' <= move[1] <= 'C'):
        return False
        
    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    
    if board[row][column] == 'x' or board[row][column] == 'o':
        return False
  
    board[row][column] = player
    return True






def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

