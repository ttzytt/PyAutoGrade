




fruit_loops = {'red' : 6, 'blue' : 5, 'yellow' : 7, 'orange' : 7, 'purple' : 4, 'green' : 6}

answer = input('What color of the fruit do you like?'
                 + ' (example response: red orange yellow) ')

while answer != 'quit':
    new_colors = answer.split()
    if new_colors[0] == 'floor':
        new_colors[1]
    colors = answer.split()
    count = 0
    for color in colors:
        count = count + fruit_loops[color]

    print (count)
    
    answer = input('What color of the fruit do you like?'
                 + ' (example response: red orange yellow) ')
