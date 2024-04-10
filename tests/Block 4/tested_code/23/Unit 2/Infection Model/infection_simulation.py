




from infection_functions import *
import random


virus_infection_probability = float(
        input('Give virus infection probability as a float between 0 and 1: '))
heal_probability = float(
        input('Give heal probability as a float between 0 and 1: '))
grid = initialize_grid()


num_rounds = 1




print()
print("Here's the resulting grid: ")
print_grid(grid)
if is_grid_mixed(grid) == False:
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            
            if grid[row][col] == '·':
                print('Everyone ended up healthy!')
            
            elif grid[row][col] == 'x':
                print('Everyone was infected.')
else:
    print('The board never settled, results were mixed.')

print('This simulation ran ' + str(num_rounds) + ' round(s).')
    
        
    

