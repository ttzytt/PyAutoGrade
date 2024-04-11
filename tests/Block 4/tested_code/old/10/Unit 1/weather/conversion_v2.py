


fahrenheit = int(input('What is the temperature today? (in °F)?'))

if fahrenheit > 90:
    print("Wow that's hot.")
    
elif fahrenheit < 50:
    print ("That's so cold!")
    
elif fahrenheit < 32:
    print("That's freezing!")

celsius = (fahrenheit-32)*5/9 
print("That's" + ' ' + str(round(celsius))+ "°C.")



