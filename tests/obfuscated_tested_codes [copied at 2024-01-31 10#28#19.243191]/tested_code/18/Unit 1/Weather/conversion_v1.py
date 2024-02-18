



temperature = int(input('What is the temperature today (in °F)?: '))


if temperature > 90:
    print('Wow, that is hot!')


print('That is ' + str(round((temperature - 32)*(5/9), 2)) + '°C')


