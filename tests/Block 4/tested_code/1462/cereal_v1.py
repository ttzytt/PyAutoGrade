



cereals = {'red': 6, 'blue': 5, 'yellow': 7, 'orange': 7, 'purple': 4, 'green': 6}

colors = (input('Enter combinations of colors ("quit" if you want to stop): ')).split()

while colors != ['quit']:
    total = 0

    for color in colors:
        total += cereals[color]

    print('There are ' + str(total) + ' fruit loops with those colors.')
    print()

    colors =(input('Enter combinations of colors ("quit" if you want to stop): ')).split()
