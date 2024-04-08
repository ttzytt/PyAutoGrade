





temp = int(input('What is the temperature today (in °F)? '))
def ask_rain():
    global b_rain
    b_rain = input('Is it raining(yes/no)(no spaces, all lowercase)? ')
def ask_jacket():
    global b_jacket
    b_jacket = input('Do you have a jacket(yes/no)(no spaces, all lowercase)? ')


if temp > 95 or temp < 32:
    print("You shouldn't play outside today")
    
elif temp < 50:
    ask_jacket()

    if b_jacket == 'no':
        print('You should not play outside today')
    else:
        print('You should play outside today')
else:
    ask_rain()

    if b_rain == 'yes':
        ask_jacket()
        if b_jacket == 'no':
            print('You should not play outside today')
        else:
            print('You should play outside today')
    else:
        print('You should play outside today')
    
