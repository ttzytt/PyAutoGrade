

celcius = 0.0


temp = int(input('What is the temperature today (in °F)? '))


if temp < 32:
    print("That's freezing!")

elif temp >= 32 and temp < 50:
    print("That's so cold!")

elif temp >= 50:
    print("Feels like temperature haha!")
        



celcius = (temp - 32) * (5/9)
print("That's " + str(round(celcius,2)) + ' °C.')


