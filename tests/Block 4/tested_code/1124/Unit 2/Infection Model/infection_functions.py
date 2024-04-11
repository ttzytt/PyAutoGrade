




import random
random.seed()



def draw_row(row,row_number):
    print(str(row_number) + ' | '
               + row[0] + ' | '
               + row[1] + ' | '
               + row[2] + ' | '
               + row[3] + ' | '
               + row[4] + ' | '
               + row[5] + ' | '
               + row[6] + ' | '
               + row[7] + ' | '
               + row[8] + ' | '
               + row[9] + ' | ')


def draw_board(board):
    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐  ')
    draw_row(board[0], 0)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
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
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   G   H   I   J   ')



def set_infected(num_infected, board):
    while num_infected > 0:
        row = random.randint(0, 9) 
        column = random.randint(0, 9)
        if board[row][column] == ' ':
            board[row][column] = 'x'
            num_infected -= 1 




def num_neighbors_different(board, row, column):
    
    num_different = 0

    
    
    
    if row > 0 and board[row][column] != board[row-1][column]:
        num_different += 1
    
    if row < 9 and board[row][column] != board[row+1][column]:
        num_different += 1
    
    if column > 0 and board[row][column] != board[row][column-1]:
        num_different += 1
    
    if column < 9 and board[row][column] != board[row][column+1]:
        num_different += 1

    return num_different





def change_state(board, changing_board, infection_probability, heal_probability):
    
    
    for row in range(10):
        for column in range(10):
            
            if board[row][column] == ' ':
                
                infected_or_not = num_neighbors_different(board, row, column) * infection_probability
                
                probability = random.random()
                
                if probability < infected_or_not:
                    changing_board[row][column] = 'x'
                
                else:
                    changing_board[row][column] = ' '
            
            elif board[row][column] == 'x':
                probability = random.random()
                if probability < heal_probability:
                    changing_board[row][column] = ' '
                else:
                    changing_board[row][column] = 'x'    
        
