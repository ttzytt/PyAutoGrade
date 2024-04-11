


import random

random.seed()

board = [ [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def draw_row(row, row_number):
    print(' │ '
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
    print(' ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ')
    draw_row(board[0], 1)
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[1], 2)
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2], 3)
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[3], 4)
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[4], 5)
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[5], 6)
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[6], 7)
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[7], 8)
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[8], 9)
    print(' ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[9], 10)
    print(' └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')



def heal_or_infect(board, row, column, heal_prob, infection_prob):
    multiplier = 0
    if board[row][column] == 'x':
        if heal_prob > random.random():
            board[row][column] = '·'
        return board[row][column]

    else:
        if row == 0:
            if column == 0:
                if board[row + 1][column] == 'x':
                    multiplier += 1
                if board[row][column + 1] == 'x':
                    multiplier += 1
            elif column == 9:
                if board[row + 1][column] == 'x':
                    multiplier += 1
                if board[row][column - 1] == 'x':
                    multiplier += 1
            else:
                if board[row + 1][column] == 'x':
                    multiplier += 1
                if board[row][column + 1] == 'x':
                    multiplier += 1
                if board[row][column - 1] == 'x':
                    multiplier += 1                
                
        elif row == 9:
            if column == 0:
                if board[row - 1][column] == 'x':
                    multiplier += 1
                if board[row][column + 1] == 'x':
                    multiplier += 1
            elif column == 9:
                if board[row - 1][column] == 'x':
                    multiplier += 1
                if board[row][column - 1] == 'x':
                    multiplier += 1
            else:
                if board[row - 1][column] == 'x':
                    multiplier += 1
                if board[row][column + 1] == 'x':
                    multiplier += 1
                if board[row][column - 1] == 'x':
                    multiplier += 1
        else:
            if column == 0:
                if board[row - 1][column] == 'x':
                    multiplier += 1
                if board[row + 1][column] == 'x':
                    multiplier += 1
                if board[row][column + 1] == 'x':
                    multiplier += 1
            elif column == 9:
                if board[row - 1][column] == 'x':
                    multiplier += 1
                if board[row + 1][column] == 'x':
                    multiplier += 1
                if board[row][column - 1] == 'x':
                    multiplier += 1
            else:
                if board[row - 1][column] == 'x':
                    multiplier += 1
                if board[row + 1][column] == 'x':
                    multiplier += 1
                if board[row][column + 1] == 'x':
                    multiplier += 1
                if board[row][column - 1] == 'x':
                    multiplier += 1
                
            

        if (multiplier * infection_prob) > random.random():
            board[row][column] = 'x'
        return board[row][column]    
        


    

