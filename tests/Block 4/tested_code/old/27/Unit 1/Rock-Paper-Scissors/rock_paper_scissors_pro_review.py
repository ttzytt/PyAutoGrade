

import random
random.seed()
loop = "continue"
choice_2_list = ['rock', 'paper', 'scissors']


score_1 = 0
score_2 = 0

ret = 0



def rps_score_round(choice_1, choice_2):
        
                
        if choice_1 == choice_2:
                return 0
        elif choice_1 == "rock":
                if choice_2 == "paper":
                        return -1
                elif choice_2 == "scissors":
                        return 1
        elif choice_1 == "paper":
                if choice_2 == "rock":
                        return 1
                elif choice_2 == "scissors":
                        return -1
        elif choice_1 == "scissors":
                if choice_2 == "rock":
                        return -1
                elif computer_select == "paper":
                        return 1


while loop != "q":     
        choice_1 = input('Enter the first choice: ')
        if choice_1 != 'rock':
                if choice_1 != 'paper':
                        if choice_1 != 'scissors':
                                print("Please enter something that's valid")
                                choice_1 = input('Enter the first choice: ')
        choice_2 = random.choice(choice_2_list)
        ret = rps_score_round(choice_1, choice_2)
        if(ret == 1):
                score_1 += 1
        elif(ret == -1):
                score_2 += 1
        print("score of you: ", score_1)
        print("score of computer", score_2)     
        loop = input("Do you want to continue playing? Enter quit or anything else: Enter q for quit ")
	
