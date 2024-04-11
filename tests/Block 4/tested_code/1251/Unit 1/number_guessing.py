




import random
random.seed ()


target_number = random.randint(1,10)

human = 0



while human != target_number:
    print()
    
    human = int(input('type a number between 1 and 10 to guess the number: ')) 
    print()

    
    if human > target_number:
        print('Your number is larger than the answer')
    elif human < target_number:
        print('Your number is smaller than the answer')


print("You're correct!")
     

