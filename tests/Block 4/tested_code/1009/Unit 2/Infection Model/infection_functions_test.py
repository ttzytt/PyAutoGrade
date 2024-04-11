


from infection_functions import *
import random






def TEST(condition, test_name="Test Case"):
    if condition:
        print(f"{test_name} Passed")
    else:
        print(f"{test_name} Failed")




def approx_equal(a, b):
    return abs(a - b) < 0.0001



def test_create_original_grid():
    
    grid_size = 5
    initial_infected = 3
    original_grid = create_original_grid(grid_size, initial_infected)
    if len(original_grid) == grid_size:
        print("create_original_grid test 1: PASS")
    else:
        print("create_original_grid test 1: FAIL")

    
    grid_size = 10
    initial_infected = 8
    original_grid = create_original_grid(grid_size, initial_infected)
    if len(original_grid) == grid_size:
        print("create_original_grid test 2: PASS")
    else:
        print("create_original_grid test 2: FAIL")

def test_update_new_grid():
    
    grid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    infection_probability = 0.3
    heal_probability = 0.4

    new_grid = update_new_grid(grid, infection_probability, heal_probability)
    
    if len(new_grid) == len(grid):
        print("update_new_grid test: PASS")
    else:
        print("update_new_grid test: FAIL")

def test_show_the_grid():
    
    sample_grid = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    
    print("Test 1: show_the_grid:")
    print("Expected Output:")
    print("X . X ")
    print(". X . ")
    print("X . X ")
    print("Actual Output:")
    show_the_grid(sample_grid)

    
    sample_grid = [[0, 0, 1], [1, 1, 0], [0, 1, 1]]
    
    print("Test 2: show_the_grid:")
    print("Expected Output:")
    print(". . X ")
    print("X X . ")
    print(". X X ")
    print("Actual Output:")
    show_the_grid(sample_grid)

test_create_original_grid()
test_update_new_grid()
test_show_the_grid()

