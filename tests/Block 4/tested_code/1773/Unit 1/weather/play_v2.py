

celcius = 0.0


temperature = int(input('What is the temperature today (in °F)? '))



if temperature < 32 or temperature > 95:
    
    print("You shouldn't play outside today")

else:
    rain = input('Is it raining? ')
    if rain == 'yes':
        
        jacket = input('Do you have a jacket?')
        if jacket == 'yes':
            print('You should go play outside!')
        elif jacket == 'no':
            print("You shouldn't play outside today")
        else: 
            print("You messed up")
    elif rain == 'no':
        if temperature >= 32 and temperature <= 50:
            
            jacket = input('Do you have a jacket?')
            if jacket == 'yes':
                print('You should go play outside!')
            elif jacket == 'no':
                print("You shouldn't play outside today")
        else: 
            print('You should go play outside!')

        

    
   

        
               









 
        




