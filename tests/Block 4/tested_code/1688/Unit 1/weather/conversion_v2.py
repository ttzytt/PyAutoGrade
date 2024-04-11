




temperature_fahrenheit = int(input('What is the temperature today (in °F)? '))
temperature_celsius = (temperature_fahrenheit - 32) * 5/9



temp_celsius_100 = int(temperature_celsius * 100)
temp_celsius_10 = int(temperature_celsius * 10)

if temp_celsius_100 % 100 == 0:
    
    rounded_celsius = int(temperature_celsius)
    
elif temp_celsius_10 % 10 == 0:
    
    rounded_celsius = round(temperature_celsius, 1)   
    
else:
    rounded_celsius = round(temperature_celsius, 2)   






if temperature_fahrenheit > 90:
    
    print("Wow, that's hot.")
    print(f"That's {rounded_celsius} °C.")
    
elif 50 > temperature_fahrenheit >= 32:
    
    print("That's so cold.")
    print(f"That's {rounded_celsius} °C.")
    
elif temperature_fahrenheit < 32:
    
    print("Ugh, that's freezing.")
    print(f"That's {rounded_celsius} °C.")
    
else:
    print(f"That's {rounded_celsius} °C.")
