




temperature = float(input("You are a fish. What's the temperature today (in °F)? "))

if  temperature < 32: 
    print("You are freezed!")
    
elif temperature >= 212:
    print("You are steamed!")
    
elif temperature < 50:
    print("It's too cold. You cannot go outside the water to play.")
    
else: 
    rain = input('Is it raining? ')
    
    if rain == 'Yes' and temperature >= 50: 
        print('You should play outside today.')
        
    elif rain == 'No':
        print("You have no water to breath! you will be dead if you play!")
        
        tank = input("Do you have a water tank? ")

        
        if tank == 'Yes': 
            print('You should play outside today.')
            
        elif tank == 'No':
            print("You are dead now！ ")

