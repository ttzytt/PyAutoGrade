










temperature_F = float(input('What is the temperature today (in °F)? '))


if(temperature_F<32):
           print("That's freezing.")
if(temperature_F<50):
    if(temperature_F>=32):
           print("That's so cold.")
if(temperature_F>90):
           print("Wow that's hot.")


temperature_C = (temperature_F - 32)*5/9


temperature_round = round(temperature_C, 2)
temperature_string = str(temperature_round)


print("That's " + temperature_string +" °C.")
