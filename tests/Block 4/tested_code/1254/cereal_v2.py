


bowl = {'red':6, 'blue':5, 'yellow':7, 'orange': 7, 'purple':4, 'green':6}

total = 0

user_input = input("What colors would you like? ")
splitted_input = user_input.split()

while splitted_input[0] == 'floor' or splitted_input[0] in bowl:

    if splitted_input[0] == 'floor':
        if splitted_input[1] in bowl:
            bowl[splitted_input[1]] = bowl[splitted_input[1]] + 1
        else:
            bowl[splitted_input[1]] = 1
        print(bowl)
    else:
        for color in splitted_input:
            total += bowl[color]
        print('There are ' + str(total) + ' fruit loops with those colors.')
        
    user_input = input("What colors would you like? ")
    splitted_input = user_input.split()  
        

