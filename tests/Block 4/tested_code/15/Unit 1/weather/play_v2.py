

 
temperature = int(input('What is the temperature today (in °F)? '))

if temperature > 95 and temperature < 32:
    print("You shouldn't play outside today.")

elif temperature <= 95 and temperature >= 50:
    raining = input('Is it raining? ')
    if raining == 'yes':
        jacket = input('Do you have a jacket? ')
        if jacket == 'yes':
            print('You should play outside today.')
        elif jacket == 'no':
            print("You shouldn't play outside today.")
    elif raining == 'no':
        print('You should play outside today.')

elif temperature < 50 and temperature >= 32:
    jacket = input('Do you have a jacket?')
    if jacket == 'yes':
        print('You should play outside today.')
    elif jacket == 'no':
        print("You shouldn't play outside today.")

        
    
