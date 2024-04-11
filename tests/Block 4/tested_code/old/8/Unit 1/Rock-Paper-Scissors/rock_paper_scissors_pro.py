





import random

random.seed()
player = input("Enter rock, paper, scissors: ")

def rps():
        score = 0
        if player == 'rock' and bot == 'scissors':
            score = score + 1
        if player == 'scissors' and bot == 'paper':
            score = score + 1
        if player == 'paper' and bot == 'rock':
            score = score + 1
        if player == 'rock' and bot == 'paper':
            score = score - 1
        if player == 'paper' and bot == 'scissors':
            score = score - 1
        if player == 'scissors' and bot == 'rock':
            score = score - 1
        else:
            score = score
        return(score)
rps_score = 0

while player != 'quit':
    bot = random.choice(['rock' , 'paper' , 'scissors'])

    
    if player == 'rock' and bot == 'paper':
        print('I chose paper.')
        print('You lose!')
    elif player == 'rock' and bot == 'scissors':
        print('I chose scissors.')
        print('You win!')
    elif player == 'paper' and bot == 'rock':
        print('You win!')
        print('I chose rock.')
    elif player == 'paper' and bot == 'scissors':
        print('I chose scissors.')
        print('You lose!')
    elif player == 'scissors' and bot == 'paper':
        print('I chose paper.')
        print('You win!')
    elif player == 'scissors' and bot == 'rock':
        print('I chose rock.')
        print('You lose!')
    elif player == bot:
        print('I chose ' + player + '.')
        print('We tie!')
    elif player != 'rock' or player != 'paper' or player != 'scissors' or player != 'quit':
        print('Please enter rock, paper, or scissors')

    rps_score = rps_score + rps()
    print("Your score is: " + str(rps_score))
    player = input("Enter rock, paper, scissors(Enter 'quit' if you want to stop playing): ")

print("Thanks for playing!")
print("Your final score was: " + str(rps_score))


