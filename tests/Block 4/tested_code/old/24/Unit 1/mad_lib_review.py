





import random

                                                                    ## Main text, in every version it displays this, the triple quotes are a multiline string, and the braces work like the the quotes and pluses in a normal string
text = 

                                                                    ## The first ending, you get this ending if you win at rock paper scisors
ending01 = 

                                                                    ##The second ending scissors version, it is what happen if you lose at rock paper scissors and choose scissors
ending02_Scissors = 

                                                                    ##The second ending rock version, it is what happen if you lose at rock paper scissors and choose rock
ending02_Rock = 

                                                                    ##The second ending paper version, it is what happen if you lose at rock paper scissors and choose paper
ending02_Paper = 

                                                                    
ending02_Mess_Up = 

def getMadlibInputs(questions):
    
                                                                    
                                                                    
    
    inputs = {}                                                     
    for (k, v) in questions.items():
        inputs[k] = input("Input a{v}: ".format(k=k, v=v))
    return inputs

def playRockPaperScissors():

                                                                    
    
    draw = True                                                     
    while (draw == True):                                           
        userChoice = input('Let\'s play rock, paper, scisors! Type in "rock", "paper", or "scissors" EXACTLY to input your choice! ')
        if (userChoice == 'rock' or userChoice == 'paper' or userChoice == 'scissors'):  ##This makes sure that the user actually choose rock, paper or scissors, so that the computer can figure out who won.
            num = random.randint(1,3)                               ## This chooses a random integer from 1-3 inclusive and assigns it to the variable num
            if (num == 1):                                          ## This function determines weather the computer will play fair, or if it will cheat. If num is 1, then it will run this function and it will play fair, but if it is anything else it will cheat. Since num can only be 1, 2, or 3, the computer has a 1/3 chance of playing fair.
                computer_rps_choice = rockPaperScissorsChoiceFair() ## This calls the function rockPaperScissorsChoiceFair and assigns its output to computer_rps_choice, look at rockPaperScissorsChoice function for more detail
                if(userChoice == computer_rps_choice):              ## If the users rock paper scissors choice is the same as the computers, It prints a draw. Note that the draw function stays True here, so the while loop will repeat
                    print('I played ' + computer_rps_choice + '! Draw! Let\'s play again!')
                elif((computer_rps_choice =='rock' and userChoice == 'scissors') or (computer_rps_choice =='scissors' and userChoice == 'paper') or (computer_rps_choice =='paper' and userChoice == 'rock')): 
                    print('I played ' + computer_rps_choice + '! I win!') 
                    winOrLose = True                                
                    draw = False                                    
                else:                                               
                    print('You win! Good game!')
                    winOrLose = False                               
                    draw = False                                    
            else:                                                   
                computer_rps_choice = rockPaperScissorsChoiceUnFair(userChoice)  
                print('I played ' + computer_rps_choice + '! I win!')  
                winOrLose = True                                    
                draw = False                                        
                  
        else:                                                       
            print('Wow, you can\'t even follow simple directions. Well, you obviously lose, and maybe you should also go back to kindergarten!')  ## Tells the user they lose
            winOrLose = True                                        ## Since the user din't play by the rules, the computer wins, so winOrLose is marked as True
            draw = False                                            

    return winOrLose, userChoice                                    
                                                              
        

def rockPaperScissorsChoiceUnFair(user_rps_choice):

                                                                    
    
    if (user_rps_choice == 'rock'):                                 
        rps_choice = 'paper'
    elif (user_rps_choice == 'paper'):                              
        rps_choice = 'scissors'
    elif (user_rps_choice == 'scissors'):                           
        rps_choice = 'rock'

    return rps_choice                                               

def rockPaperScissorsChoiceFair():

                                                                    
    
    num = random.randint(1,3)                                       
    if (num == 1):                                                  
        rps_choice = 'rock'
    elif (num == 2):                                                
        rps_choice = 'paper'
    elif (num == 3):
        rps_choice = 'scissors'                                     
    
    return rps_choice                                               

def main():

    questions = {                                                   
        'adjective01' : 'n adjective',
        'noun01' : ' noun',
        'noun02' : ' noun',
        'name01' : ' name',
        'place01' : ' place',
        'adjective02' : 'n adjective',
        'celebrity01' : ' celebrity',
        'verbEndingInIng01' : ' verb ending in ing',
        'adjective03' : 'n adjective',
        'adjective04' : 'n adjective',
        'noun03' : ' noun',
        'pluralNoun01' : ' plural noun',
        'verbEndingInIng02' : ' verb ending in ing',
        'verbEndingInIng03' : ' verb ending in ing',
        'bodyPart01' : ' body part',
        'noun04' : ' noun',
        'place02' : ' place',
        'loudNoise01' : ' loud noise',
        'verbPastTense01' : ' verb, past tense'
        }

    inputs = getMadlibInputs(questions)                             
    rpsWinOrLose, userChoice = playRockPaperScissors()              
    inputs['rockPaperScissors'] = userChoice                        

    if(rpsWinOrLose):                                               
        print(text.format(**inputs))                                
        if(inputs['rockPaperScissors'] == 'paper'):                 
            print(ending02_Paper.format(**inputs))
        elif(inputs['rockPaperScissors'] == 'scissors'):            
            print(ending02_Scissors.format(**inputs))
        elif (inputs['rockPaperScissors'] == 'rock'):               
            print(ending02_Rock.format(**inputs))
        else:
            print(ending02_Mess_Up.format(**inputs))                
    else:                                                           
        print(text.format(**inputs))
        print(ending01.format(**inputs))



if __name__ == '__main__':                                          
    main()                                                          
