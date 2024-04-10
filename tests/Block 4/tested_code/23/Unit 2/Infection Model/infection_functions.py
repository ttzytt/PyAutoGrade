





import random


def initialize_grid():
    grid_size = int(input('How many rows/columns will the grid have? '))
    
    grid = []

    grid.append([])
    for col in range(grid_size + 2):
        
        grid[0].append('·')

            
    for row in range(1, grid_size + 1):
        grid.append([]) 
        grid[row].append('·')
        for col in range(grid_size):
            
            grid[row].append(random.choice(['x', '·']))
        grid[row].append('·')


    grid.append([])
    for col in range(grid_size + 2):
        
        grid[-1].append('·')


    print('Generating random grid: ')
    print_grid(grid)
    return grid


def print_grid(grid):
 for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        print(grid[row][col], end = ' ') 
    print()
    


def get_num_infected_neighbors(grid, row, col):
    num_infected_neighbors = 0

    
    
    if grid[row - 1][col] == "x": 
       num_infected_neighbors += 1
    if grid[row + 1][col] == "x": 
        num_infected_neighbors += 1
    if grid[row][col + 1] == "x": 
        num_infected_neighbors += 1
    if grid[row][col - 1] == "x": 
        num_infected_neighbors += 1

    return num_infected_neighbors
               
    
  
  
  
  
  
  
  
  
  
  

  
  
  
  
  
  
  
  
  
  

def simulate_round(grid, infection_probability, heal_probability):
    
    
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            
            if grid[row][col] == '·':
                num_infected_neighbors = get_num_infected_neighbors(grid, row, col)
                if (num_infected_neighbors > 0 and
        random.random() < infection_probability * num_infected_neighbors):
                    grid[row][col] = '@'
                       
    
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            
            if grid[row][col] == 'x' and random.random() < heal_probability:
                grid[row][col] = '·'
    
    
    
    
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == '@':
                grid[row][col] = 'x'



def is_grid_mixed(grid):
  for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        
        if grid[row][col] != grid[0][0]:
            return True
    return False

