

def ask(question):
    while True: 
        response = input(question + " ").lower()
        if response == 'yes' or response == 'y':
            return True
        elif response == 'no' or response == 'n':
            return False
        else:
            print("Invalid Input.")






    





print('Choose a number between 1 and 10')
print('I\'ma try to guess it, answer "yes" or "no" to the following questions:')

if ask('Is your number odd?'):
    if ask('Is it divisible by 3?'):
        if ask('Is it prime?'):
            print('Your number is 3.')
        else:
            print('Your number is 9.')
    else:
        if ask('Is it prime?'):
            if ask('Is it divisible by 5?'):
                print('Your number is 5.')
            else:
                print('Your number is 7.')
        else:
            print('Your number is 1.')
else:
    if ask('Is it greater than 7? (not including 7)'):
        if ask('Is it divisible by 5?'):
            print('Your number is 10.')
        else:
            print('Your number is 8.')
    else:
        if ask('Is it prime?'):
            print('Your number is 2.')
        else:
            if ask('Is it divisible by 3?'):
                print('Your number is 6.')
            else:
                print('Your number is 4.')

print("Let's play again later!")
