

 
temperature = int(input('What is the temperature today (in °F)? '))

if temperature > 95 and temperature < 32:
    print("You shouldn't play outside today.")

if temperature <= 95 and temperature >= 32:
    raining = input('Is it raining? ')
    if raining == 'yes':
        jacket = input('Do you have a jacket? ')
        if jacket == 'yes':
            print('You should play outside today.')
        if jacket == 'no':
            print("You shouldn't play outside today.")
    elif raining == 'no':
        if temperature >= 50:
            print('You should play outside today.')
        else:
            jacket = input('Do you have a jacket? ')
            if jacket == 'yes':
                print('You should play outside today.')
            if jacket == 'no':
                print("You shouldn't play outside today.")
        
    

