


import random
random.seed()


def rps_score_round(choice_1, choice_2): 
    
    
    
    
    if choice_1 == choice_2:  
        return 0
    elif choice_1 == 'rock':
        if choice_2 == 'paper':
            return -1
        else: 
            return 1
            
    elif choice_1 == 'paper':
        if choice_2 == 'rock':
            return 1
        else: 
            return -1
        
    else:  
        if choice_2 == 'rock':
           return -1
        elif choice_2 == 'paper':
            return 1
        
       



point = 0 
play_again = 'yes'
while play_again == 'yes':
    human_input = input('Enter rock, paper, scissor, or q to quit (the number represents your total points): ') 
    computer_input = random.choice(['rock','paper', 'scissor'])
    while human_input!= 'rock' and human_input != 'paper' and human_input != 'scissor' and human_input != 'q':
        print('Previous input not valid, follow instructions')
        human_input = input('Enter rock, paper, scissor, or q to quit (the number represents your total points): ')
    point_function = rps_score_round(human_input, computer_input)
    
    
    if  human_input == 'q': 
        play_again = 'no'
        print('sad to see you go')
    elif point_function == -1:
        print(computer_input)
        print('I win')
        point -= 1
    elif point_function == 1:
        print(computer_input)
        print('You win')
        point += 1 
    elif point_function == 0:
        print(computer_input)
        print('We tie')
        
    print(point) 



 




















