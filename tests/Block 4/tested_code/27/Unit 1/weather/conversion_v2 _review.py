

temperature = int(input('What is the temperature today (in °F)? '))
if(temperature<32):
           print("That’s freezing.")
if(temperature<50):
    if(temperature>=32):
           print("That’s so cold.")


temptwo = (temperature - 32)*5/9
float(temptwo)
tempstr = str(temptwo)


pri = "That's " + tempstr +" °C."
print(pri)



