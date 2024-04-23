


import random 

random.seed()

player_choice = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ")

total_score = 0

while player_choice != 'q': 
        
        computer_choice = random.choice(('rock', 'paper', 'scissors'))

        

        print ("I choose " + computer_choice + ".")

        if player_choice == computer_choice:
                print('We tie.')


        elif player_choice == 'rock':
                if computer_choice == 'paper':
                        print('I win.')
                elif computer_choice == 'scissors':
                        print('You win.')

        elif player_choice == 'paper':
                if computer_choice =='rock':
                        print('You win.')
                elif computer_choice == 'scissors':
                        print('I win.')

        elif player_choice == 'scissors':
                if computer_choice == 'rock':
                        print ('I win.')
                elif computer_choice == 'paper':
                        print('You win.')

        elif player_choice == 'q':
                print('Bye bye!')
                        
        else:
                print("Silly! That's not rock paper scissors! :(")
        

        
            

        def rps_score_round(player_choice, computer_choice):
                if player_choice == computer_choice:
                        return 0
        
                elif player_choice == 'rock':
                        if computer_choice == 'paper':
                                return -1
                        elif computer_choice == 'scissors':
                                return 1

                elif player_choice == 'paper':
                        if computer_choice =='rock':
                                return 1
                        elif computer_choice == 'scissors':
                                return -1

                elif player_choice == 'scissors':
                        if computer_choice == 'rock':
                                return -1
                        elif computer_choice == 'paper':
                                return 1

        total_score += rps_score_round(player_choice, computer_choice)
        


                
        print('Your score right now is: ' + str(total_score))        
        print()
        
        player_choice = input("Enter 'rock', 'paper' or 'scissors', or 'q' to quit: ")

