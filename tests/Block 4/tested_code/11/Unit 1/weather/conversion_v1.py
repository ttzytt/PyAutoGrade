



a = int(input('What is the temperature today (in °F)? '))


b = str((a - 32) / 1.8)


if a >= 90:
    
    print("Wow, that's hot. That's " + b + " °C")
else:
    
    print("That's " + b + "°C")
