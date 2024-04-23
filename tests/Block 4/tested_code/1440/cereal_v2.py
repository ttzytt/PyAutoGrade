




cafe = {'red':6,'yellow':7,'purple':4,'green':6}

def counting_fruitloop_floor():
    colors = input('what color of cereals do u wanna count?').split()
    sums = 0
    if colors[0] == 'floor':
        for i in range(1,len(colors)):
            if colors[i] in cafe:
                cafe[colors[i]] = cafe[colors[i]] + 1
            else:
                cafe[colors[i]] = 1
    else:
        for color in colors:
            sums += cafe[color]
        print('the sum for these cereals are:' + str(sums))
    return cafe

user_quit = input('do u wanna quit? Enter "yes" or "no"')

while user_quit != 'yes':
    cafe = counting_fruitloop_floor()
    user_quit = input('do u wanna quit? Enter "y" for yes')
