




def rabbit_sheep_simulation(model, rabbits, sheep, cycles=50,):
    populations = []
    '''
    print('Starting conditions:')
    print('Rabbits: ' + str(rabbits))
    print('Sheep: ' + str(sheep))
    print()
    '''
    populations.append((rabbits, sheep))
    
    for i in range(cycles):
        if model == 1:
            new_rabbits = (rabbits + 0.1 * (3 - rabbits) * rabbits
                           - 0.2 * rabbits * sheep)
            new_sheep = (sheep + 0.1 * (2 - sheep) * sheep - 0.1
                         * rabbits * sheep)
        else:
            new_rabbits = (rabbits + 0.1 * (3 - rabbits) * rabbits - 0.2
                           * rabbits * sheep)
            new_sheep = (sheep + 0.1 * (1 - sheep) * sheep - 0.02
                         * rabbits * sheep)

        if new_rabbits < 0 :
            new_rabbits = 0
        if new_sheep < 0:
            new_sheep = 0

        rabbits = new_rabbits
        sheep = new_sheep

        populations.append((rabbits, sheep))

        '''
        print('Cycle ' + str(i+1))
        print('Rabbits: ' + str(round(rabbits, 2)))
        print('Sheep: ' + str(round(sheep, 2)))
        print()
        '''
    return populations

def coordinates_close(coords1, coords2):
    return (coords2[0] >= coords1[0] - 0.05 and coords2[1] >= coords1[1] - 0.05
            and coords2[0] <= coords1[0] + 0.05 and coords2[1] <= coords1[1] + 0.05)

def find_sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

def find_turning_point(populations):
    pre_slope = None
    for i in range(0, len(populations) - 1):
        delta_y = populations[i+1][1] - populations[i][1]
        delta_x = populations[i+1][0] - populations[i][0]

        if delta_x == 0:
            slope = 0
        else:
            slope = delta_y / delta_x



        if pre_slope != None:
            if find_sign(pre_slope) != find_sign(slope):

                return populations[i]

        pre_slope = slope

'''
starting_values = []
turning_points = []
i = 1
j = 1
while i <= 12:
    while j <= 12:
        turning_points.append(find_turning_point(rabbit_sheep_simulation(2, i, j, 50)))
        starting_values.append((i, j))
        
        j += 0.5
    i += 0.5
    j = 1
        

print(turning_points)

margin = 0.04
black_points = []
red_points = []
black_starting_values = []
red_starting_values = []
for i in range(1, len(turning_points)):
    x = turning_points[i][0]
    y = turning_points[i][1]
    if y <= -x + 2 + margin and y >= -x + 2 - margin: # black line
        if turning_points[i] == (1.6789380841080364, 0.32516495573852666):
            print(starting_values[i])
        black_points.append(turning_points[i]) 
        black_starting_values.append(starting_values[i])
        
    if y <= -(x/2) + 1.5 + margin and y >= -(x/2) + 1.5 - margin: # red line
        red_points.append(turning_points[i])
        red_starting_values.append(starting_values[i])
        
print(black_starting_values)
print(red_starting_values)
'''


'''
sheep_wins = []
rabbit_wins = []

i = 1
j = 1
while i < 12:
    while j < 12:
        if coordinates_close(rabbit_sheep_simulation(1, i, j, 300)[-1], (3, 0)):
            rabbit_wins.append((i, j))
        else:
            sheep_wins.append((i, j))
        
        j += 0.5
    i += 0.5
    j = 1

print(rabbit_wins)
print(sheep_wins)
'''

print(rabbit_sheep_simulation(2, 2.5, 1, 100))
