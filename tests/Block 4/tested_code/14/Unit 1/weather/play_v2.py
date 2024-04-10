



temperature = int(input('What is the temperature today (in °F)? '))



if temperature > 95 or temperature < 32:
    print("You shouldn't play outside today")
    

elif temperature < 50:
    b_jacket = input('Do you have a jacket(yes/no)(no spaces, all lowercase)? ')
    
    if b_jacket == 'no':
        print('You should not play outside today')
    else:
        print('You should play outside today')


else:
    b_rain = input('Is it raining(yes/no)(no spaces, all lowercase)? ')
    
    if b_rain == 'yes':
        b_jacket = input('Do you have a jacket(yes/no)(no spaces, all lowercase)? ')
        if b_jacket == 'no':
            print('You should not play outside today')
        else:
            print('You should play outside today')         
    else:
        print('You should play outside today')
    
