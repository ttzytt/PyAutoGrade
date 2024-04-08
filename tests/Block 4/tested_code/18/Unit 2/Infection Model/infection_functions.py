




import random



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


def initialize_board(size, initial_infected):
    
    
    board = [['·' for _ in range(size)] for _ in range(size)]

    
    for _ in range(initial_infected):
        
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        board[row][col] = 'x'

    return board

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
