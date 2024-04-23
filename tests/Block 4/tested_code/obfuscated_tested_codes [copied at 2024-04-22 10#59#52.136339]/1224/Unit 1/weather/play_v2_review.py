

fahrenheit = int(input('What is the temperature today (in °F)?'))
raining = input("Is it raining?")
if raining == 'Yes': 
    jacket = input('Do you have a jacket?')
    if jacket == 'No':
        print("You shouldn't play outside today.")
        
    elif jacket == 'Yes' and fahrenheit < 50 and fahrenheit > 32:
        print('You should play outside today.')
        
    elif jacket == 'Yes' and fahrenheit > 50 or fahrenheit < 32:
        print("You shouldn't play outside today.")

elif raining == 'No' and fahrenheit < 95 and fahrenheit > 50:
    print('You should play outside today.')
    
elif raining == 'No' and fahrenheit > 95 or fahrenheit < 50:
    print ("You shouldn't play outside today.")
    



    
    







    

    
    
       
