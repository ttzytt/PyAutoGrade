import random
random.seed()


def draw_row(row):
    print(' │ '
          + str(row[1]) + ' │ '
          + str(row[2]) + ' │ '
          + str(row[3]) + ' │ '
          + str(row[4]) + ' │ '
          + str(row[5]) + ' │ '
          + str(row[6]) + ' │ '
          + str(row[7]) + ' │ '
          + str(row[8]) + ' │ '
          + str(row[9]) + ' │ '
          + str(row[10]) + ' │ ')
    

def draw_board(board):
    print(' ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ')
    draw_row(board[1])
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2])
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[3])
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[4])
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[5])
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[6])
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[7])
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[8])
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[9])
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    draw_row(board[10])
    print(' └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')
    


def make_sick(sick_probability, board):

    for row in range(1, 11):
        for column in range(1, 11):
            if random.randint(1, 100) < sick_probability:
                board[row][column] = 'X'
            else:
                board[row][column] = '·'

def probability_to_switch(sick_probability, heal_probability, row, column, board):

    num_of_sick_neighbors = 0

    if board[row][column] == 'X':
        return heal_probability
    else:
        num_of_sick_neighbors = 0

        if board[row][column + 1] == 'X':
            num_of_sick_neighbors += 1
        if board[row][column - 1] == 'X':
            num_of_sick_neighbors += 1
        if board[row + 1][column] == 'X':
            num_of_sick_neighbors += 1
        if board[row - 1][column] == 'X':
            num_of_sick_neighbors += 1

        return  sick_probability * num_of_sick_neighbors

def probability_board(sick_probability, heal_probability, board):
    prob_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    for row in range(1, 11):
        for column in range(1, 11):
            prob_board[row][column] = probability_to_switch(sick_probability, heal_probability, row, column, board)

    return prob_board

def switch_board(prob_board, board):
    for row in range(1, 11):
        for column in range(1, 11):
            switch_probability = prob_board[row][column]
            if random.randint(0, 99) < switch_probability:
                if board[row][column] == "X":
                    board[row][column] = "·"
                else:
                    board[row][column] = "X"
            


def existing_sick(board):
    for row in range(1, 11):
        for column in range(1, 11):
            if board[row][column] == "X":
                return True
    return False


    
def existing_regular(board):
    for row in range(1, 11):
        for column in range(1, 11):
            if board[row][column] == "·":
                return True
    return False

    
