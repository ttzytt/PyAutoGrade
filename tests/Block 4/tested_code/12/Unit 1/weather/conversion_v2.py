




fahrenheit = float(input("What is the temperature today(in °F)? "))
celsius = float(5 * (fahrenheit - 32) / 9)


if fahrenheit > 90:
    
    print("Wow that's hot.")

elif fahrenheit < 32:
    
    print("That's freezing.")

elif fahrenheit >= 32 and fahrenheit < 50:
    
    print("That's so cold.")


print("That's " + str(celsius) + " °C.")
