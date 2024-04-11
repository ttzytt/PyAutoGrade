

tempF = float(input('What is the temperature today (in °F)? '))
human = input('Are you a human?')
if human == 'yes' or 'Yes':
    
    if tempF >= 95 or tempF <= 32:
        print("You shouldn't play outside today.")
    
    
    
    
    elif tempF < 95 and tempF >= 50:
        rain = input("Is it raining? ")
        if rain == ("yes" or "Yes"):
            jacket1 = input("Do you have a jacket? ")
            if jacket1 == ("yes" or "Yes"):
                print("You should play outside today.")
            else: print("You shouldn't play outside today.")
        else: print("You should play outside today.")
    
    elif tempF > 32 and tempF < 50:
        jacket2 = input("Do you have a jacket? ")
        if jacket2 == ("yes" or "Yes"):
            print("You should play outside today.")
        else: print("You shouldn't play outside today.")
