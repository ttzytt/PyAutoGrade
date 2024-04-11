



import random



def rps_score_round(choice_1,choice_2):
    if choice_1 == choice_2:
        return 0


    elif choice_1 == 'rock': 
        if choice_2 == 'scissors':
            return 1
        else:
            return -1
           
        
    elif choice_1 == 'paper':
        if choice_2 == 'scissors':
            return 1
        else:
            return -1
           

    elif choice_1 == 'scissors':
        if choice_2 == 'paper':
            return 1
        else:
            return -1

ys = 0
cs = 0



Flag = False
while Flag == False:

    


    user_choice = input("Enter 'rock' or 'paper' or 'scissors', if you wish to exit the game, enter 'q': ")

    if user_choice == 'q':
        print('Game over')
        Flag = True

    elif user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
        computer = ['rock', 'paper', 'scissors']
      
        
        computer_choice = random.choice(computer)
        print('I choose ' + computer_choice  + '.')
        
        ys = ys + rps_score_round(user_choice,computer_choice) 
        cs = cs - rps_score_round(user_choice,computer_choice)
        print('Your score: ' + str(ys) + ' My score: ' + str(cs))
              


           




























    
       





