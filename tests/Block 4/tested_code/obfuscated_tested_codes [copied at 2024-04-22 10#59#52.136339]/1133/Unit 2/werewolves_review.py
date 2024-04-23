



import random


def find_winner(num_werewolves, num_villagers):
    while num_werewolves > 0 and num_villagers > num_werewolves:
        
        if random.random() < num_villagers*1.0/(num_villagers+num_werewolves): 
            num_villagers -= 1 
        
        else:
            num_werewolves -= 1
        num_villagers -= 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

    return 'werewolves' if num_werewolves > 0 else 'village'



def odds_of_werewolves_winning(num_werewolves, num_villagers, num_simulations=1000000):
    werewolves_won = 0
    for i in range(num_simulations):
        winner = find_winner(num_werewolves, num_villagers)
        if winner == 'werewolves':
            werewolves_won += 1
    return werewolves_won / num_simulations



if __name__ == "__main__":
    num_werewolves = int(input("Enter the number of werewolves: "))
    num_villagers = int(input("Enter the number of villagers: "))

    result = find_winner(num_werewolves, num_villagers)
    print("The winner is:"+ result)

    odds = odds_of_werewolves_winning(num_werewolves, num_villagers)
    print("Odds of werewolves winning: " + str(round(odds, 2)))







'''
Enter the number of werewolves: 2
Enter the number of villagers: 15
The winner is: village
 
Enter the number of werewolves: 2
Enter the number of villagers: 13
The winner is: werewolves
 
Enter the number of werewolves: 2
Enter the number of villagers: 14
The winner is: werewolves
 
Enter the number of werewolves: 2
Enter the number of villagers: 16
The winner is: werewolves
Odds of werewolves winning: 63.15%
 
Enter the number of werewolves: 2
Enter the number of villagers: 20
The winner is: werewolves
Odds of werewolves winning: 58.19%
 
Enter the number of werewolves: 2
Enter the number of villagers: 26
The winner is: werewolves
Odds of werewolves winning: 52.68%
 
Enter the number of werewolves: 2
Enter the number of villagers: 28
The winner is: werewolves
Odds of werewolves winning: 51.09%
 
Enter the number of werewolves: 2
Enter the number of villagers: 30
The winner is: village
Odds of werewolves winning: 49.77%
'''
















