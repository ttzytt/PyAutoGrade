




def rabbit_sheep_simulation(model, rabbits, sheep, cycles=50,):
    populations = []
    
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






print(rabbit_sheep_simulation(2, 2.5, 1, 100))
