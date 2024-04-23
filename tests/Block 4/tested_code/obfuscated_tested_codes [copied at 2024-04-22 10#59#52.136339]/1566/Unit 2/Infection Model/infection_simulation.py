


'''
Question 1: By setting the heal probability to 0.5 and the default infection
probability with 1 infected neighbo as 0.15, after 7 rounds of the simulation,
the code will eventually be eradicated.
'''


import random
from infection_functions import *

rows = 10
columns = 10
rounds_of_simulation = 10 

board = make_board(rows, columns)
for _ in range((rows * columns) // rows): 
    row = random.randint(0, rows - 1) 
    column = random.randint(0, columns - 1)
    board[row][column] = 'x'

for number_of_rounds in range(rounds_of_simulation):
    number_of_round = number_of_rounds + 1
    print('Round ' + str(number_of_round))
    print('Initial board: ')
    
    for row in board:
        for cell in row:
            
            
            print(cell, end= ' ')
        print()
    print()
    
    heal_probabilities = heal_probability(board)
    infect_probabilities = infection_probability(board)
    new_board = make_board(rows, columns)
    
    for row in range(rows):
        for column in range(columns):
            if board[row][column] == 'x':
                if random.random() < heal_probabilities[row][column]:
                    new_board[row][column] = '·'
                else:
                    new_board[row][column] = 'x'
            else:
                if random.random() < infect_probabilities[row][column]:
                    new_board[row][column] = 'x'
                else:
                    new_board[row][column] = '·'
    board = new_board

    
    print('New board')
    for row in board:
        for cell in row:
            print(cell, end= ' ')
        print()
    print()
