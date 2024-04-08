

heal_prob = 0.7
infect_prob = 0.3

import random

random.seed()

def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ '
          + row[4] + ' │ '
          + row[5] + ' │ '
          + row[6] + ' │ '
          + row[7] + ' │ '
          + row[8] + ' │ '
          + row[9] + ' │ '
          + row[0] + ' │ ')

def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ')
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
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[10], 0)
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   G   H   I   J   ')
    
    return board




def create_infection(empty_board, num_infected):
    rows = len(empty_board)
    cols = len(empty_board[0])
    num_of_infected = 0

  
    while num_of_infected < num_infected:
        row = random.randint(0, rows - 2)
        col = random.randint(0, cols - 2)
        if empty_board[row][col] == ' ':
            empty_board[row][col] = 'X'
            num_of_infected = num_of_infected + 1



def num_adjacent_infected(board, row, col):
    adjacent_infected = 0
    rows, cols = len(board), len(board[0])

    
    if row - 1 >= 0 and board[row - 1][col] == 'X':
        adjacent_infected += 1
    
    if col - 1 >= 0 and board[row][col - 1] == 'X':
        adjacent_infected += 1
    
    if col + 1 < cols and board[row][col + 1] == 'X':
        adjacent_infected += 1
    
    if row + 1 < rows and board[row + 1][col] == 'X':
        adjacent_infected += 1
    return adjacent_infected


    return adjacent_infected


def heal_probability(board):
    for row in range(0, len(board)-1):
        for col in range(0, len(board[row])-1):
            if board[row][col] == 'X':
                if random.random() < heal_prob:
                    board[row][col] = ' '
    return board



def count_infected(board):
    total_infected = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'X':  
                total_infected += 1
    return total_infected


   


def cured_board(board, infected, cured):
    for row, column in cured:
        board[row][column] = ' '
    return board

def infect_probability(board, infected):
    rows = len(board)
    cols = len(board[0])
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if board[row][col] == ' ':
                num_adj_infected = num_adjacent_infected(infected, row, col)
                infect_chance = infect_prob * num_adj_infected
                if random.random() < infect_chance:
                    board[row][col] = 'X'
    return board

def is_board_full(board):
    for row in range(1, len(board)-1):
        for col in range(1, len(board[row])-1):
            if board[row][col] == ' ':
                return False
    return True
