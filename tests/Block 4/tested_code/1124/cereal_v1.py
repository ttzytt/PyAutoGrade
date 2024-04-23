



bowl = {'red' : 6, 'blue' : 5, 'yellow' : 7, 'orange': 7, 'purple' : 4, 'green' : 6}


total_amount = 0


inputted_colors = input('Which colors do you want?')


colors = inputted_colors.split()


for color in colors:
    total_amount += bowl[color]

print('There are ' + str(total_amount) + ' fruit loops with these colors.')
