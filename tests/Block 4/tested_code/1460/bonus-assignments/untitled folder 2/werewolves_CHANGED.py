




from random import randint
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          





def find_winner(num_werewolves, num_villager):
    is_day = True
    while num_werewolves < num_villager and num_werewolves > 0:
        if is_day: 
            if randint(1, num_werewolves + num_villager) <= num_werewolves:
                
                num_werewolves -= 1
            else:
                num_villager -= 1
        else: 
            num_villager -= 1
        is_day = not is_day 
    if num_werewolves > 0:
        return 'werewolves'
    return 'village'

def odds_of_werewolves_winning(num_werewolves, num_villager, tries = 100):
    werewolves_wins = 0
    for _ in range(tries):
        if find_winner(num_werewolves, num_villager) == 'werewolves':
            werewolves_wins += 1
    return werewolves_wins / tries


while True:
    werewolves = input("Number of Werewolves: ")
    if not werewolves.isnumeric(): 
        print("not a number")
        werewolves = input("Number of Werewolves: ")
    werewolves = int(werewolves)
    villagers = input("Number of Villagers: ")
    if not villagers.isnumeric():
        print("not a number")
        villagers = input("Number of Villagers: ")
    villagers = int(villagers)
    tries = input("Number of Tries: ")
    if not tries.isnumeric():
        print("not a number")
        tries = input("Number of Tries: ")
    tries = int(tries)

    odds = odds_of_werewolves_winning(werewolves, villagers, tries)
    print("Odd of werewolves winning with", werewolves,
          "werewolves and", villagers, "villagers is",
          round(odds,4), "(",round(odds*100,2) ,"% )")
















'''
Q2

It is preferred for the # of total players to be odd.

Let the number of werewolves be x. Note that the werewolves
win when the total number of players is equal or less than 2x.

When each Day and Night passes, during the Day either one werewolf
or one villager is lost. During the night, one village is lost.

Either way, the village loses 2 people. As such, after each day and
night cycle, the parity of the total number of people will not change.

Let's compare an odd and even starting number.

Let's first assume the starting number of people is even, 2k.
Each day and night, this total will decrease by 2 until eventually
reaching exactly 2x. For example, if our starting number was 8 and
there was 1 werewolf, we would have a total of 8, 6, 4, until
reaching 2.

This does assume that no werewolf gets voted out, but note that even
if a werewolf does get voted out, 2x is still an even number.

Let's now assume the starting number of people is odd, 2k+1.
Likewise, the total will decrease by 2 every day and night cycle.
However, it will never reach exactly 2x, since an odd number
subtracted by an even number will never be even. Therefore, the game
only ends when we reach 2x - 1. For example, if our starting number
was 7 and there was 1 werewolf, we would have a total of 7, 5,
3, until reaching 1 (which is less than 2).

Note that even though we have a less total number of people (8 vs 7),
the number of cycles (day and nights) needed to have the werewolves
win is the same, 3.

This may lead to the inference that the chance of werewolves winning
given a consecuitve odd and even number is the same, but if you were
to actually calculate the chance of werewolves winning, it would reveal
something a bit bigger...

Let's assume that werewolves don't get voted out.
Then, the chance of werewolves winning is the chance that anyone else
(the villagers) get voted out each round until the final round.

So, the chance that a werewolf wins is:

Starting with 8:
(8 - 1)/8 * (6 - 1)/6 * (4 - 1)/4 

vs

Starting with 7:
(7 - 1)/7 * (5 - 1)/5 * (3 - 1)/3

Now, notice that:
(8 - 1)/8 > (7 - 1)/7,
(6 - 1)/6 > (5 - 1)/5,
(4 - 1)/4 > (3 - 1)/3

Therefore:
(8 - 1)/8 * (6 - 1)/6 * (4 - 1)/4 > (7 - 1)/7 * (5 - 1)/5 * (3 - 1)/3.
So the chance the werewolf wins is actually larger on 8 than it is on
7.

Note that as the total number increases, the number of factors that
get multiplied increases, making each chance closer to 0 and therefore
making the absolute difference between 2k and 2k+1 for larger numbers
near nothing.

This was also assuming that the werewolves can't get voted out. However, note
that if the werewolves could get voted out, the chance that there is for
a werewolf to get voted out is less when there's more total people. Therefore,
the chance that the werewolves win is still intuitively greater on 8 than
it is on 7. Also, when a werewolf gets voted out, it just adds one more cycle,
no matter if starting from an odd or even (given they're consecutive), so
the impact it has aligns with the pattern we already noticed.

Therefore, the villagers prefer odd numbers.
'''