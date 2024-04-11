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

"""
What combinations of probabilities lead to the
virus eventually being eradicated, and when does the virus stick around?

If heal_prob is high (close to 1) and infect_prob is low (close to 0), there's a high chance that infected individuals will be cured before they can spread the virus, leading to the virus being eradicated.
If heal_prob is low and infect_prob is high, infected individuals are less likely to be cured, and the virus can spread rapidly and stay alive. I assume that a heal prob of 0.7 and an infect prob of 0.3 would eventually eradicate the virus but after many trials.
"""
