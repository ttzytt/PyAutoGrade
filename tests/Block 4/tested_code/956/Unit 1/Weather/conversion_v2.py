










weather = int(input('What is the temperature today (in °F)? '))
degree = round((weather - 32) * 5/9,2)




if 120 >= weather >= 90:
    print('Wow, that is hot!')
    print('That is ' + str(degree) + '°C')




elif weather < 32:
    print('That is freezing')
    print('That is ' + str(degree) + '°C')




elif 32 <= weather < 50:
    print('That is so cold')
    print('That is ' + str(degree) + '°C')




elif weather > 120:
    print('Are you burning?')
    print('That is ' + str(degree) + '°C')




else:
    print('That is ' + str(degree) + '°C')
