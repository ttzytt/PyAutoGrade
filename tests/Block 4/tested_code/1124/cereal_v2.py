



bowl = {'red' : 6, 'blue' : 5, 'yellow' : 7, 'orange': 7, 'purple' : 4, 'green' : 6}


inputted_colors = input('Which colors do you want to check or add?')

while inputted_colors != 'stop':
    
    total_amount = 0

    
    colors = inputted_colors.split()

    
    
    if colors[0] == 'floor':
        if colors[1] in bowl:
            bowl[colors[1]] += 1
        else:
            bowl[colors[1]] = 1
    else:
        
        for color in colors:
            total_amount += bowl[color]
        print('There are ' + str(total_amount) + ' fruit loops with these colors.')
    
    inputted_colors = input('Which colors do you want to check or add?')
    print(bowl)
    
