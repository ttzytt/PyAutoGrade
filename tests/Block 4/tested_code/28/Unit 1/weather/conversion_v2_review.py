




temperature_f = float(input('What is the temperature today (in °F)? '))



if temperature_f > 90:
    print("Wow that's hot.")
if temperature_f < 32:
    print("That's freezing.")
if temperature_f >= 32 and temperature_f < 50:
    print("That's so cold.")



temperature_c = (temperature_f - 32) * 5/9




if temperature_c % 1 == 0:
    print("That's " + str(int(temperature_c)) + " °C.")
else:
    print("That's " + str(round(temperature_c, 2)) + " °C.")


