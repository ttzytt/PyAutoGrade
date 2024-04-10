




temperature = int(input("You are a fish. What's the temperature today (in °F)? "))



if  temperature < 32: 
    print("You will be freezed!")
elif temperature >= 212:
    print("You are steamed!")
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

