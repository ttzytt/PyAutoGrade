






temp_F = float(input('What is the temperature today?(in Fahrenheit) '))
print()

temp_C_float = (temp_F - 32) * 5/9

temp_C_float = round(temp_C_float, 2)

temp_C_str = str(temp_C_float)


if temp_F > 90:
              print("Wow, that's hot.")
              print()

print("That's " + temp_C_str + " Celsius.")


