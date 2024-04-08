






temperature = int(input('What is the temperature today(in °F): '))


celsius = round(float(( int(temperature) - 32 ) * 5 / 9), 2)


if temperature >= 90:
    print('Wow that is hot. ')
    print('That is ' + str(celsius) + '℃. ')

elif temperature < 32:
    print('That is freezing.')

elif temperature >= 32 and temperature < 50:
    print('That is so cold.')

print('That is ' + str(celsius) + '℃. ')
