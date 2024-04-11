



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
    
    print('   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐ ')
    draw_row(grid[0], ' 1')
    print('   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[1], ' 2')
    print('   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[2], ' 3')
    print('   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[3], ' 4')
    print('   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[4], ' 5')
    print('   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[5], ' 6')
    print('   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[6], ' 7')
    print('   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[7], ' 8')
    print('   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[8], ' 9')
    print('   ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤ ')
    draw_row(grid[9], '10')
    print('   └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘ ')
    print('     A   B   C   D   E   F   G   H   I   J')



def update_1_round(grid, infection_probability, heal_probability):

    

    






for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == ' ':
            infected_neighbours = 0
            if grid[i - 1][j] == 'x':
                infected_neighbours += 1
            if grid[i + 1][j] == 'x':
                infected_neighbours += 1
            if grid[i][j - 1] == 'x':
                infected_neighbours += 1
            if grid[i][j + 1] == 'x':
                infected_neighbours += 1

            grid[i][j] = infected_neighbours

            

            
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'x':
            if random.random() < 0.1:
                grid[i][j] == ' '                

        if grid[i][j] != 'x':
            if random.random() < 0.1 * gird[i][j]:
                gird[i][j] == 'x'
            else: 
                grid[i][j] == ' '
        
            
    





draw_grid(grid)











