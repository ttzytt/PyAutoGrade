







import random
random.seed()




def find_winner(num_werewolves, num_villager):
    while num_werewolves != 0 and num_villager > num_werewolves:
        
        a = random.randint(1, num_werewolves + num_villager)
        if a > num_villager:
            num_werewolves -= 1
        else:
            num_villager -= 1

        
        num_villager -= 1

    if num_werewolves == 0:
        return 'village'
    else:
        return 'werewolves'



def odds_of_werewolves_winning(num_werewolves, num_villager):
    werewolves_win = 0
    time = 1000 
    for _ in range(1000):
        if find_winner(num_werewolves, num_villager)=='werewolves':
            werewolves_win += 1
    
    if werewolves_win == 0:
        while werewolves_win == 0:
            time += 1
            if find_winner(num_werewolves, num_villager)=='werewolves':
                werewolves_win += 1
    
    return werewolves_win * 1.00 / time


print("Do you want to find winner or find the odds of werewolves winning?"
      + "(Type in 'find winner' or 'odds of werewolves winning')")
ans = input()
num_werewolves = int(input("How many werewolves do you want to have in simulation? "))
num_villager = int(input("How many villagers do you want to have in simulation? "))

if ans == "find winner":
    print("The winner: " + find_winner(num_werewolves, num_villager) + "!")
elif ans == "odds of werewolves winning":
    print("The odds for werewolves to win is " + str(odds_of_werewolves_winning(num_werewolves, num_villager)))

"""
The following is answer for T11 part D.
The odd thing I noticed is that the odds for the werewolves to win is lower when the number if the villagers is odd
while the number of werewolves(even) remains constant. When the number of villagers is odd, the possibility for
werewolves to win is about 43%. When the number of villagers is even, the possibility for werewolves to win is
about 50%.

The following is answer for T11 part E, Question 2.
When the number of both werewolves and villagers is even, it's easier for the werewolves to win. This is because there
must be two players killed everyday, and when the werewolves win, the number of remaining players must be even.
(number of werewolves equal to number of villagers)
As a result, the werewolves need an extra day to survive and then win the game if the total number of players is odd,
and they will have a higher chance to be randomly killed by villagers as well. Thus, whether the total number of
players is odd or even affects the chances of winning in the game. When the number is odd, the werewolves have
less chances. When it is even, werewolves have more chances to win.
"""
