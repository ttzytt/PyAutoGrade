





Fahrenheit = float(input('What is the temperature today (in °F)? ')) 

if Fahrenheit > 90: 
    print("Wow that's hot.")
    
elif Fahrenheit < 32: 
    print("Oh! That's freezing.")


elif Fahrenheit < 50: 
    print("That's so cold.")


Celsuis = float (Fahrenheit - 32)/ 1.8 


print ("That's " + str(round(Celsuis,2)) + '°C.') 


