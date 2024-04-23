


fruit_loop = {'red' : 6, 'blue' : 5, 'yellow' : 7, 'orange' : 7, 'purple' : 4, 'green' : 6}

user_input = input('What color combination would you like'
                ' example response: red orange yellow), or enter quit: ')

while user_input.lower() != 'quit':
    
    keys = user_input.lower().split()

    total = 0
    for key in keys:
        total = total + fruit_loop[key]

    print('The total amount of fruit loops is ' + str(total))
    print()

    
    user_input = input('What color combination would you like'
                   ' example response: red orange yellow), or enter quit: ')








