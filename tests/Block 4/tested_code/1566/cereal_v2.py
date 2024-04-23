




'''
When entering 'floor red' it will first show 0. You will have to input 'red' to see that red has
updated.

'''

cereal = {'red':6, 'blue':5, 'yellow':7, 'orange':7, 'purple':4, 'green':6}

run = True
while run == True:
    player_input = input('Please enter some colors with spaces in between or quit to exit the program: ')
    if player_input == 'quit':
        print('bye')
        run = False
    else:
        colors = player_input.split()
        cereal_count = 0
        i = 0 
        while i < len(colors):
            
            color = colors[i]
            if color == 'floor':
                i += 1
                if i < len(colors):
                    new_color = colors[i]
                    if new_color in cereal:
                        cereal[new_color] += 1     
                    else:
                        cereal[new_color] = 1
            
            elif color in cereal:
                cereal_count += cereal[color]
            
            else:
                cereal[color] = 1
                cereal_count += 1
            i += 1
        print('There are ' + str(cereal_count) + ' fruit loops with those colors')





