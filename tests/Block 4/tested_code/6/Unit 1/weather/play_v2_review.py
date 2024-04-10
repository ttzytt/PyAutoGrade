





weather = int(input('What is the temperature today (in °F)? '))
rainingAnswer = input('Is it raining? ')
jacketAnswer = input('Do you have a jacket? ')



if weather > 95:
    print('You should not play outside today')


if weather < 32:
    print('You should not play outside today')




if 32 < weather < 50:
    if jacketAnswer == 'Yes':
      print('You should play outside today')

    if jacketAnswer == 'No':
      print('You should not play outside today')



if 50 < weather < 95:
    if rainingAnswer == 'Yes':
      jacketAnswer == 'No'
      print('You should not play outside today')

    if rainingAnswer == 'Yes':
      jacketAnswer == 'Yes'
      print('You should play outside today')

    if rainingAnswer == 'No':
      print('You should play outside today')
