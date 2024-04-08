

import random
random.seed()


def draw_row(row, row_number):
    print(str(row_number) + ' │ '
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

def draw_board(infection_board):
    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ')
    draw_row(infection_board[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(infection_board[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(infection_board[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(infection_board[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(infection_board[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(infection_board[5], 6)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(infection_board[6], 7)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(infection_board[7], 8)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(infection_board[8], 9)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(infection_board[9], 0)
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   G   H   I   J ')




def check_neighbors(board, row, column):
    infected_neighbors = 0
    if row > 0:
        if board[row-1][column] == '+':
            infected_neighbors += 1
    if row < 9:
        if board[row+1][column] == '+':
            infected_neighbors += 1
    if column > 0:
        if board[row][column - 1] == '+':
            infected_neighbors += 1
    if column < 9:
        if board[row][column + 1] == '+':
            infected_neighbors += 1
    return infected_neighbors


def draw_patients_cured(board, patients, cured):
    for count in range(len(patients)):
        row = patients[count][0]
        column = patients[count][1]
        board[row][column] = '+'
    for i in range(len(cured)):
        row = cured[i][0]
        column = cured[i][1]
        board[row][column] = ' '
    return board


def count_patients(board):
    num_patients = 0
    for r in range(10):
        for c in range(10):
            if board[r][c] == '+':
                num_patients += 1
    return num_patients

