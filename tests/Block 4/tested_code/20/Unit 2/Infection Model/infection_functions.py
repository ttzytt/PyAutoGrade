



import random

def create_original_grid(grid_size, initial_infected):
    grid = [] 
    for _ in range(grid_size):
        row = [] 
        for _ in range(grid_size):
            row.append(0) 
        grid.append(row) 

    for _ in range(initial_infected):
        
        row_get_infected = random.randint(0, grid_size - 1)
        
        col_get_infected = random.randint(0, grid_size - 1)
        
        grid[row_get_infected][col_get_infected] = 1

    return grid 


def update_new_grid(grid, infection_probability, heal_probability):
    new_grid = [] 
    grid_size = len(grid)
    for row in grid:
        new_row = [] 
        for col in range(grid_size):
            cell = grid[row][col]  

        for cell in row:
            if cell == 1: 
                if random.random() < heal_probability: 
                    new_row.append(0)

                else:
                    new_row.append(1)

            elif cell == 0: 
                
                if random.random() < infection_probability:
                    new_row.append(1) 
                
                else:
                    new_row.append(0) 

        new_grid.append(new_row) 
    return new_grid 

def show_the_grid(new_grid): 
    for row in new_grid:
        for cell in row:
            if cell == 1:
                print ("X", end = " ") 
            elif cell == 0:
                print (".", end = " ") 
        print()

def run_how_many_times(grid_size, num_simulations):
    for _ in range(num_simulations):
        
        original_grid = random.randint(1, grid_size * grid_size)

        print("Original Grid: ")
        show_the_grid(original_grid) 

        new_grid = original_grid[:] 
        for _ in range(20): 
            
            new_grid = update_new_grid(grid, infection_probability, heal_porbability)
        print("Update New Grid: ")
        show_the_grid(new_grid) 
        print()
        
