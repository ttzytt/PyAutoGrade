


import random

random.seed()

print("Let's play rock paper")


player_choice = input("Enter 'rock' or 'paper'(all lowercase): ")


if player_choice == 'paper' :
    player_choice = 1
elif player_choice =='rock':
    player_choice = 0


computer_choice = random.randint(0,1)


if player_choice != 1 and 0:

    print("that's not rock or paper")
    print('learn how to read')
    



elif player_choice > computer_choice:
    print('''I choose rock
                    ____ 
                   /    \ 
                  |      | 
                 /        \ 
                 \________/ 

                   ''')
    print('You win.')


elif player_choice == computer_choice:

    
    if computer_choice == 1:
        print('''I choose paper
                    ____
                   |    |
                   |    |
                   |____|

                   ''')
        print('''We tie''')

    
    else:
        print('''I choose rock
                    ____ 
                   /    \ 
                  |      | 
                 /        \ 
                 \________/ 

                   ''')
        print('We tie')


else:
    print('''I choose paper
                    ____
                   |    |
                   |    |
                   |____|

                   ''')
    print('You lose')




