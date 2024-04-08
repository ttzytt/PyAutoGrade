




temperature = float(input('What is the temperature today (in °F)? '))


if temperature > 95 or temperature < 32: 
    print("You shouldn't play outside today.")

elif temperature >= 50: 
    is_raining = input('Is it raining? ')
    if is_raining.lower() == 'yes': 
        has_jacket = input('Do you have a jacket? ')
        if has_jacket.lower() == 'no':
            print("You shouldn't play outside today.")
        elif has_jacket.lower() == 'yes':
            print('You should play outside today.')
        else: 
            print('Invalid answer.')
    elif is_raining.lower() == 'no': 
        print('You should play outside today.')
    else:
        print('Invalid answer.')
        
else: 
      
    has_jacket = input('Do you have a jacket? ')
    if has_jacket.lower() == 'no': 
        print("You shouldn't play outside today.")
    elif has_jacket.lower() == 'yes':
        print("You should play outside today.")
    else:
        print('Invalid answer.')
