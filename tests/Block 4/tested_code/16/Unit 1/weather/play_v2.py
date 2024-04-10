



temp_in_F = int(input('What is the temperature today (in °F)? '))

if((temp_in_F > 95) or (temp_in_F < 32)):
    print('You shouldn\'t play outside today')
else:
    raining = input('Is it raining? ')
    if(raining == 'yes') or (raining == 'Yes'):
        jacket = input('Do you have a jacket? ')
        if(jacket == 'yes') or (jacket == 'Yes'):
            print('You should play outside today')
        elif(jacket == 'no') or (jacket == 'No'):
            print('You shouldn\'t play outside today')
        else:
            print('I\'m sorry we don\'t support this answer')
    elif(raining == 'no') or (raining == 'No'):
        print('You should play outside today')
    else:
        print('I\'m sorry we don\'t support this answer')
            




