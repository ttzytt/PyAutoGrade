


from infection_functions import *


def infection_simulation(grid, cycles, heal_probability, infect_probability):


    
                     
    for i in range(cycles):

        
        
        next_grid = []
        for row in range(len(grid)):
            next_grid.append(grid[row][:]) 
                                           
                                           

        
        
        for person_y in range(len(grid) - 2):
            for person_x in range(len(grid[0]) - 2):
                if grid[person_y+1][person_x+1] == 'x': 
                    heal_infected(heal_probability, person_x, person_y, grid,
                                  next_grid)

                else: 
                    infect_healthy(infect_probability, person_x, person_y,
                                   grid, next_grid)
        grid = next_grid
        print('Cycle ' + str(i+1))
        print_grid(grid)
        
        print()

    return grid
















'''
x = 10
y = 10

grid = create_grid(x, y)

# Randomly put some infected people on the grid
for i in range(x):
    random_x = random.randint(0, x-1)
    random_y = random.randint(0, y-1)
    grid[random_y+1][random_x+1] = 'x'

infection_simulation(grid, 100, 1, 1)
'''
