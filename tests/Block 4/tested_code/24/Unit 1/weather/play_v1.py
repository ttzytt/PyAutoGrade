


temperature = int(input('What is the temperature today (in °F)? '))
conversion = str(round((temperature - 32)*(5/9),2)) 


if temperature > 95 or temperature <= 50:
    
    print("You shouldn't play outside today.")
    print("That's " + conversion + "°C.")
    
else:
    
    print("You should play outside today.")
    print("That's " + conversion + "°C.")

