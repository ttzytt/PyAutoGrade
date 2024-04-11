



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
    
    
    
    def convert_to_string_bitboard(board, value):
        bitboard = ''
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == value:
                    bitboard += '1'
                else:
                    bitboard += '0'
        return bitboard

    
    '''
    Structure:
    1 2 3
    4 5 6
    7 8 9
    (not starting from 0)
    '''
    winning_groups = [
        [1,2,3], [4,5,6], [7,8,9],
        [1,4,7], [2,5,8], [3,6,9],
        [1,5,9], [3,5,7], 
        ]

    
    x_bitboard = convert_to_string_bitboard(board, 'x')
    for group in winning_groups:
        is_all_value = True
        for i in group:
            
            if x_bitboard[i-1] == '0':
                is_all_value = False
        if is_all_value:
            return 'x'
    
    o_bitboard = convert_to_string_bitboard(board, 'o')
    for group in winning_groups:
        is_all_value = True
        for i in group:
            if o_bitboard[i-1] == '0':
                is_all_value = False
        if is_all_value:
            return 'o'
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
    
    
    
    if (len(move) != 2):
        return False          
    is_valid_row = ((move[0] == '1') or (move[0] == '2') or (move[0] == '3'))
    is_valid_column = ((move[1] == 'A') or (move[1] == 'B') or (move[1] == 'C'))
    if not (is_valid_row and is_valid_column):
        return False
    
    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    
    if board[row][column] != ' ':
        return False
    board[row][column] = player
    return True





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

