


nums_of_colors = {'red' : 6, 'blue' : 5, 'yellow' : 7, 'orange' : 7,
          'purple' : 4, 'green' : 6}




user_input = input('What colors would you like to eat? ')

while user_input != 'quit':
    input_colors = user_input.split() 
    sum_loops = 0

    for color in input_colors:
        sum_loops += nums_of_colors[color]

    print()
    print('There are ' + str(sum_loops) + ' fruit loops with those colors.')
    print()
    
    user_input = input('What colors would you like to eat? ')

print()
print('Thanks for checking the cereal inventory!')
