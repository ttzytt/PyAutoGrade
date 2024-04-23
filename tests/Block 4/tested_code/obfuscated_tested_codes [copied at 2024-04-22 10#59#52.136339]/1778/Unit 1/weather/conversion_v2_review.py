



Fahrenheit = float(input("What is the temperature today(in °F)?"))
Celsius = str(round((5 * (Fahrenheit - 32) / 9)))


if Fahrenheit > 90:
    print("Wow that's hot.")
    print("That's " + Celsius + " °C.")


elif Fahrenheit<32:
    print("That's freezing.")
    print("That's " + Celsius + " °C.")



elif Fahrenheit>=32 and Fahrenheit<50:
    print("That's so cold.")
    print("That's " + Celsius + " °C.")


else:
    print("That's " + Celsius + " °C.")
!



    
    
