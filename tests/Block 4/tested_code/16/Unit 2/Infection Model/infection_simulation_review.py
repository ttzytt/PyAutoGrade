



from infection_functions import *






board = [ [' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
          [' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x']]

heal_probability = 0.9
infection_probability = 0.5



rounds = int(input('How many rounds would you like to run? '))
for i in range(rounds):
    mark_numbers(board)
    heal_infected(board, heal_probability)
    infect(board, infection_probability)
draw_board(board)





