






cereals = {'red':6, 'orange':7, 'yellow':7, 'green':6, 'blue':5, 'purple':4}
answer = input('what color fruit loop would you like? ')


while answer != 'quit': 
    num_of_cereals = 0
    colors = answer.split() 
    for i in range(len(colors)):
        num_of_cereals = num_of_cereals + cereals[colors[i]] 
    print('there are ' + str(num_of_cereals) + ' with those colors.') 
    answer = input('what color fruit loop would you like? ')
