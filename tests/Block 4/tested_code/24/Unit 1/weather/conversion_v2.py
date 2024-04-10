




temperature = int(input('What temperature is it today (in °F)? '))

conversion = str(round((temperature - 32)*(5/9),2)) 


if temperature > 90:
    
    print("Wow that's hot.")
    print("That's " + conversion + ('°C'))

elif temperature > 50:
    
    print("That's average.")
    print("That is " + conversion + ('°C'))

elif temperature > 32:
    
    print("That's cold.")
    print("That is "+ conversion + ('°C'))

else:
    
    print("That's Freezing!")
    print("It is " + conversion + ("°C"))
