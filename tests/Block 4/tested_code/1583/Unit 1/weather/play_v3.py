



temperature = float(input('What is the temperature today (in °F)? '))


if temperature > 95 or temperature < 32: 
    print("You shouldn't play outside today.")

elif temperature >= 50: 
    is_raining = input('Is it raining? ')
    if is_raining.lower() == 'yes': 
                                    
        is_waterproof = input('Are you waterproof? ')
        if is_waterproof.lower() == 'no':
            print("You shouldn't play outside today.")
        elif is_waterproof.lower() == 'yes':
            print('You should play outside today.')
        else: 
            print('Invalid answer.')
    elif is_raining.lower() == 'no': 
        print('You should play outside today.')
    else:
        print('Invalid answer.')
        
else: 
      
    from_arctic = input('Are you from the arctic? ')
    if from_arctic.lower() == 'no': 
        print("You shouldn't play outside today.")
    elif from_arctic.lower() == 'yes':
        print("You should play outside today.")
    else:
        print('Invalid answer.')
