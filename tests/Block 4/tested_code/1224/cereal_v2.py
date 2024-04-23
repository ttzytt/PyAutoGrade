


total = 0
cont_loop = ''
bowl_o_loops = {'red' : 6, 'blue' : 5, 'yellow': 7, 'orange' : 7, 'purple' : 4, 'green' : 6}

while True:
    colors = input('Which colors of fruit loops? (type quit to quit) ')
    colors = colors.split()
    
    if colors[0] == 'floor':
        
        if colors[1] not in bowl_o_loops:
            bowl_o_loops[colors[1]] = 1 
        else:
            bowl_o_loops[colors[1]] += 1
            
    elif colors[0] == 'quit':
        
        break
    
    else:
        for color in colors:
            total += bowl_o_loops[color]
        
        print('There are ' + str(total) + ' Fruit loops with that color')
    total = 0

                
