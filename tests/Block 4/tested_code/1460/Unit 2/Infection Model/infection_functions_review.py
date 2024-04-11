


from random import random






def determine_if_infected(infection_probability, num_neighbors_infected):
    return random() < infection_probability * num_neighbors_infected





def determine_if_still_infected(heal_probability):
    
    return random() > heal_probability 






def check_neighbors(grid, x, y):
    infected_neighbors = 0
    if y + 1 < len(grid) and grid[y + 1][x]:
        infected_neighbors += 1
    if y - 1 >= 0 and grid[y - 1][x]:
        infected_neighbors += 1
    if x + 1 < len(grid[0]) and grid[y][x + 1]:
        infected_neighbors += 1
    if x - 1 >= 0 and grid[y][x - 1]:
        infected_neighbors += 1
    return infected_neighbors



def is_everyone_healed(grid):
    everyone_healed = True
    for row in grid:
        for square in row: 
            if square: 
                everyone_healed = False
    return everyone_healed



def is_everyone_infected(grid):
    everyone_infected = True
    for row in grid:
        for square in row:
            if not square: 
                everyone_infected = False
    return everyone_infected


def print_grid(grid):
    rows = len(grid)
    columns = len(grid[0])
    grid_to_print = []
    for y in range(rows):
        row_to_print = []
        for x in range(columns):
            if grid[y][x]: 
                row_to_print.append('💀') 
            else: 
                row_to_print.append('😐')
        grid_to_print.append(' '.join(row_to_print))
    print('\n'.join(grid_to_print))
        
