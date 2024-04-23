



import random


def initialize_grid( num_rows, num_cols, infected_chance=0.1):
    """Initialize the grid with healthy and infected individuals."""
    grid = []  
    total_cells = size * size
    infected_count = int(total_cells * infected_chance)  

    
    for i in range(num_rows): 
        row = []
        for j in range(num_cols):
            if infected_count > 0 and random.choice([True, False]):
                row.append('x')  
                infected_count -= 1
            else:
                row.append('·')  
        grid.append(row)

    return grid





def count_infected_neighbors(grid, row, col):
    """Count the number of infected neighbors for a given cell."""
    infected_count = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(max(0, row-1), min(rows, row+2)):
        for c in range(max(0, col-1), min(cols, col+2)):
            if (r != row and c != col) and grid[r][c] == 'x':
                infected_count += 1
    return infected_count

def update_health_status(grid, heal_probability, infection_probability, cycle_length=10):
    """Update the health status of each individual based on their neighbors, without using random.random()."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    new_grid = [['·' for i in range(cols)] for j in range(rows)]  
    heal_cycle_threshold = int(cycle_length * heal_probability)
    infection_cycle_threshold = int(cycle_length * infection_probability)

    cycle_counter = 0  

    for row in range(rows):
        for col in range(cols):
            cycle_counter = (cycle_counter + 1) % cycle_length  
            if grid[row][col] == 'x':
                
                if cycle_counter < heal_cycle_threshold:
                    new_grid[row][col] = '·'
                else:
                    new_grid[row][col] = 'x'
            else:
                
                infected_neighbors = count_infected_neighbors(grid, row, col)
                if cycle_counter < infection_cycle_threshold * infected_neighbors:
                    new_grid[row][col] = 'x'

    return new_grid


