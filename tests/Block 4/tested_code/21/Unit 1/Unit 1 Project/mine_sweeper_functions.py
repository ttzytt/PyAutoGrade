

import random

random.seed()











import random

random.seed()

def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ '
          + row[4] + ' │ ')

def draw_board(board):
    print('  ┌───┬───┬───┬───┐ ')
    draw_row(board[1], 1)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[2], 2)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[3], 3)
    print('  ├───┼───┼───┼───┤ ')
    draw_row(board[4], 4)
    print('  └───┴───┴───┴───┘ ')
    print('    A   B   C   D ')
    return board

def create_mines(num_mines):
    mines_board = [[' ', ' ', ' ',' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ']]
    rows = len(mines_board)
    cols = len(mines_board[0])
    num_of_mines = 0
    
    while num_of_mines < num_mines:
        row = random.randint(1, rows - 2)
        col = random.randint(1, cols - 2)
        if mines_board[row][col] == ' ':
            mines_board[row][col] = '*'
            num_of_mines = num_of_mines + 1
    return mines_board

def get_move(player):
    return input('player ' + str(player) + ' choose your move: ')

def make_move(player, move, board, mines, previous_moves):
    if not check_move(move):
        print('Invalid move. Try again.')
        return False

    row = int(move[0]) - 1
    column = ord(move[1]) - ord('A')

    
    row += 1
    column += 1

    if (row, column) in previous_moves:
        print('You have already made this move. Try again.')
        return False

    previous_moves.append((row, column))

    if mines[row][column] == '*':
        board[row][column] = '*'
        print('You have hit a mine!')
        return 'mine'
    
    board[row][column] = str(num_adjacent_mines(mines, row, column))
    return True


def check_move(move):
    if len(move) != 2:
        return False

    if move[0] != '1' and move[0] != '2' and move[0] != '3' and move[0] != '4':
        return False
    if move[1] != 'A' and move[1] != 'B' and move[1] != 'C' and move[1] != 'D':
        return False

    return True



def num_adjacent_mines(mines, row, col):
    adjacent_mines = 0
    rows, cols = len(mines), len(mines[0])

    
    if row - 1 >= 0 and col - 1 >= 0 and mines[row - 1][col - 1] == '*':
        adjacent_mines += 1
    
    if row - 1 >= 0 and mines[row - 1][col] == '*':
        adjacent_mines += 1
    
    if row - 1 >= 0 and col + 1 < cols and mines[row - 1][col + 1] == '*':
        adjacent_mines += 1
    
    if col - 1 >= 0 and mines[row][col - 1] == '*':
        adjacent_mines += 1
    
    if col + 1 < cols and mines[row][col + 1] == '*':
        adjacent_mines += 1
    
    if row + 1 < rows and col - 1 >= 0 and mines[row + 1][col - 1] == '*':
        adjacent_mines += 1
    
    if row + 1 < rows and mines[row + 1][col] == '*':
        adjacent_mines += 1
    
    if row + 1 < rows and col + 1 < cols and mines[row + 1][col + 1] == '*':
        adjacent_mines += 1

    return adjacent_mines


    return adjacent_mines

def is_board_full(board):
    for row in range(1, len(board)-1):
        for col in range(1, len(board[row])-1):
            if board[row][col] == ' ':
                return False
    return True

def next_player(player):
    if player == 1:
        return 2
    else:
        return 1
