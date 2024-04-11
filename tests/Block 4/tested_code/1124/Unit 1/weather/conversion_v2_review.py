



tempF = float(input('What is the temperature today?(in Fahrenheit)'))
tempCf = (tempF-32) * 5/9

tempCs = str(tempCf)

if tempF > 90 and tempF < 150:
    print("Wow, that's hot.")
elif tempF <= 32 and tempF >-30:
    print("That's freezing!")
elif tempF > 32 and tempF < 50:
    print("Wow, that's cold.")
elif tempF >= 150 or tempF <= -30:
    print("How are you alive?")
print("That's " + tempCs + " Celsius.")


