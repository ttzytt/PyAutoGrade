



cereals = {'red': 6, 'blue': 5, 'yellow': 7, 'orange': 7, 'purple': 4, 'green': 6}

colors = (input('Enter combinations of colors or a bonus loop ("quit" if stop): ')).split()

while colors != ['quit']:
    total = 0

    if colors[0] == 'floor':
        if colors[1] in cereals:
            cereals[colors[1]] += 1
            print('You added a fruit loop!')
        else:
            cereals[colors[1]] = 1
            print('You added a new color!')

    else:
        for color in colors:
            total += cereals[color]
        print('There are ' + str(total) + ' fruit loops with those colors.')

    print()

    colors = (input('Enter combinations of colors or a bonus loop ("quit" if stop): ')).split()
