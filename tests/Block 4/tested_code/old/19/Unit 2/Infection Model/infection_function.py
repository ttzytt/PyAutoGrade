





















import random




def create_grid(num_rows, num_columns, board):   
    
    
    for i_r in range(num_rows + 2):
        board.append([])
        for i_c in range(num_columns + 2):
            board[i_r].append(0)




def place_infected(num_rows, num_columns, board, num_infected):
    
    actual_num_infected = 0
    
    while actual_num_infected < num_infected:
        
        random_row = random.randint(1, num_rows)
        random_column = random.randint(1, num_columns)
        
        if board[random_row][random_column] == 0:
            board[random_row][random_column] = 1
            actual_num_infected += 1
        



def check_infected(board, row, column):
    
    return (board[row + 1][column]) + (board[row][column + 1]) + (board[row - 1][column]) + (board[row][column - 1])




def execute_round(num_rows, num_columns, board, infection_prob, heal_prob):

    new_board = []

    
    
    
    create_grid(num_rows, num_columns, new_board)
    
    for i_r in range(1, num_rows + 1):
        for i_c in range(1, num_columns + 1):
            
            if board[i_r][i_c] == 1:
                if random.random() < heal_prob:
                    
                    new_board[i_r][i_c] = 0
                else:
                    new_board[i_r][i_c] = 1
            else:
                
                
                if random.random() < infection_prob * check_infected(board, i_r, i_c):
                    new_board[i_r][i_c] = 1
                else:
                    new_board[i_r][i_c] = 0

    
    return new_board



def draw_board(board, num_rows, num_columns):
    
    total = 0
    
    
    for i_r in range(1, num_rows + 1):
        for i_c in range(1, num_columns + 1):
            if board[i_r][i_c] == 0:
                
                print('·', end=" ")
            else:
                print('x', end=" ")
                total += 1
        
        print()
    
    return total



def count_infected(board, num_rows, num_columns):
    
    total = 0
    
    for i_r in range(1, num_rows + 1):
        for i_c in range(1, num_columns + 1):
            if board[i_r][i_c] == 1:
                total += 1
    
    return total
