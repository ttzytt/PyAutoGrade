


import random
random.seed()








                                                
                                                
                                                
                                                
def create_grid(columns, rows):
    grid = []
    
    for y in range(rows+2): 
        row = ['·']*(columns+2)
        grid.append(row)
    return grid




def print_grid(grid):
    for y in range(len(grid)):
        row = ''
        for x in range(len(grid[0])):
            row += grid[y][x]
            row += '    '
        print(row)
        print()









def count_infected_neighbors(person_x, person_y, grid):
    
    
    person_x += 1
    person_y += 1
    count = 0
    if grid[person_y - 1][person_x] == 'x':
        count += 1
    if grid[person_y][person_x + 1] == 'x':
        count += 1
    if grid[person_y + 1][person_x] == 'x':
        count += 1
    if grid[person_y][person_x - 1] == 'x':
        count += 1

    return count













def heal_infected(heal_probability, infected_x, infected_y, grid,
                  grid_to_modify):
    infected_x += 1
    infected_y += 1

    if_heal = random.random()
    if if_heal <= heal_probability:
        grid_to_modify[infected_y][infected_x] = '·'
















def infect_healthy(infect_probability, healthy_x, healthy_y, grid,
                   grid_to_modify):
    num_infected_neighbors = count_infected_neighbors(healthy_x, healthy_y,
                                                      grid)
    healthy_x += 1
    healthy_y += 1
    
    if random.random() <= infect_probability * num_infected_neighbors:
        grid_to_modify[healthy_y][healthy_x] = 'x'


