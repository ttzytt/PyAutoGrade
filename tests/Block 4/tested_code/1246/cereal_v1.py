


fruit_loop_bowl = {'red' : 6, 'yellow' : 7, 'blue' : 5, 'orange' : 7, 'purple' : 4, 'green' : 6}

in_game = True

while in_game:
    color_list = input("which colors: ").split()

    if color_list[0] == ['quit']:
        in_game = False
        continue

    if color_list[0] not in fruit_loop_bowl:
        while True:
            print('pls learn how to type')

    total = 0

    for i in range(len(color_list)):

        total += fruit_loop_bowl[color_list[i]]

    print('There are ' + str(total) + ' fruit loops with those colors.')
