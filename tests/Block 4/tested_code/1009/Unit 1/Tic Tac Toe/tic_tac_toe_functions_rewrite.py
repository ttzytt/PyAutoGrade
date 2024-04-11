



"""
The following functions are for use in making a modified Tic-Tac-Toe game.

For all of the code below, a board 5 by 5 is a list of lists of the form
        [ [' ', 'o', ' ', 'x', ' '],
          ['x', ' ', 'x', 'o', ' '],
          ['x', 'o', ' ', 'x', 'o'],
          [' ', ' ', ' ', 'o', 'x'],
          ['o', 'x', ' ', ' ', 'x'] ]
(Each entry is an 'x', 'o', or ' '.)

For the player, a board will be printed in the form
      ┌───┬───┬───┬───┬───┐ 
    1 │   │ o │   │ x │   │ 
      ├───┼───┼───┼───┼───┤ 
    2 │ x │   │ x │ o │   │ 
      ├───┼───┼───┼───┼───┤ 
    3 │ x │ o │   │ x │ o │ 
      ├───┼───┼───┼───┼───┤ 
    4 │   │   │   │ o │ x │ 
      ├───┼───┼───┼───┼───┤ 
    5 │ o │ x │   │   │ x │ 
      └───┴───┴───┴───┴───┘ 
        A   B   C   D   E

For each cell, a value point is assigned; if a player can connect 3 or more adjacent cells, he/she will gain the corresponding points added, for example:
      ┌───┬───┬───┬───┬───┐               ┌───┬───┬───┬───┬───┐ 
    1 │ 3 │ 3 │ 3 │ 3 │ 3 │             1 │ x │   │ x │ x │   │ 
      ├───┼───┼───┼───┼───┤               ├───┼───┼───┼───┼───┤ 
    2 │ 3 │ 2 │ 1 │ 2 │ 3 │             2 │ x │ o │   │   │ o │ 
      ├───┼───┼───┼───┼───┤               ├───┼───┼───┼───┼───┤
    3 │ 3 │ 1 │ 1 │ 1 │ 3 │             3 │ x │   │ o │ o │ o │ 
      ├───┼───┼───┼───┼───┤               ├───┼───┼───┼───┼───┤ 
    4 │ 3 │ 2 │ 1 │ 2 │ 3 │             4 │ x │   │   │ o │   │ 
      ├───┼───┼───┼───┼───┤               ├───┼───┼───┼───┼───┤ 
    5 │ 3 │ 3 │ 3 │ 3 │ 3 │             5 │   │   │   │   │ o │ 
      └───┴───┴───┴───┴───┘               └───┴───┴───┴───┴───┘ 
        A   B   C   D   E                   A   B   C   D   E
    player x will get 3 + 3 + 3 + 3 = 12 points, play o will get (1 + 1 + 3) + (2 + 1 + 2 + 3) = 13 points

Moves/spaces are referred to by strings such as '1A' or '2C'. The game will continue until the board is full.       
"""

"""
Print the given row to the screen.
row: A list representing one row of the board
row_number: Integer to be printed before the row
"""
def draw_row(row, row_number):
    print(f'{row_number} │', end='')
    for cell in row:
        print(f' {cell} │', end='')
    print()

"""
Print the current board to the screen.
board: The 5x5 grid to be printed
"""
def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┐ ')
    for i in range(5):
        draw_row(board[i], i + 1)  
        if i < 4:
            print('  ├───┼───┼───┼───┼───┤ ')
    print('  └───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E ')


"""
Return the next player to move.
player: Current player ('x' or 'o')
return: The next player ('x' or 'o')
"""
def next_player(player):
    if player == 'x':
        return 'o'
    else:  
        return 'x'

    
"""
Ask the player for their move and return the string they enter.
player: Current player ('x' or 'o')
return: Valid move in the format (row, column)
"""
def get_move(player):
    while True: 
        move = input(f"Player {player}, enter your move (row and column): ")
        if len(move) == 2 and move[0].isdigit() and move[1].isalpha(): 
            row = int(move[0]) - 1
            col = ord(move[1].lower()) - ord('a')
            if 0 <= row < 5 and 0 <= col < 5:
                return row, col
        print('Invalid input or out of bounds. Please enter in the format "1A", "2B", "3C", etc.')


"""
Modify board by making player make the given move, and return True if successful.
Inputs:
    player      must be either 'x' or 'o'
    move        [row, col]
    board       see top of file
Return:
    If move is valid, then board is modified accordingly and the function returns True.
    If move is an invalid because the space is already occupied, then the board will not be modified and the function returns False.
"""
def make_move(player, move, board):
    
    row, col = move 
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else: 
        print("Space is already occupied. Try again.")
        return False

"""
Check if the board is fully occupied.
board: The game board
return: True if the board is full, False otherwise
"""
def is_board_full(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == ' ':
                return False
    return True


"""
Calculate and return the total points for a given player according to the board and point values.
Inputs:
    board: The game board
    board_points: Point values assigned to each cell in the board
    player: The player ('x' or 'o') for whom the score is to be calculated
Return: 
    Total points currently gained by the player
"""
def calculate_score(board, board_points, player):
    points = 0

    
    for row in range(5):
        count = 0
        tmp_points = 0 
        for col in range(5):
            if board[row][col] == player:
                tmp_points += board_points[row][col]
                count += 1
            else:
                if count >= 3:
                    points += tmp_points
                
                count = 0
                tmp_points = 0

        if count >= 3:
            points += tmp_points
    
    
    for col in range(5):
        count = 0
        tmp_points = 0
        for row in range(5):
            if board[row][col] == player:
                tmp_points += board_points[row][col]
                count += 1
            else:
                if count >= 3:
                    points += tmp_points
                
                count = 0
                tmp_points = 0
                
        if count >= 3:
            points += tmp_points
    
    
    for i in range(2,7):
        count = 0
        tmp_points = 0
        for j in range(5):
            
            if 0 <= i-j < 5:
                if board[j][i-j] == player:
                    tmp_points += board_points[j][i-j]
                    count += 1
                else:
                    if count >= 3:
                        points += tmp_points
                    
                    count = 0
                    tmp_points = 0
            else:
                if count >= 3:
                    points += tmp_points
                    
                count = 0
                tmp_points = 0

        if count >= 3:
            points += tmp_points
    
    
    for i in range (-2, 3): 
        count = 0
        tmp_points = 0
        for j in range(5):
            
            if 0 <= i+j <5:
                if board[j][i+j] == player:
                    tmp_points += board_points[j][i+j]
                    count += 1
                else:
                    if count >= 3:
                        points += tmp_points
                    
                    count = 0
                    tmp_points = 0
            else:
                if count >= 3:
                    points += tmp_points
                    
                count = 0
                tmp_points = 0

        if count >= 3:
            points += tmp_points

    return points

