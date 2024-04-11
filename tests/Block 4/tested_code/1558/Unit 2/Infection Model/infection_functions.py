




import random

"""
The following functions are for the Infection Model simulation. This is a simulation showing the spreading
of an infections disease.
There are people on a 10 by 10 grid.

Each round, 10 people start infected and the rest start healthy.
The configuration of infected individuals in the starting field
is random.

For the code the board is a list of 10 lists where
'.' is a healthy person and 'x' is an infected person. 

  [ ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', 'x', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', 'x', '·', '·', '·'],
    ['·', 'x', '·', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', 'x', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·', 'x', '·'],
    ['·', '·', 'x', 'x', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', 'x', '·', '·', '·', 'x', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·'] ]
For the user it is printed in the form
    ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ 
    │ · │ · │ · │ · | · | · | · | · | · | · |
    ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ 
    │ · │ · │ x │ · | · | · | · | · | · | · | 
    ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ 
    │ · │ · │ · │ · | · | · | x | · | · | · | 
    ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ 
    │ · │ x │ · │ · | · | · | · | · | · | · |  
    ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ 
    │ · │ · │ · │ · | x | · | · | · | · | · | 
    ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ 
    │ · │ · │ · │ · | · | · | · | · | x | · |  
    ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ 
    │ · │ · │ x │ x | · | · | · | · | · | · | 
    ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ 
    │ · │ · │ · │ · | · | · | · | · | · | · | 
    ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ 
    │ · │ · │ · │ x | · | · | · | x | · | · |
    ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ 
    │ · │ · │ · │ · | · | · | · | · | · | · |
    └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘


Every round, each infected person has a chance
(heal_probibility) to heal. Each healthy person has a chance
(infection_probability * num_infected_neighbors) where neighbors
those who are directly above, below or next to the person.


- Initial Infected: 10
- Infection Probability: 0.1
- Heal Probability: 0.2

"""

def draw_row(row):
    print('  │ '
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
    draw_row(board[0])
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[1])
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[2])
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[3])
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[4])
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[5])
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[6])
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[7])
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[8])
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(board[9])
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')

"""
Makes the whole board healthy then randomly chooses an
initial_infected number of squares in the board and makes
them infected.
"""
def initialize_board(size, initial_infected):
    
    
    board = [['·' for _ in range(size)] for _ in range(size)]

    
    for _ in range(initial_infected):
        
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        board[row][col] = 'x'

    return board
"""
Checks for vertical or horizontal neighbors in a spot on the
board, which is specified before the function is called.
"""
def count_infected_neighbors(board, row, col):
    size = len(board)
    infected_neighbors = 0
    
    
    if col > 0 and board[row][col - 1] == 'x':
        infected_neighbors += 1
        
    
    if col < size - 1 and board[row][col + 1] == 'x':
        infected_neighbors += 1
        
    
    if row > 0 and board[row - 1][col] == 'x':
        infected_neighbors += 1
        
    
    if row < size - 1 and board[row + 1][col] == 'x':
        infected_neighbors += 1

    return infected_neighbors


"""
Makes a new grid where each infected 'x' has a chance to heal
and become a '·' and each healthy '·' has a chance to become an
infected 'x'. 

"""
def update_board(board, infection_probability, heal_probability):
    size = len(board) 
    new_board = [['·' for _ in range(size)] for _ in range(size)]

    for row in range(size):
        for col in range(size):
            if board[row][col] == 'x':
                      
                
                if random.random() < heal_probability:
                    new_board[row][col] = '·'
                else:
                    new_board[row][col] = 'x'
            else:
                
                num_infected_neighbors = count_infected_neighbors(board, row, col)

                
                if num_infected_neighbors != 0:
                    infection_chance = infection_probability * num_infected_neighbors
                else:
                    infection_chance = infection_probability
                
                if random.random() < infection_chance:
                    new_board[row][col] = 'x'

    return new_board
