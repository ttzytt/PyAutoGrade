




temperature_f = float(input('What is the temperature today (in °F)? '))

if temperature_f > 90:
    print("Wow that's hot.")


temperature_c = (temperature_f - 32) * 5/9




if temperature_c % 1 == 0: 
    print("That's " + str(int(temperature_c)) + " °C.")
else:
    print("That's " + str(round(temperature_c, 2)) + " °C.")
