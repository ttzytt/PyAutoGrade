'''
Task 21
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

    if user_key[0] == 'print':
        print(color_to_number)

    elif user_key[0] == 'floor': 

        for n in range(1,len(user_key)):
            if user_key[n] in available_colors:
                color_to_number[user_key[n]] += 1
            else:
                color_to_number[user_key[n]] = 1
                available_colors.append(user_key[n])
        
        print('Your color/new color is added successfully')       
        
    else: 
        for n in range(len(user_key)):
            
            if user_key[n] not in available_colors:
                print('Sorry, ' + user_key[n] + ' is unavailable')
                available = False
                break

            else:
                total_num += color_to_number[user_key[n]]
            
        if available == True:
            print('There are ' + str(total_num) + ' for total')
    print()
    user = input('Input your combinations of color(s): ')
    available = True

