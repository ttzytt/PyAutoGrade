




temperature = float(input('What is the temperature today (in °F)? '))


if temperature > 95:
    
    print("You shouldn't play outside today.")
elif temperature > 32:
    
    raining = input('Is it raining? ')
    if raining.lower() == 'yes':
        
        waterproof = input('Are you waterproof? ')
        if waterproof.lower() == 'no':
            
            print("You shouldn't play outside today.")
        elif temperature < 50:
            arctic = input('Are you from the arctic? ')
            if arctic.lower() == 'no':
                
                print("You shouldn't play outside today.")
            else:
                
                print("You should play outside today.")
        else:
            
            print("You should play outside today.")
    elif temperature < 50:
        arctic = input('Are you from the arctic? ')
        if arctic.lower() == 'no':
            
            print("You shouldn't play outside today.")
        else:
            
            print("You should play outside today.")
    else:
        
        print("You should play outside today.")
else:
    
    print("You shouldn't play outside today.")


