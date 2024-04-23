


'''
Program returns total number of fruit loops depending
on input color(s) (Ex. 'red blue orange' returns 18)
Any color fruit loops can be added to the dictionary
including existing colors by typing "floor" before a color"
'''

fruit_loops = {'red':6, 'blue':5, 'yellow':7, 'orange':7, 'purple':4, 'green':6}

response = input('What fruit loop colors would you like to count? '
                 'You can also type "floor" before a color '
                 'to add a fruit loop, or a new color! '
                 'Type "quit" when you\'re done: ')

while response != 'quit':
    words_input = response.split()
    num_fruit_loops = 0
    
    if words_input[0] == 'floor': # If the first word is floor
        if words_input[1] in fruit_loops: # If the 2nd word is an existing color
            fruit_loops[words_input[1]] += 1
        else: # If the 2nd word is a new color
            fruit_loops[str(words_input[1])] = 1
    else:
        # Cycles through every input color
        for i in range(len(words_input)):
            num_fruit_loops = num_fruit_loops + fruit_loops[words_input[i]]
        print('There are ' + str(num_fruit_loops)
              + ' fruit loops with these colors.')

    response = input('What colors of fruit loops would you like to count? '
                     'Type "quit" when you\'re done with your questions: ')

    
