



temperature = int(input('What is the temperature today (in °F)? '))


tamperature_in_celsius = str((temperature - 32) / 1.8)


if temperature >= 90:
    
    print("Wow, that's hot. That's " + tamperature_in_celsius + " °C")
else:
    
    print("That's " + tamperature_in_celsius + "°C")

