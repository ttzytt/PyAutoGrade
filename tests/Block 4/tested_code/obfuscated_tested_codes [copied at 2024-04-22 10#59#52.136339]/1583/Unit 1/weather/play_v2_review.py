






temperature = float(input('What is the temperature today (in °F)? '))


if temperature > 95 or temperature < 32:
    
    print("You shouldn't play outside today.")

'''
R Inconsistent comparison string (== 'yes' vs == 'no')
R It doesn't really matter if you're sure the user will type Yes or No
R But:
R Asking about rain and giving an invalid answer will produce a yes
R Asking about jacket and giving an invalid answer will produce a no
R Doesn't seem to be intentional
'''
elif temperature > 50:
    # If it's greater than 50, ask if it's raining
    raining = input('Is it raining? ')
    if raining.lower() == 'yes':
        # If it's raining, ask about a jacket
        jacket = input('Do you have a jacket? ')
        if jacket.lower() == 'no':
            
            print("You shouldn't play outside today.")
        else:
            
            print('You should play outside today.')
    else:
        
        print('You should play outside today.')
else:
    
    jacket = input('Do you have a jacket? ')
    if jacket.lower() == 'no':
        
        print("You shouldn't play outside today.")
    else:
        
        print("You should play outside today.")
