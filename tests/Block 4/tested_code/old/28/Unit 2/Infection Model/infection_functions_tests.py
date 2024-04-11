





from infection_functions import *
from infection_simulation import *







def TEST(has_passed):
    if has_passed:
        print('pass')
    else:
        print('FAIL')






def count_infected_neighbors_TEST():
    print('Start count_infected_neighbors_TEST')
    

    
    grid = create_grid(10, 10)
    TEST(count_infected_neighbors(5, 5, grid) == 0)
    
    
    grid = create_grid(10, 10)
    grid[5][6] = 'x'
    TEST(count_infected_neighbors(5, 5, grid) == 1)

    
    grid = create_grid(10, 10)
    grid[7][6] = 'x'
    grid[6][7] = 'x'
    TEST(count_infected_neighbors(5, 5, grid) == 2)

    
    grid = create_grid(10, 10)
    grid[5][6] = 'x'
    grid[7][6] = 'x'
    grid[6][7] = 'x'
    TEST(count_infected_neighbors(5, 5, grid) == 3)

    
    grid = create_grid(10, 10)
    grid[5][6] = 'x'
    grid[7][6] = 'x'
    grid[6][7] = 'x'
    grid[6][5] = 'x'
    TEST(count_infected_neighbors(5, 5, grid) == 4)

    
    grid = create_grid(10, 10)
    grid[5][5] = 'x'
    TEST(count_infected_neighbors(5, 5, grid) == 0)

    
    grid = create_grid(10, 10)
    grid[5][5] = 'x'
    grid[5][7] = 'x'
    grid[3][2] = 'x'
    grid[8][7] = 'x'
    grid[1][9] = 'x'
    grid[9][8] = 'x'
    grid[4][5] = 'x'
    grid[6][7] = 'x'
    TEST(count_infected_neighbors(5, 5, grid) == 1)

    
    grid = create_grid(10, 10)
    grid[2][5] = 'x'
    grid[1][6] = 'x'
    TEST(count_infected_neighbors(4, 0, grid) == 2)

    
    grid = create_grid(10, 10)
    grid[1][2] = 'x'
    grid[2][1] = 'x'
    TEST(count_infected_neighbors(0, 0, grid) == 2)

    print('End count_infected_neighbors_TEST')


def infection_simulation_TEST():
    print('Start infection_simulation_TEST')
    

    x = 5
    y = 5
    grid = create_grid(x, y)
    
    grid[1][1] = 'x'
    grid[2][1] = 'x'
    grid[5][1] = 'x'
    grid[4][5] = 'x'
    grid[2][4] = 'x'
    
    expected_grid = create_grid(x, y)

    expected_grid[1][2] = 'x'
    expected_grid[1][4] = 'x'
    expected_grid[2][2] = 'x'
    expected_grid[2][3] = 'x'
    expected_grid[2][5] = 'x'
    expected_grid[3][1] = 'x'
    expected_grid[3][4] = 'x'
    expected_grid[3][5] = 'x'
    expected_grid[4][1] = 'x'
    expected_grid[4][4] = 'x'
    expected_grid[5][2] = 'x'
    expected_grid[5][5] = 'x'

    grid = infection_simulation(grid, 1, 1, 1)

    TEST(grid == expected_grid)
    
    print('End infection_simulation_TEST')


count_infected_neighbors_TEST()
print()
infection_simulation_TEST()
