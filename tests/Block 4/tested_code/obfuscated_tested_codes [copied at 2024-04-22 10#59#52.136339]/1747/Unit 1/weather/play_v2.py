




Integer = int(input('What is temperature today in °F? '))


if Integer >= 95 or Integer <= 32:
    print("You shouldn't play outside.")


elif Integer > 32 and Integer <= 50:
    
    Jacket = input('Do you have a jacket? ')
    
    if Jacket == 'yes':
        print("You should play outside")
    elif Jacket == 'no':
        print("You shouldn't play outside")


else:

    
    Rain = input('Is it raining? ')
    
    if Rain == 'yes'
        
        Jacket = input('Do you have a jacket? ')
        
        if Jacket == 'yes':
            print("You should play outside")
        elif Jacket == 'no':
            print("You shouldn't play outside")
    
    
    elif Rain == 'no':
        print("You should play outside")
