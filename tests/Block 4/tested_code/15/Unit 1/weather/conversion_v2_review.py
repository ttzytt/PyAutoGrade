


temperature = int(input('What is the temperature today (in °F)? '))

if temperature > 90:
     print("Wow that's hot.")
elif temperature < 32:
    print("That's freezing.")
elif temperature >= 32 and temperature < 50:
    print("That's so cold.")
else:
     print("That's normal.")
     
celsius = str(round((temperature-32)/(9/5),2))
print("That's " + celsius + ' °C')





