


fruit_loop_bowl = {'red' : 6, 'yellow' : 7, 'blue' : 5, 'orange' : 7, 'purple' : 4, 'green' : 6}

in_game = True

while in_game:
    color_list = input("which colors: ").split()

    if color_list[0] == ['quit']:
        in_game = False

    elif len(color_list) == 0:
        for i in range(50):
            print('pls learn how to type')

    elif color_list[0] == 'floor':
        if len(color_list) != 2:
            print("pls inpyut correctly ")
            
        elif color_list[1] in fruit_loop_bowl:
            fruit_loop_bowl[color_list[1]] += 1

        else:
            fruit_loop_bowl[color_list[1]] = 1

    elif color_list[0] not in fruit_loop_bowl:
        print("pls inpyut corectly")
            
    else:
        total = 0

        for i in range(len(color_list)):

            total += fruit_loop_bowl[color_list[i]]
    

        print('There are ' + str(total) + ' fruit loops with those colors.')
