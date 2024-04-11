



farenheit = float(input('What is the temperature today in °F? '))


if farenheit > 95:
    print('You shouldnt play outside today.')
elif farenheit < 32:
    print('You shouldnt play outside today.')


elif farenheit > 32 and farenheit < 50:
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
        elif jacket == 'No':
            frog = input('Are you a frog? ')
            if frog == 'Yes':
                print('You should play outside today.')
        else:
                print('You shouldnt play outside today.')
    else:
        print('You should play outside today.')
