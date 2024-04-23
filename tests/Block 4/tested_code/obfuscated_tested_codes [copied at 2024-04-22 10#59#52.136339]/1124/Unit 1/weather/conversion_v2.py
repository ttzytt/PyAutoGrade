


'''
This program will convert Fahrenheit to Celsius and tell the user different
statements based on the temperature
'''


temp_F = float(input('What is the temperature today?(in Fahrenheit) '))
print()


temp_C_float = (temp_F - 32) * 5/9


temp_C_float = round(temp_C_float, 2)


temp_C_str = str(temp_C_float)



if temp_F > 90 and temp_F < 150:
    print("Wow, that's hot.")
    print()
elif temp_F <= 32 and tempF >-30:
    print("That's freezing!")
    print()
elif temp_F > 32 and temp_F < 50:
    print("Wow, that's cold.")
    print()
elif temp_F >= 150 or temp_F <= -30:
    print("How are you alive?")
    print()
print("That's " + temp_C_str + " Celsius.")


