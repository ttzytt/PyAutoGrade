



temperature = int(input('What is the temperature today (in °F)?: '))


if temperature > 90:
    print('Wow, that is hot!')
elif 32 <= temperature < 50:
    print('That is so cold!')
elif temperature < 32:
    print('That is freezing!')


print('That is ' + str(round((temperature - 32)*(5/9), 2)) + '°C')
    


