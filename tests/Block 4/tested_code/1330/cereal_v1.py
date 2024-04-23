






fruit_loops = {'red':6, 'blue':5, 'yellow':7,
               'orange':7, 'purple':4, 'green':6}

'''
colors = input('What colors do you want for fruits: ')
Sum = 0

for color in fruit_loops:
    #print(color)
    if color in colors:
        Sum += fruit_loops[color]
if Sum != 0:
    print('There are ' + str(Sum) + ' fruit loops with those colors')
else:
    print('You input wrong colors!')
'''



attitude = 'yes'

while not False:
    colors = input('What colors do you want for fruits: ')
    Sum = 0
    if 'quit' not in colors:
        for color in fruit_loops:
            
            if color in colors:
                Sum += fruit_loops[color]
        print('There are ' + str(Sum) + ' fruit loops with those colors') 
    else:
        print('STOP')
        break
        
        
