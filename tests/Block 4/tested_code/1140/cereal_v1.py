


fruit_loops = {'red':6, 'blue':5, 'yellow':7, 'orange':7, 'purple':4, 'green':6}




response = input('What colors of fruit loops would you like to count? '
                 'Type "quit" when you\'re done with your questions: ')

while response != 'quit':
    colors = response.split()
    num_fruit_loops = 0
    # Cycles through every input color
    for i in range(len(colors)):
        # Finds the sum of the input colors
        num_fruit_loops = num_fruit_loops + fruit_loops[colors[i]]
    print('There are ' + str(num_fruit_loops)
              + ' fruit loops with these colors.')
    response = input('What colors of fruit loops would you like to count? '
              'Type "quit" when you\'re done with your questions: ')

    
