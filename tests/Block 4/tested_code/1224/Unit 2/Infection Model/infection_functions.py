






probability_board =[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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


import random
random.seed()



def board_generator(board):
    current_row = 1
    current_column = 1
    times_ran = 0
    random_num = 0
    while times_ran < 100:
        random_num = random.random()
        if random_num < 0.1:
            board[current_row][current_column] = 'X'

        if current_column < 10:
            current_column += 1
        else:
            current_row += 1
            current_column = 1

        times_ran += 1
        


def draw_board(board):
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])
    print(board[6])
    print(board[7])
    print(board[8])
    print(board[9])
    print(board[10])
    print(board[11])
    

        


def num_infected_neighbors(board, probability_board):
    
    current_row = 1
    current_column = 1
    amount_infected = 0
    times_ran = 0
    
    while times_ran < 100:
        
        amount_infected = 0
        
        if board[current_row][current_column] == '·':
            if board[current_row + 1][current_column] == 'X':
                amount_infected += 1
            if board[current_row - 1][current_column] == 'X':
                amount_infected += 1
            if board[current_row][current_column + 1] == 'X':
                amount_infected += 1
            if board[current_row][current_column - 1] == 'X':
                amount_infected += 1
            probability_board[current_row][current_column] = str(amount_infected)
        else:
            
            probability_board[current_row][current_column] = '-1'
        
        if current_column < 10:
            current_column += 1
        else:
            current_row += 1
            current_column = 1
            
        times_ran += 1






def if_heal(board, heal_probability):
    current_row = 1
    current_column = 1
    times_ran = 0
    while times_ran < 100:
        
        if board[current_row][current_column] == 'X':
            rand_num = random.randint(0,100)
            
            if rand_num < heal_probability:
                board[current_row][current_column] = '·'
                num_infected_neighbors(board,probability_board)

        
        if current_column < 10:
            current_column += 1
        else:
            current_row += 1
            current_column = 1
        times_ran += 1


def if_infect(board, probability_board, infection_probability):
    current_row = 1
    current_column = 1
    times_ran = 0
    while times_ran < 100: 
        if board[current_row][current_column] == '·':
            rand_num = random.randint(0,99)
            
            if rand_num < (infection_probability * int(probability_board[current_row][current_column])):
                board[current_row][current_column] = 'X'
                num_infected_neighbors(board,probability_board)

        
        if current_column < 10:
            current_column += 1
        else:
            current_row += 1
            current_column = 1
        times_ran += 1




            
