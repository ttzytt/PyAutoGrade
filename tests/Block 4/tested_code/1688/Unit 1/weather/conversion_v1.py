




temp_fahrenheit = int(input('What is the temperature today (in °F)? '))
temp_celsius = (temp_fahrenheit - 32) * 5/9



temp_celsius_100 = int(temp_celsius * 100)
temp_celsius_10 = int(temp_celsius * 10)

if temp_celsius_100 % 100 == 0:
    
    rounded_celsius = int(temp_celsius)
    
elif temp_celsius_10 % 10 == 0:
    
    rounded_celsius = round(temp_celsius, 1)
    
else:
    rounded_celsius = round(temp_celsius, 2)



if temp_fahrenheit > 90:
    
    print("Wow, that's hot.")
    print(f"That's {rounded_celsius} °C.")
    
else:
    print(f"That's {rounded_celsius} °C.")
    

























