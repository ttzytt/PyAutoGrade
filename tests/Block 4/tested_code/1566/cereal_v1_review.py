




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
        for color in colors:
            if color in cereal:
                cereal_count += cereal[color]     
        print('There are ' + str(cereal_count) + ' fruit loops with those colors')
