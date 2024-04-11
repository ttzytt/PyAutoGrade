



temperature = int(input('What is the temperature today (in °F)?: '))

if temperature > 90:
    print('Wow, that is hot!')
    print('That is ' + str(round((temperature - 32)*(5/9), 2)) + '°C')

elif 50 <= temperature <= 90:
    print('That is ' + str(round((temperature - 32)*(5/9), 2)) + '°C')

elif 32 <= temperature < 50:
    print('That is ' + str(round((temperature - 32)*(5/9), 2)) + '°C')
    print('That is so cold!')

elif temperature < 32:
    print('That is ' + str(round((temperature - 32)*(5/9), 2)) + '°C')
    print('That is freezing!')



    












