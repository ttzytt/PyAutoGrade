


















from infection_functions import *

import random
random.seed()


board =  [['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·'],
          ['·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·', '·']]


infection_probability = float(input("Enter the infection probability:"))
heal_probability = float(input("Enter the heal probability:"))
total_days = int(input("How many days would you like to run the simulation for:"))
days = 1
next_day = 1

board_generator(board)


while days < total_days and next_day == 1:
    num_infected_neighbors(board, probability_board)
    if_heal(board, heal_probability)
    if_infect(board, probability_board, infection_probability)
    print("Day " + str(days))
    draw_board(board)
    draw_board(probability_board)
    print()
    days += 1
    print("1 = yes, 2 = no")
    
    next_day = int(input("Would you like to proceed to the next day?"))
    
print("Simulation ended")
        
