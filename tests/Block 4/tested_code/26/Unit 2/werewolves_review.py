import random
random.seed()



def find_winner(num_wolves,num_villager):
    
    
    

    
    for i in range(num_villager):

        
        temp = num_wolves+num_villager
        x = random.randint(0,temp)
        if x <= num_villager:
            num_villager -= 1
        else:
            num_wolves -= 1

        
        
        if num_wolves == 0:
            return 'villager'
        if num_villager == num_wolves:
            return 'werewolves'
        
        num_villager -= 1
        if num_wolves == 0:
            return 'villager'
        if num_villager == num_wolves:
            return 'werewolves'


def odds_of_werewolves_winning(num_werewolves, num_villager, nums = 100000):
    
    records = []
    for i in range(nums):
        if find_winner(num_werewolves, num_villager) == 'werewolves':
            records.append(1)
    return sum(records)/nums

wolves = int(input("wolves_number: "))
villager = int(input("villager_number: "))
print('The odds of werewolves wining is ' + str(odds_of_werewolves_winning(wolves, villager)))









