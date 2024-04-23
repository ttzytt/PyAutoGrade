'''
Task 20
Written by Alex
'''





color_to_number = ({'red':6, 'blue':5, 'yellow':7, 
                    'orange':7, 'purple':4, 'green':6})


available_colors = []
for colors in color_to_number:
    available_colors.append(colors)
    
user = input('Input your combinations of color(s): ')
while user != 'quit':
    user_key = user.split()
    total_num = 0
    available = True
    for n in range(len(user_key)):
        if user_key[n] not in available_colors:
            print('Sorry, ' + user_key[n] + ' is unavailable')
            available = False
            break
        total_num += color_to_number[user_key[n]]
    if available == True:
        print('Total: ' + str(total_num))
    print()
    user = input('Input your combinations of color(s): ')
    available = True


