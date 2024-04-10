



have_jacket = ''

temperature = int(input('What is the temperature today in °F? '))

rain = input('Is it raining? ').lower()
if (rain == 'yes') or (temperature > 32 and temperature < 50):
    have_jacket = input('Do you have a jacket? ').lower()

homework_done = input('Have you finished your homework yet? (yes/no) ').lower()
alive = input('Are you alive right now? (yes/no) ').lower()

if (rain == 'yes' and have_jacket == 'no') or temperature < 50 and have_jacket == 'no' or (temperature > 95 or temperature < 35)  or (alive == 'no' or homework_done == 'no'):
    print('You should not play outside today. ')

else:
    print('You should play outside today. ')
