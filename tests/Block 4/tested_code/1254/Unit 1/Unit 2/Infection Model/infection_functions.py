




import random
random.seed()


def draw_row(row, row_num):
    print(str(row_num) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ '
          + row[4] + ' │ '
          + row[5] + ' │ '
          + row[6] + ' │ '
          + row[7] + ' │ '
          + row[8] + ' │ '
          + row[9] + ' │ ')


def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 0)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 1)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 2)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 3)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 4)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[5], 5)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[6], 6)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[7], 7)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[8], 8)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[9], 9)
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   G   H   I   J   ')
    

def check_infected(board, row, column):
    num_different = 0
    
    if row > 0 and board[row][column] != board[row - 1][column]:
        if board[row - 1][column] == 'x':
            num_different += 1
    if row < 9 and board[row][column] != board[row + 1][column]:
        if board[row + 1][column] == 'x':
            num_different += 1
    
    if column > 0 and board[row][column] != board[row][column - 1]:
        if board[row][column - 1] == 'x':
            num_different += 1
    if column < 9 and board[row][column] != board[row][column + 1]:
        if board[row][column + 1] == 'x':
            num_different += 1
    return num_different


def mark_numbers(board):
    for row in range(10):
        for column in range(10):
            
            if board[row][column] != 'x' and check_infected(board, row, column) != 0: 
                board[row][column] = str(check_infected(board, row, column))
    
    return board


def heal_infected(board, heal_probability):
    for row in range(10):
        for column in range(10):
            if board[row][column] == 'x':
                if random.random() < heal_probability: 
                    board[row][column] = ' '
                else:
                    board[row][column] = 'x'
    return board


def infect(board, infection_probability):
    for row in range(10):
        for column in range(10):
            if board[row][column] != 'x' and board[row][column] != ' ':
                
                
                if random.random() < infection_probability * int(board[row][column]):
                    board[row][column] = 'x'
                else:
                    board[row][column] = ' '
    return board           

            
            
