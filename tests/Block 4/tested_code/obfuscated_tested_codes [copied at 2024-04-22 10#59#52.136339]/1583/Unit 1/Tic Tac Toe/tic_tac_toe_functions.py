

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


def all_equal(my_list):
    if len(my_list) == 0:
        return "Empty list"


    comparison_value = my_list[0] 
                                  
    for i in range(len(my_list)):
        if my_list[i] is not comparison_value: 
                                               
            return False
    return True 


def draw_board(board):
    def draw_row(row, row_number):
        print(str(row_number) + ' │ '
              + row[0] + ' │ '
              + row[1] + ' │ '
              + row[2] + ' │ ')
    
    print('  ┌───┬───┬───┐ ')
    draw_row(board[0], 1)
    print('  ├───┼───┼───┤ ')
    draw_row(board[1], 2)
    print('  ├───┼───┼───┤ ')
    draw_row(board[2], 3)
    print('  └───┴───┴───┘ ')
    print('    A   B   C   ')




def find_winner(board):
    diagonal_1 = []
    diagonal_2 = []
    for i in range(len(board)):
        
        testing_sequence = [] 
        testing_sequence = board[i] 
        if all_equal(testing_sequence) and board[i][0] != ' ':
            return testing_sequence[0]

        
        testing_sequence = [] 
        for j in range(len(board[i])):
            testing_sequence.append(board[j][i]) 
        if all_equal(testing_sequence) and board[j][0] != ' ':
            return testing_sequence[0]

        
        diagonal_1.append(board[i][i])
        diagonal_2.append(board[2-i][i])
    if all_equal(diagonal_1) and diagonal_1[0] != ' ':
        return diagonal_1[0]
    if all_equal(diagonal_2) and diagonal_2[0] != ' ':
        return diagonal_2[0]
    
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
    
    if len(move) != 2 or not (('1' <= move[0] <= '3') and \
                              ('A' <= move[1] <= 'C')):

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

