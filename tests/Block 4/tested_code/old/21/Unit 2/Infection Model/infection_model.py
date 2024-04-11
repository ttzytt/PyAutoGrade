from infection_functions import *
import random
random.seed()



num_initial_infected = 5
heal_prob = 0.7
infect_prob = 0.3


board = [[' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]



create_infection(board, num_initial_infected)
draw_board(board)





while not is_board_full(board):
    
    print()


    
    continuation = input("Would you like to continue? (no to exit) ").lower()
    if continuation == "no":
        break


    
    cured = []
    for row in range(0, 11):
        for col in range(0, 11):
            if board[row][col] == 'X':
                if random.random() < heal_prob:
                    cured.append((row, col))
            elif board[row][col] == ' ':
                num_adj_infected = num_adjacent_infected(board, row, col)
                infect_chance = infect_prob * num_adj_infected
                if random.random() < infect_chance:
                    board[row][col] = 'X'

    
    for row, col in cured:
        board[row][col] = ' '

    draw_board(board)
    create_infection(board, num_initial_infected)


