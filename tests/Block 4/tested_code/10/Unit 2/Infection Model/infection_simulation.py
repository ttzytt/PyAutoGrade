




from infection_functions import *






board =   [ [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] ]


from infection_functions import initialize_board, update_board



initial_infected = 99
infection_probability = 0.1
heal_probability = 0.2

print('Welcome to the Infection simulation')
print('This simulation will start with people in a 10x10 grid, where 10 are infected')
print('infected people are marked with an x and healthy people are marked with a ·')
print()
print(f'Each healthy person has a {infection_probability} chance to get sick')
print(f'Each infected person has a  {heal_probability} chance to heal')
print()


board = initialize_board(10, initial_infected)


num_rounds = 1000

for round_num in range(num_rounds):
    print(f'Round {round_num + 1}')
    draw_board(board)  

    
    input('Press Enter to continue')
    print()

    
    board = update_board(board, infection_probability, heal_probability)


print()
print('Simulation complete. Max rounds gone through')
