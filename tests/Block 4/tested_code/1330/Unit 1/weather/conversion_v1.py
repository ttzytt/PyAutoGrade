





temperature = int(input('What is the temperature today(in °F): '))


celsius = round(float(( int(temperature) - 32 ) * 5 / 9), 2)


if temperature >= 90:
    print('Wow that is hot. ')

print('That is ' + str(celsius) + 'C. ')
