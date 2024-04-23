


from infection_functions import *



infection_probability = 0.4
heal_probability = 0.5

grid_rows = 10
grid_columns = 10

max_turns = 10000
print_turn_interval = 10

squares_to_be_inserted = [[0,0],[9,0],[0,9],[9,9]]


is_infected_grid = []
for _ in range(grid_rows):
    row = []
    for _ in range(grid_columns):
        row.append(False)
    is_infected_grid.append(row)



for square in squares_to_be_inserted:
    grid_column = square[0]
    grid_row = square[1]
    is_infected_grid[grid_row][grid_column] = True

print_grid(is_infected_grid)
print("This is the starting map. Press ENTER to continue")
input()

turn = 1
was_prompted_to_quit = False
while turn < max_turns and (not is_everyone_healed(is_infected_grid)):
    if (turn % print_turn_interval == 0):
        print("Turn",turn,":")
        print_grid(is_infected_grid)
    new_grid = []
    for row in range(grid_rows):
        new_row = []
        for column in range(grid_columns):
            if is_infected_grid[row][column]: 
                
                new_row.append(determine_if_still_infected(heal_probability))
            else: 
                new_row.append(determine_if_infected(infection_probability,
                                                      check_neighbors(is_infected_grid, column, row)))
        new_grid.append(new_row)
    is_infected_grid = new_grid

    
    if is_everyone_infected(is_infected_grid):
        if not was_prompted_to_quit:
            was_prompted_to_quit = True
            if turn % print_turn_interval != 0:
                print(f"Turn {turn}:")
                print_grid(is_infected_grid)
            print(f"Everyone is infected (Turn {turn}). Would you like to continue?")
            user_input = input("Press ENTER to continue. Type anything to quit. ")
            if user_input != '':
                turn = max_turns
    else:
        was_prompted_to_quit = False
    
    turn += 1
if turn == max_turns + 1: 
    turn = '^^^'
print(f"Final State ({turn} turns): ")
print_grid(is_infected_grid)



'''
Are individuals in different locations (corners, edges, closer or further from the center,
...) sick more often? By how much?

Individuals are generally more sick in the middle than at the corners or edges, since people
can have up to 4 neighbors in the middle, 3 neighbors at the edges, and 2 neighbors in the
corners. As such, less max neighbors = less max infected neighbors

This does depend on the starting grid of the board, but after a few turns, this pattern
should show true.
'''
