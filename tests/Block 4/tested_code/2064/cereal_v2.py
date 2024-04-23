





cereal = { 'red' : 6, 'blue' : 5, 'yellow' : 7, 'orange' : 7, 'purple' : 4,
           'green' : 6}

user_colors = input('Enter some colors: ')
cereal_sum = 0

while (user_colors != 'quit'):
    colors = user_colors.split()
    if(colors[0] == 'floor'):
        if colors[1] in cereal:
            cereal[colors[1]] = cereal[colors[1]] + 1
        else:
            cereal[colors[1]] = 1
    else:
        for color in colors:
            cereal_sum += cereal[color]
        print('There are ' + str(cereal_sum) + ' fruit loops with those colors.')
    user_colors = input('Enter some colors: ')
    cereal_sum = 0
        


