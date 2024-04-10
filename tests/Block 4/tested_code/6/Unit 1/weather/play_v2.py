












weather = int(input('What is the temperature today (in °F)? '))




if weather >= 95:
    print('You should not play outside today')
    



if weather <= 32:
    print('You should not play outside today')





if 32 < weather < 50:
    jacketAnswer = input('Do you have a jacket?(write Yes or No with capital letter at the front) ')
    if jacketAnswer == 'Yes':
      print('You should play outside today')

    elif jacketAnswer == 'No':
      print('You should not play outside today')





if 50 < weather < 95:
    rainingAnswer = input('Is it raining?(write Yes or No with capital letter at the front) ')
    if rainingAnswer == 'Yes':
        jacketAnswer = input('Do you have a jacket?(write Yes or No with capital letter at the front) ')
        if jacketAnswer == 'No':
            print('You should not play outside today')
        if jacketAnswer == 'Yes':
            print('You should play outside today')
    if rainingAnswer == 'No':
      print('You should play outside today')
