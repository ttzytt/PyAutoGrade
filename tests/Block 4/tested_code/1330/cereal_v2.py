






print('Task 20 begins:')

fruit_loops = {'red':6, 'blue':5, 'yellow':7,
               'orange':7, 'purple':4, 'green':6}

print('B begins:')

colors = input('What colors do you want for fruits: ')
Sum = 0
color = colors.split()
for i in range(len(color)):
    if color[i] in fruit_loops:
        Sum += fruit_loops[color[i]]
print('There are ' + str(Sum) + ' fruit loops with those colors')




print('C begins:')
attitude = 'yes'
colors = 'not quit'
while colors != 'quit':
    colors = input('What colors do you want for fruits: ')
    Sum = 0
    color = colors.split()
    for i in range(len(color)):
        if color[i] in fruit_loops:
            Sum += fruit_loops[color[i]]
    print('There are ' + str(Sum) + ' fruit loops with those colors')
print('Bye!')


        


print('Task 21 begins:')


print('A begins:')

fruit_loops = {'red':6, 'blue':5, 'yellow':7,
               'orange':7, 'purple':4, 'green':6}
Sum = 0

somethings = 'not quit'
while somethings != 'quit':
    somethings = input('Say something ')
    something = somethings.split()

    if 'floor' in something:
        if something[1] in fruit_loops:
            fruit_loops[something[1]] += 1
        print('You found one! for ' + str(something[1]) + ' you now have '
              + str(fruit_loops[something[1]]) )
    else:
        for i in range(len(something)):
            if something[i] in fruit_loops:
                Sum += fruit_loops[something[i]]

        print('There are ' + str(Sum) + ' fruit loops with those colors')
        


'''
print('B begins:')
n = 0
Sum = 0

fruit_loops = {'red':6, 'blue':5, 'yellow':7,
               'orange':7, 'purple':4, 'green':6}

what_you_find = input('What did you find: ')
color_you_find = what_you_find.split()
if 'floor' in color_you_find:
    if color_you_find[1] in fruit_loops:
        fruit_loops[color] += 1
        print('You found one! for ' + str(color) + ' you now have '
                  + str(fruit_loops[color]) )
    else:
        fruit_loops[color_you_find[1]] += 1
        print('You found a new color! You found: '
              + color_you_find[1])
elif color[n] in fruit_loops:
    while n <= len(color):
    #print(color)
    if color in color_you_find:
        Sum += fruit_loops[color]
    if Sum != 0:
        print('There are ' + str(Sum) + ' fruit loops with those colors')
    n += 1
'''    

print('B begins:')

fruit_loops = {'red':6, 'blue':5, 'yellow':7,
               'orange':7, 'purple':4, 'green':6}
Sum = 0
what_you_find = 'not quit'
while what_you_find != 'quit':
    what_you_find = input('What did you find: ')
    color_you_find = what_you_find.split()

    if 'floor' in color_you_find:
        if color_you_find[1] in fruit_loops:
            fruit_loops[color_you_find[1]] += 1
            print('You found one! for ' + str(color_you_find[1]) + ' you now have '
                  + str(fruit_loops[color_you_find[1]]) )
        elif color_you_find[1] not in fruit_loops:
            fruit_loops[color_you_find[1]] = 1
            print('You found a new color! You found: '
                  + color_you_find[1])
    else:
        for i in range(len(color_you_find)):
            if color_you_find[i] in fruit_loops:
                Sum += fruit_loops[color_you_find[i]]
                

        print('There are ' + str(Sum) + ' fruit loops with those colors') 

        
    
