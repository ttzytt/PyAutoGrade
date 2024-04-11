
tempurature = input('What is the temperature today (in °F)? ')


tempurature = int(tempurature)



if tempurature >= 90:
    print('Wow thats hot.')
elif tempurature >= 32 and tempurature < 50:
    print('Thats so cold.')


print('Thats ' + str((tempurature - 32) * 5/9) + '°C.')
