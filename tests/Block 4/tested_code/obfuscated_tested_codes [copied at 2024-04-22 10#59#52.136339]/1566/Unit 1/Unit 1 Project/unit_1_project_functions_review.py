




"""R
This makes it crash:

1. INVALID INPUT TWICE
  ┌───┬───┬───┐ 
1 │ X │ o │   │ 
  ├───┼───┼───┤ 
2 │   │   │   │ 
  ├───┼───┼───┤ 
3 │   │   │   │ 
  └───┴───┴───┘ 
    A   B   C   
o player, choose your move: 1A
o player, choose your size (1 or 2): 2
That is not a valid move.
o player, choose your move: 1A
o player, choose your size (1 or 2): 1
Traceback (most recent call last):
  File "/Users/pcsp1/Dropbox/PCS 1 - Jeffrey Yang/Unit 1 Project/unit_1_project.py", line 59, in <module>
    replace_complete = replace(piece, piece_size, board, int(next_move[0]) - 1, ord(next_move[1]) - ord('A'))
  File "/Users/pcsp1/Dropbox/PCS 1 - Jeffrey Yang/Unit 1 Project/unit_1_project_functions.py", line 94, in replace
    initial_piece = board[row][column] # Selects the square the piece will be played on


2. INVALID INPUT AT CHOOSE SIZE SPOT
  ┌───┬───┬───┐ 
1 │ x │   │   │ 
  ├───┼───┼───┤ 
2 │ o │   │   │ 
  ├───┼───┼───┤ 
3 │   │   │   │ 
  └───┴───┴───┘ 
    A   B   C   
x player, choose your move: 1B
x player, choose your size (1 or 2): @
Traceback (most recent call last):
  File "/Users/pcsp1/Dropbox/PCS 1 - Jeffrey Yang/Unit 1 Project/unit_1_project.py", line 32, in <module>
    piece_size = get_size(player)
  File "/Users/pcsp1/Dropbox/PCS 1 - Jeffrey Yang/Unit 1 Project/unit_1_project_functions.py", line 141, in get_size
    size = int(input(player + ' player, choose your size (1 or 2): '))
ValueError: invalid literal for int() with base 10: '@'


3. HOW DOES THE SIZE WORK?
x player, choose your size (1 or 2): 1
  ┌───┬───┬───┐ 
1 │ X │ x │ x │ 
  ├───┼───┼───┤ 
2 │ O │ o │   │ 
  ├───┼───┼───┤ 
3 │   │   │   │ 
  └───┴───┴───┘ 
    A   B   C   

The x player wins!
IF THE SIZE 2 CAN REPLACE THE SIZE 1, THEN NO ONE's GOING TO USE SIZE 1.
"""



"""
player is x or o
Moves are referred to by strings such as '1A' or '2C'
size gives the move a size of 1 or 2
piece is X, x, o and O
size_of() determines the size of the piece based on if its a big or small piece
get_size() gets the size the player inputs
replace() checks if a piece you play can replace a piece the computer played



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



def size_of(piece):
    if piece == 'x' or piece =='o':
        size = 1
        return size
    elif piece =='X' or piece == 'O':
        size = 2
        return size
    else:
        size = 0
        return size


def make_piece(player, size):
    if player == 'x': 
        if size == 2:
            return 'X'
        else:
            return 'x'
    elif player == 'o':
        if size == 2:
            return 'O'
        else:
            return 'o'
    else:
        return ' '
    


def replace(piece, size, row, column, board):
    initial_piece = board[row][column] 
    initial_size = size_of(initial_piece)
    
    if initial_size < size:
        board[row][column] = make_piece(next_player(piece), size) 
        return True
    else:
        return False

        


def find_winner(board):
    
    for row in range(0,len(board)):
        if (board[row][0].lower() == board[row][1].lower()
            and board[row][0].lower() == board[row][2].lower()
            and board[row][0] != ' '):
            return board[row][0].lower()
    
    for column in range(0, len(board)):
        if (board[0][column].lower() == board[1][column].lower() and
            board[0][column].lower() == board[2][column].lower()
            and board[0][column] != ' '):
            return board[0][column].lower()
    
    if (board[0][0] == board[1][1].lower()
        and board[0][0].lower() == board[2][2].lower()
        and board[0][0] != ' '):
        return board[0][0].lower()
    elif (board[0][2].lower() == board[1][1].lower()
          and board[0][2].lower() == board[2][0].lower()
          and board[0][0] != ' ') :
        return board[1][1].lower()
    else:
        return None

    



def get_move(player):
    return input(player + ' player, choose your move: ')



def get_size(player):
    size = int(input(player + ' player, choose your size (1 or 2): '))
    return size



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

def make_move(piece, move, board):
    
    if len(move) != 2:
        return False
    if move[0] != '1' and move[0] != '2' and move[0] != '3':
        return False
    if move[1] != 'A' and move[1] != 'B' and move[1] != 'C':
        return False
    
    
    
       

    
    
    row = int(move[0]) - 1
    
    
    
    column = ord(move[1]) - ord('A')

    
    

    
    if board[row][column] != ' ':
        initial_piece_size = size_of(board[row][column])
        if size_of(piece) == initial_piece_size:
            return False
        elif size_of(piece) > initial_piece_size:
            board[row][column] = piece
            return True
        else:
            return False

    board[row][column] = piece
    return True





def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'
