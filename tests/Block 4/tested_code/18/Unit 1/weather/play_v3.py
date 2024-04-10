



integer = int(input('What is temperature today in °F? ')) 


if integer >= 95:  
    print("Please don't play outside. You're gonna burn!")

elif integer <= 32:  
    print("It's freezing. Please don't play outside!")

elif integer > 32 and integer <= 50: 
    print("It's kinda cold outside. Think before you head out.")
    rain = input('Is it raining? ') 
    
    if rain == 'yes':
        jacket = input('Do you have a jacket? ')
        
        if jacket == 'yes':
            print("If you play outside, remember to wear the jacket!")
        elif jacket == 'no':
            print("You shouldn't play outside today. You'll soak!")
    
    elif rain == 'no':
        print('Okay, but still think before you head out.')

else: 
    
    rain = input('Is it raining? ')
    if rain == 'yes'
        jacket = input('Do you have a jacket? ')
        if jacket == 'yes':
            print("If you play outside, remember to wear the jacket!")
        elif jacket == 'no':
            print("You shouldn't play outside today. You'll soak!")
    elif rain == 'no':
        print('The weather seems nice. You should play outside today!')


