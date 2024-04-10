



temperature = float(input('What is the temperature today(in °F)? '))


print()


if temperature > 90:
    print('Wow, that is hot.')


temp = round(((temperature - 32) * 5/9), 2)


print('That is '+ str(temp) + ' °C')    

