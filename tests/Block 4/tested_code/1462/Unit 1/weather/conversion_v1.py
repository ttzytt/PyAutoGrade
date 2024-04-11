



temperature = float(input('What is the temperature today (in °F)? '))


temp_converted = round((temperature-32) * 5/9, 2)



if temperature > 90: 
    print("Wow that's hot.")
    print("That's " + str(temp_converted) + " °C")
else:  
    
    print("That's " + str(temp_converted) + " °C")
    

