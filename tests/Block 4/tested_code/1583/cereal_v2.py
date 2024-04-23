


nums_of_colors = {'red' : 6, 'blue' : 5, 'yellow' : 7, 'orange' : 7,
          'purple' : 4, 'green' : 6}




user_input = input('What would you like to do? ')

while user_input != 'quit':
    inputs = user_input.split() 

    if 'floor' in inputs: 
        if inputs[1] not in nums_of_colors:
            nums_of_colors[inputs[1]] = 1
        else:
            nums_of_colors[inputs[1]] += 1

        print()
        print('Yum! A fruit loop on the floor!')
        print()
        
    else: 
        sum_loops = 0

        for color in inputs:
            sum_loops += nums_of_colors[color]

        print()
        print('There are ' + str(sum_loops) + ' fruit loops with those colors.')
        print()
        
    user_input = input('What would you like to do? ')

print()
print('Thanks for checking the cereal inventory!')
