



import random
random.seed()
loop = "continue"
choice_2_list = ['rock', 'paper', 'scissors']

score_user = 0
score_computer = 0

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
        while loop != "quit":
                choice_1 = input('Enter the first choice: ')
                if choice_1 != 'rock':
                        if choice_1 != 'paper':
                                if choice_1 != 'scissors':
                                        print("Please enter something that's valid")
                                        choice_1 = input('Enter the first choice: ')
                choice_2 = random.choice(choice_2_list)
                print("You choose", choice_1)
                print("I choose", choice_2)
                print()        
                ret = rps_score_round(choice_1, choice_2)
                if ret == 1:
                        score_user += 1
                elif ret == -1:
                        score_computer += 1
                print("score of you: ", score_user)
                print("score of computer", score_computer)    
                loop = input("Do you want to continue playing? Enter q for quit ")
	
