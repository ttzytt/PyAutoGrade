





import random











def find_winner(num_werewolves, num_villager):
    phase_count = 0 
    while 0 < num_werewolves < num_villager:
        if phase_count % 2 == 0: 
            
            random_kill = random.randint(1, num_werewolves + num_villager)

            
            
            
            if random_kill <= num_werewolves: 
                                              
                num_werewolves -= 1
            else:
                num_villager -= 1

        else: 
            num_villager -= 1
        phase_count += 1

    if num_werewolves >= num_villager:
        return 'werewolves'
    return 'village'
    


def find_winner_2(num_werewolves, num_villager):
    phase_count = 0 
    while 0 < num_werewolves < num_villager:
        if phase_count % 2 == 0: 
            num_villager -= 1

        else: 
            
            random_kill = random.randint(1, num_werewolves + num_villager)

            
            
            
            if random_kill <= num_werewolves: 
                                              
                num_werewolves -= 1
            else:
                num_villager -= 1

        phase_count += 1

    if num_werewolves >= num_villager:
        return 'werewolves'
    return 'village'










def odds_of_werewolves_winning(num_werewolves, num_villager, tries = 100):
    games_won_by_werewolves = 0
    for i in range(tries):
        
        if find_winner(num_werewolves, num_villager) == 'werewolves':
            games_won_by_werewolves += 1

    return games_won_by_werewolves / tries


'''
INSANE ANALYSIS!!

When there are 2 werewolves and 100 villagers, the winrate of the werewolves
is about 0.29.
When there are 2 werewolves and 99 villagers, intuitively, it would seem that
werewolves would win more because there are less villagers to kill. However,
the winrate in this case is 0.24, substantially lower.


What causes this difference in winrate?


The game always starts with day. So:

(assume that every voting event kills a villager as well)

To kill 5 villagers: DAY NIGHT DAY NIGHT DAY
To kill 6 villagers: DAY NIGHT DAY NIGHT DAY NIGHT <---- SAME AMOUNT OF DAYS!

There is the same amount of days for 5 and 6 villagers, which means the same
amount of voting events where a werewolf can be voted out.

This means (assuming that all of the voting events are the same) that 102
people and 101 people take the same amount of days to kill even though
there are less people. 

find_winner_2 proves it, because it simulates with night first. When running
find_winner_2, the number of nights are the same but not the number of days.
The winrate is higher with 2 99 compares to 2 100 (which is the opposite of
find_winner.)


So...

We can see that the number of voting events are the same, so that does not
cause the difference in winrate. It depends on the probability of kicking out a
werewolf IN a voting event. With more villagers, the chances of voting out
a werewolf is lower, so the even number of villagers causes a higher winrate.

Compare 2 99 and 2 100:
2 99 takes 49 days
2 100 takes 49 days <--- less chance of voting werewolf = higher winrate

Compare 2 98 and 2 99:
2 98 takes 48 days  <--- less days = higher winrate
2 99 takes 49 days


In conclusion, the winrate of werewolves is higher when the number of
people to kill is even, as opposed to odd.


'''





get_tries = input("How many tries? Type 'q' to quit. ")

while get_tries != 'q':
    get_werewolves = input('How many werewolves? ')
    get_villagers = input('How many villagers? ')
    print()
    print('The odds of werewolves winning is '
          + str(odds_of_werewolves_winning(int(get_werewolves),
                                           int(get_villagers),
                                           int(get_tries)))
          + '.')
    print()
    get_tries = input("How many tries? Type 'q' to quit. ")

print()
print('Come again soon!')
