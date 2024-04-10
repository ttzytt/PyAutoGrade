




Integer = int(input('What is temperature today in °F? '))



if Integer >= 90:
    print('Wow that is hot.')

elif Integer >= 32 and Integer <= 50:
    print('OMG that is cold.')

elif Integer <= 31:
    print('Wear more clothing. It is freezing!!')


Celsius = (Integer - 32) / 1.8
print('That is ' + str(Celsius) + '°C.')
