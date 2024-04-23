


import random
random.seed()


c_choice = random.randint(1,10)



p_choice = 0



while p_choice != c_choice:
    
    p_choice = int(input('choose and integer between 1 and 10 (inclusive): '))

    if p_choice > c_choice:
        print('too high')
    elif p_choice < c_choice:
        print('too low')
    else:
        p_choice = c_choice


print('Congrats u got it')
        
