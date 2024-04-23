


bowl = {'red':6, 'blue':5, 'yellow':7, 'orange': 7, 'purple':4, 'green':6}

colors_chosen = input("What colors would you like? ")
list_of_colors_chosen = colors_chosen.split()
total = 0

for color in list_of_colors_chosen:
    total += bowl[color]

print('There are ' + str(total) + ' fruit loops with those colors.')
