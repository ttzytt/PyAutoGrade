





tempF = float(input('What is the temperature today (in °F)? '))
print()


human = input('Are you a human? ')
print()


if human == 'yes' or human == 'Yes':
    
    
    if tempF >= 95 or tempF <= 32:
        print("You shouldn't play outside today.")
        
        
        
    elif tempF < 95 and tempF >= 50:
        rain = input("Is it raining? ")
        print()
        if rain == ("yes" or "Yes"):
            jacket1 = input("Do you have a jacket? ")
            print()
            if jacket1 == ("yes" or "Yes"):
                print("You should play outside today.")
            else: print("You shouldn't play outside today.")
        else: print("You should play outside today.")


        
    elif tempF > 32 and tempF < 50:
        jacket2 = input("Do you have a jacket? ")
        print()
        if jacket2 == ("yes" or "Yes"):
            print("You should play outside today.")
        else: print("You shouldn't play outside today.")

        
elif human == 'no' or human == 'No':
    print('This program is only made for humans, SCRAM!')

else:
    print('That is not an answer, shutting down.')
