

temperature = int(input('What is the temperature today (in °F)? '))


if temperature < 32 or temperature >= 95:
    print("You should not go outside!")
    

elif temperature < 50:
    jacket = input('Do you have a jacket? ')
    if jacket == ('no'):
        print('You should not go outside today.')
    elif jacket == ('yes'):
        print('You can go outside today.')

else:
    rain = input("Is it raining? ")
    if rain == ('no'):
        print("You can go outside.")
    elif rain == ('yes'):
        print("You can go outside but it might be wet.")


