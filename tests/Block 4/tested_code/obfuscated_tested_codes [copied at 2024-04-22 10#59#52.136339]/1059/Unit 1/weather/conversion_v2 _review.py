

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


'''
The code works fine, but when I run it, the decimals extend on for more than two spaces.
Also, I don't understand why you converted temptwo into a float afterwards.
You could have said "float(input('What is the temperature today (in °F)?'))"
and skipped the conversion step.
Finally, the variable name pri is not neccessary.
You can do "print('That's' + tempstr + '°C.')" and skip the variable step.
Good job on this code!


'''
