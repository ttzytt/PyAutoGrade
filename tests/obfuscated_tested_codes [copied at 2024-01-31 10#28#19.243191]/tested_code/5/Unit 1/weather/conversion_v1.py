

celcius = 0.0


temp = int(input('What is the temperature today (in °F)? '))
print(temp)

if temp > 90:
    print('Wow thats hot.')

celcius = (temp - 32) * (5/9)
print("That's " + str(celcius) + ' °C.')


