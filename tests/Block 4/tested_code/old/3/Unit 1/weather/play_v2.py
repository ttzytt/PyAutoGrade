



temperature = int(input('What is the temperature today(in °F)? '))



if temperature > 95 :
    print("You shouldn't play outside today.")

elif temperature >= 50 and temperature <= 95:
    answer_1 = input('Is it raining? ')
    
    if answer_1 == 'Yes':
        answer_2 = input('Do you have a jacket? ')

        if answer_2 == 'No':
            print("You should't play outside today.")
        else:
            print('You should play outside today.')

    else:
        print('You should play outside today.')

elif temperature > 32 and temperature < 50:
    answer_2 = input('Do you have a jacket? ')

    if answer_2 == 'Yes':
        print('You should play outside today.')
        
    else:
        print("You should't play outside today.")
    
else:
    print('You should not play outside today.')
