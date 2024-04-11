


from infection_function

def test_initialize_grid():
    size = 5
    grid = initialize_grid(size)
    correct_size = True
    for row in grid:
        if len(row) != size:
            correct_size = False
            break
    if len(grid) == size and correct_size:
        print("test_initialize_grid Passed")
    else:
        print("test_initialize_grid Failed")

def test_count_infected_neighbors():
    grid = [
        ['·', 'x', '·'],
        ['·', 'x', '·'],
        ['·', '·', '·']
    ]
    expected = 1
    result = count_infected_neighbors(grid, 0, 0)
    if result == expected:
        print("test_count_infected_neighbors Passed")
    else:
        print("test_count_infected_neighbors Failed: Expected " + str(expected) + ", got " + str(result))

        
def test_update_health_status():
    
    grid = [
        ['x', '·', '·'],
        ['·', '·', '·'],
        ['·', '·', '·']
    ]
    heal_probability = 1.0  
    infection_probability = 0.0  
    updated_grid = update_health_status(grid, heal_probability, infection_probability)
    correct_update = True
    if updated_grid[0][0] != '·':  
        correct_update = False
    for row in updated_grid:
        for cell in row:
            if cell != '·':  
                correct_update = False
                break
        if not correct_update:
            break
    if correct_update:
        print("test_update_health_status Passed")
    else:
        print("test_update_health_status Failed")

test_initialize_grid()
test_count_infected_neighbors()
test_update_health_status()
