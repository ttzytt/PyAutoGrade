









from random import choice, seed
seed()


user_choice = input('Rock, Paper, or Scissors: ').lower()

computer_choice = choice(['rock','paper','scissors'])

print('I choose ' + computer_choice)

if user_choice == 'rock':
    
    
    rock_battles = {
        'rock': 'We tie.',
        'paper': 'I win.',
        'scissors': 'You win'
    }

    print(rock_battles.get(computer_choice))
    
if user_choice == 'paper':
    
    paper_battles = {
        'rock': 'You win.',
        'paper': 'We tie.',
        'scissors': 'I win.'
    }

    print(paper_battles.get(computer_choice))
    
if user_choice == 'scissors':
    
    scissors_battles = {
        'rock': 'I win.',
        'paper': 'You win.',
        'scissors': 'We tie.'
    }

    print(scissors_battles.get(computer_choice))
