




import random
random.seed()


def find_current_winner(num_werewolves, num_villagers):
    if num_werewolves >= num_villagers:
        return 'werewolves'
    elif num_werewolves == 0:
        return 'villagers'
    else:
        return None

def find_winner(num_werewolves, num_villagers):

    day_night = 1
    
    while True:
        
        if find_current_winner(num_werewolves, num_villagers) != None:
           return find_current_winner(num_werewolves, num_villagers)
        
        
        if day_night % 2 != 0: 
            total_people = num_werewolves + num_villagers
            
            
            person_killed = random.randint(1, total_people)
            
            
            if person_killed <= num_werewolves:
                return find_winner(num_werewolves - 1, num_villagers)
            
            else:
                return find_winner(num_werewolves, num_villagers - 1)

        
        else:
            return find_winner(num_werewolves, num_villagers - 1)

        day_night += 1


def odds_of_werewolves_winning(num_werewolves, num_villagers):
  num_trials = 10000
  werewolves_wins = 0
  for i in range (num_trials):
      if find_winner(num_werewolves, num_villagers) == 'werewolves':
          werewolves_wins += 1
  return werewolves_wins/num_trials


print('Welcome! Please input the following starting conditions for your game.')
num_werewolves = int(input('Enter the number of werewolves: '))
num_villagers = int(input('Enter the number of villagers: '))
print('The odds of the werewolves winning was '
      + str(odds_of_werewolves_winning(num_werewolves, num_villagers)) + '. ')













