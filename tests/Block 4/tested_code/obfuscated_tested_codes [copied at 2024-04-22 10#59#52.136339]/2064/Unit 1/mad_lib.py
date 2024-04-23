

"""
Teacher comments:
• Reviewer should be listed above
• Cool program
• Variable names must always follow proper style
• Many lines of code are too long (don't go past column 80)

Normally I give very thorough line-by-line feedback on the first
assignment, but this is too long to do that for. I'm going to start
graded normally on your next assignment – make sure that any version
that does extra stuff is in a separate file – thanks!

For your other assignments, if I make comments in your code,
I will use ### to make them stand out. (So don't use anything like
that yourself!!)

Do not remove any of my comments.
"""

'''
NOTE:
This is slightly different then the assignment intended. It still technically fulfils all of the rquirements which are:
    - Make a Madlib that has something to do with you
        - I enjoy reading, so I made my Madlib with a story
            - And while it does have alternate endings, that's part of the charm!
    -Include comments
        - As you can see I have added a bunch of comments
So yes, it does have some extra parts, but I still think that it counts because I have all of the parts that are required, and the assignment didn't specifically state that you couldn't do extra.
Plus only doing the assignment would have boring.
Thank you! :)
'''

import random

                                                                    ## Main text, in every version it displays this, the triple quotes are a multiline string, and the braces work like the the quotes and pluses in a normal string
text = '''
Once upon a {adjective01} {noun01} there was a {noun02} named {name01}. {name01} was chosen to save the lost artifact 
of {place01}, only to find that {place01} was under the control of the {adjective02} leader {celebrity01}. All of the
people were running around {verbEndingInIng01}. 
'''

                                                                    ## The first ending, you get this ending if you win at rock paper scisors
ending01 = '''
{name01} stared at the chaos in {adjective03}, trying to think of something to do. {name01}
glanced at the {adjective04} {noun03}. Large {pluralNoun01} formed, and {noun03} came {verbEndingInIng02}
down. Something started {verbEndingInIng03} towards {name01}. {name01} tried to ignore it, but
then he noticed it was the lost artifact of {place01}, the {rockPaperScissors}! {name01} quickly
grabbed the {rockPaperScissors} and hit {celebrity01} in the {bodyPart01} with it. The citizens of
{place01} rejoiced and quickly made a national {noun04} for {name01}.
'''

                                                                    ##The second ending scissors version, it is what happen if you lose at rock paper scissors and choose scissors
ending02_Scissors = '''
{name01} quickly started running, grabbing a pair of scissors for saftey. {name01}
had almost made it to the {place02} but then tripped, and fell on top of the scissors.
{name01} got impaled by the scissors and was then eaten by vultures, as he rotted to mush.

I guess that's why you don't run with scissors.
'''

                                                                    ##The second ending rock version, it is what happen if you lose at rock paper scissors and choose rock
ending02_Rock = ''' And so, {name01} ran away and hid in a {noun04}, hoping it was safe. {name01} stayed like that
until . . . . He heard large {pluralNoun01} form, and then {noun03} came {verbEndingInIng02} down, and just when
{name01} thought everything was alright, a big rock came rolling down and and flattened {name01}.
'''

                                                                    ##The second ending paper version, it is what happen if you lose at rock paper scissors and choose paper
ending02_Paper = '''
{name01} started {verbEndingInIng02} as fast as possible, until {name01} found a piece of paper and grabbed
it and jumped off a {noun03},and unfortunetly it didn't work as a parachute, and {name01} plummeted to the
ground, where a very loud "{loudNoise01}" was heard as {name01} hit the {noun04}.
'''

                                                                    
ending02_Mess_Up = '''
And so, {name01} grabbed a {rockPaperScissors} and started to {celebrity01}, determined to restore
the city by taking down the leader. {name01} {verbPastTense01} over there and tried to hit {celebrity01}
in the {bodyPart01}, but because {celebrity01} can only be defeated by rock, paper, or scissors, and
{name01} made the dumb choice of picking {rockPaperScissors}, {name01} was easily blocked by {celebrity01},
who shoved {name01} into an abyss where {name01} met their doom.
'''

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
