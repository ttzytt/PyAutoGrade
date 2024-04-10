









weather = int(input('What is the temperature today (in °F)? '))
degree = round((weather-32)*5/9,2)




if weather > 90:
    print('Wow, that is hot!')
    print('That is ' + str(degree) + '°C')




else:
    print('That is ' + str(degree) + '°C')
