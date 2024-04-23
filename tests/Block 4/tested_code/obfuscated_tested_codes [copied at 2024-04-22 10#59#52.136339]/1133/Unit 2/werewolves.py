


import random


def find_winner(num_werewolves, num_villagers):
    while num_werewolves > 0 and num_villagers > num_werewolves:
        
        if random.random() < num_villagers/(num_villagers+num_werewolves):
            num_villagers -= 1         
        else:
            num_werewolves -= 1
        num_villagers -= 1    

     return 'werewolves' if num_werewolves > 0 else 'village'


'''
通过一百万次（num_simulations = 1000000）的游戏模拟，该函数旨在达到统计上显著的样本量。
这大量的模拟有助于以高准确度逼近狼人获胜的真实概率。大数定律表明，随着试验次数的增加，
平均结果将更接近期望值。
1,000,000默认值的参数。这种方式提供了一个选项，允许调用者在需要时覆盖模拟次数，
如果他们没有指定不同的数字，函数将默认使用一百万次模拟

'''
def odds_of_werewolves_winning(num_werewolves, num_villagers, num_simulations=1000000):
    werewolves_won = 0
    for i in range(num_simulations):
        winner = find_winner(num_werewolves, num_villagers)
        if winner == 'werewolves':
            werewolves_won += 1
    return werewolves_won / num_simulations

'''
允许灵活性。这意味着在调用函数时，如果需要，可以指定不同数量的模拟次数，而无需更改函数的代码。
这在需要快速测试少量模拟或进行更广泛测试与更多模拟的场景中非常有用。
这意味着每次调用此函数时，它都会运行一百万次模拟，不提供给调用者指定不同模拟次数的选项
。这种方式简化了函数的签名，但减少了灵活性。
'''
def odds_of_werewolves_winning(num_werewolves, num_villagers):
    num_simulations = 1000000
    werewolves_won = 0
    for i in range(num_simulations):
        winner = find_winner(num_werewolves, num_villagers)
        if winner == 'werewolves':
            werewolves_won += 1
    return werewolves_won / num_simulations





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
















