






import random

def make_board(rows, columns):
    board = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append('·')
        board.append(row)
    return board


def make_people(board):
    board_with_people = []
    for row in board:
        person_row = []
        for i in row:
            if i == '·':
                person_row.append('·')
            else:
                person_row.append('x')
        board_with_people.append(person_row)
    return board_with_people
    

def infection_probability(board):
    
    rows = len(board)
    columns = len(board[0])
    probability_infection = []
    
    for i in range(rows):
        store_row = []
        for j in range(columns):
            
            neighbor_infected  = num_infected_neighbors(board, i, j)
            
            if not board[i][j] == 'x':
                
                if neighbor_infected > 0:
                    
                    
                    infection_prob = (neighbor_infected * 0.15)
                    store_row.append(infection_prob)
                
                else:
                    store_row.append(0)
            else:
                store_row.append(0)
        
        probability_infection.append(store_row)
    return probability_infection


def heal_probability(board):
    
    rows = len(board)
    columns = len(board[0])
    probability_of_heal = []

    for row in range(rows):
        store_row = []
        for column in range(columns):
            
            if board[row][column] == 'x':
                store_row.append(0.2)
            
            else:
                store_row.append(0)
        probability_of_heal.append(store_row)
    
    return probability_of_heal


def num_infected_neighbors(board, row, column):
    rows = len(board)
    columns = len(board[0])
    neighbors_infected = 0
    
    
    if row > 0 and board[row - 1][column] == 'x': 
        neighbors_infected += 1
    if row < rows - 1 and board[row + 1][column] == 'x': 
        neighbors_infected += 1
    if column > 0 and board[row][column - 1] == 'x': 
        neighbors_infected += 1
    if column < columns - 1 and board[row][column + 1] == 'x': 
        neighbors_infected += 1
        
    
    return neighbors_infected

