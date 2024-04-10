




import random
from infection_functions import*


rows = 10
columns = 10
rounds_of_simulation = 10

board = make_board(rows, columns)

for _ in range(rows * columns // 10): 
    i = random.randint(0, rows - 1) 
    j = random.randint(0, columns - 1)
    board[i][j] = 'x'
    
print('Initial board: ')

for row in board:
    for cell in row:
        print(cell, end = ' ')
    print()
print()

for number_of_rounds in range(rounds_of_simulation):
    
    
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
    
    print(f'Round {number_of_rounds + 1}: ')
    for row in board:
        for cell in row:
            print(cell, end = ' ')
        print()
    print()
