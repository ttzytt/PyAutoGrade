

fahrenheit = int(input('What is the temperature today? (in °F)?')) 
if fahrenheit > 91:
    print ("Wow that's hot.") 
elif fahrenheit < 32:
    print ("That's so cold!") 
celsius = (fahrenheit-32)*5/9 
print("That's" + ' ' + str(round(celsius))+ "°C.")




