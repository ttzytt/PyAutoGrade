








temperature = int(input("What's the temperature today (in °F)? "))




if temperature > 95 or temperature < 32: 
    print("You shouldn't play outside today.")
else:
    rain = input('Is it raining? ')
    if rain == 'No' and temperature >= 50:
        print('You should play outside today.')
    elif rain == 'No':
        print("You shouldn't play outside today.")
    elif rain == 'Yes':
        jacket = input("Do you have a jacket? ")
        if jacket == 'Yes': 
            print('You should play outside today.')
        elif jacket == 'No':
            print("You shouldn't play outside today.") 


