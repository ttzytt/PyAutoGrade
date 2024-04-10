


import random

def draw_grid(board):
    for row in range(1, 11):
        for column in range(1, 11):
            if board[row][column] == 0:
                print('· ', end = '')
            else:
                print('x ', end = '')
        print()
            


def infected_neighbors(a, b, board):
    
    return board[a][b - 1] + board[a][b + 1] + board[a - 1][b] + board[a + 1][b]
        

def infection_simulation(heal_probability, infection_probability, old_board, repetition):

    new_board = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for _ in range(repetition):

        for row in range(1, 11):
            for column in range(1, 11):

                
                if old_board[row][column] == 1:
                    if random.random() < heal_probability:
                        new_board[row][column] = 0
                    else:
                        new_board[row][column] = 1

                
                else:
                    if random.random() < infection_probability * infected_neighbors(row, column, old_board):
                        new_board[row][column] = 1
                    else:
                        new_board[row][column] = 0
        
        draw_grid(new_board)
        print('------------------')

        
        old_board, new_board = new_board, old_board

    return old_board


