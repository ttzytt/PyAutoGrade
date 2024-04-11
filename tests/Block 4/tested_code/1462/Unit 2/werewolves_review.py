




import random



def find_winner(num_werewolves, num_villager):

    
    people = []
    for i in range(num_werewolves):
        people.append('w')
    for i in range(num_villager):
        people.append('v')

    
    win = False
    while win == False:
        
        random.shuffle(people)
        people = people[1:]

        
        if people[0] == 'w':
            num_werewolves = num_werewolves - 1
        elif people[0] == 'v':
            num_villager = num_villager - 1

        if num_werewolves == 0:
            win = 'villagers'

        if num_werewolves == num_villager:
            win = 'werewolves'

        
        people.sort()
        people = people[1:]
        num_villager = num_villager - 1

        if num_werewolves == 0:
            win = 'villagers'

        if num_werewolves == num_villager:
            win = 'werewolves'

    return win



def odds_of_werewolves_winning(num_werewolves, num_villager):

    werewolf_win = 0
    
    for i in range(1000):
        win = find_winner(num_werewolves, num_villager)
        if win == 'werewolves':
            werewolf_win = werewolf_win + 1

    return (werewolf_win/1000)


num_werewolves = int(input("Number of werewolves: "))
num_villager = int(input("Number of villagers: "))
result = odds_of_werewolves_winning(num_werewolves, num_villager)
print("The odds of werewolves winning is " + str(result) + ".")



"""
Yes, I notice that when there are 4 werewolves and the number of villagers are odd,
The percentage of villagers winning would be higher when the number of villagers
are even.

(4, 99): 0.536
(4, 100): 0.566
(4, 101): 0.531

As the number of villagers increasing, the odds of werewolves winning should get
smaller. However, when there are 100 villagers, the odds are greater than when
there are 99 villagers.

"""



"""
1. Odd: About 151.
   Even: About 180.

2. If the total number of players is odd. The odd/even state of the werewolves and
   villagers would be different. When the werewolves win, the number of
   villagers equal to werewolves.
   
   - If the odd/even state of them are the same, then the only time that the villagers
   and the werewolves reach the same number is the night time, which means that a
   villager MUST get killed, which is not good.

   - If the odd/even state of them are different, then at day time they would reach the
   same odd/even state since one would get killed. Then, either werewolf/villager would
   get killed, which is better than only villager get killed in last round. In this way,
   it is possible for villagers would win. 

3. 1: 100
   2: 151
   3: 200
   
   Guess: The people might grow around 50 each time.

"""




      


        

