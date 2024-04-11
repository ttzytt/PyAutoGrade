
tempurature = int ('What is the tempurature today (in °F)? ')


tempurature = int(tempurature)


if tempurature > 95 or tempurature < 50:
    print('You shouldnt play outside today. ')
elif tempurature <95 or tempurature >50:
    print('You should play outside today. ')


if tempurature > 32 and tempurature < 50:
    print('Do you have a jacket?')


jacket = input('Do you have a jacket?')

jacket = int(jacket)

rain = input('Is it raining?')

rain = int(rain)


if rain == 'Yes' and jacket == 'Yes':
    print('You shouldn play outside today. ')
elif rain == 'Yes' and jacket == 'No':
    print('You shouldnt play outside today. ')
else:
    print('You should play outside today')
