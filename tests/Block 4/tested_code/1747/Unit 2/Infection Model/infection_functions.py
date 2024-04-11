



import random
random.seed()


'''Some function related to giving the row and row number'''



def draw_row(row, row_number):
    print(str(row_number) + ' │ '
          + row[0] + ' │ '
          + row[1] + ' │ '
          + row[2] + ' │ '
          + row[3] + ' │ '
          + row[4] + ' │ '
          + row[5] + ' │ '
          + row[6] + ' │ '
          + row[7] + ' │ '
          + row[8] + ' │ '
          + row[9] + ' │ ')



def draw_grid(grid):
    print('  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ')
    draw_row(grid[0], 1)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[1], 2)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[2], 3)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[3], 4)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[4], 5)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[5], 6)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[6], 7)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[7], 8)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[8], 9)
    print('  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[9], 10)
    print('  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')
    print('    A   B   C   D   E   F   G   H   I   J   ')


'''By this point, infection_probablity, heal probability, x· symbols should be given/known.'''



def cell_infection_probability(infection_probability):

    num_infected_neighbors = 0

    
    for i in range(1,9):
        for j in range(1,9):
            if grid[i-1][j] == 'x':
                num_infected_neighbors += 1
            elif grid[i][j-1] == 'x':
                num_infected_neighbors += 1
            elif grid[i][j+1] == 'x':
                num_infected_neighbors += 1
            elif grid[i+1][j] == 'x':
                num_infected_neighbors += 1

    
    for i = 0:
        for j in range(1,9):
            if grid[i][j-1] == 'x':
                num_infected_neighbors += 1
            elif grid[i][j+1] == 'x':
                num_infected_neighbors += 1
            elif grid[i+1][j] == 'x':
                num_infected_neighbors += 1
    for i = 9:
        for j in range(1,9):
            if grid[i-1][j] == 'x':
                num_infected_neighbors += 1
            elif grid[i][j-1] == 'x':
                num_infected_neighbors += 1
            elif grid[i][j+1] == 'x':
                num_infected_neighbors += 1

    
    for i = 0:
        for j = 0:
            if grid[i][j+1] == 'x':
                num_infected_neighbors += 1
            elif grid[i+1][j] == 'x':
                num_infected_neighbors += 1
    for i = 0:
        for j = 9:
            if grid[i][j-1] == 'x':
                num_infected_neighbors += 1
            elif grid[i+1][j] == 'x':
                num_infected_neighbors += 1
    for i = 9:
        for j = 0:
            if grid[i-1][j] == 'x':
                num_infected_neighbors += 1
            elif grid[i][j+1] == 'x':
                num_infected_neighbors += 1
    for i = 9:
        for j = 9:
            if grid[i-1][j] == 'x':
                num_infected_neighbors += 1
            elif grid[i][j-1] == 'x':
                num_infected_neighbors += 1

    return (infection_probability * num_infected_neighbors)
    


def updated_infection_grid():
    







































