



temperature = float(input('What is the temperature today in °F? '))


if temperature > 95:
    print('You shouldnt play outside today.')
elif temperature < 32:
    print('You shouldnt play outside today.')
    

elif temperature > 32 and temperature < 50:
    jacket = input('Do you have a jacket? ')
    if jacket == 'Yes':
        print('You should play outside today.')
    else:
        print('You shouldnt play outside today.')


else:
    rain = input('Is it raining? ')


    if rain == 'Yes':
        jacket = input('Do you have a jacket? ')
        if jacket == 'Yes':
            print('You should play outside today.')
        else:
            print('You shouldnt play outside today.')
    else:
        print('You should play outside today.')
        


