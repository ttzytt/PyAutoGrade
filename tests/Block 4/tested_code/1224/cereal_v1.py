


total = 0
cont_loop = ''
while cont_loop != 'quit':
    bowl_o_loops = {'red' : 6, 'blue' : 5, 'yellow': 7, 'orange' : 7, 'purple' : 4, 'green' : 6}

    colors = input('Which colors of fruit loops? ')
    colors = colors.split()

    for color in colors:
        total += bowl_o_loops[color]
    print('There are ' + str(total) + ' Fruit loops with that color')
    cont_loop = input('Enter quit to stop')
    total = 0

                
