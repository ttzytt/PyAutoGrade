


'''
This program is a modded version of blackjack, the card will be randomly
choosed from 1-11, the goal for the user is to have cards bigger than the
other party.


The program is rigged, in the first two rounds, it be in easy mode, the 
user have a very big chance to win. After that, the program will go into 
harder, this way, the user's chance to win is greatly lowered.
'''

"""
The card number of the cheat program is stored in user_number_cheat_1 or 2
The card number of the computer in cheat
 program is stored in computer_number_cheat_1 or 2


The card number of the user in hard program is 
stored in user_number_hard_1 or 2

The card number of the computer in hard program is 
stored in computer_number_hard_1 or 2
"""


print ('''This program is a modded version of blackjack, the card will be randomly
choosed from 1-11, the goal for the user is to have cards bigger than the
other party. Push means that it's a tie between the 2 parties''')
import random
random.seed()
money = 1000
play_count = 0
loop = "continue"

print("You have 1000 dollars by default.")

while loop != "quit":
    if money <= 0:
        print("You have no money, you can't play anymore")
        break
    Play_money = int(input("How much money do you want to play: "))

    if play_count<3 :
 
        user_number_cheat_1 = random.randint(4, 11)
        user_number_cheat_2 = random.randint(5, 10)

        computer_number_cheat_1= random.randint(1, 5)
        computer_number_cheat_2 = random.randint(1, 4)


        if (user_number_cheat_1 + user_number_cheat_2 ==
            computer_number_cheat_1 + computer_number_cheat_2):
            print("The first card you have is: " + str(user_number_cheat_1))
            print("The second card you have is: " + str(user_number_cheat_2))
            print("The first card I have is: " + str(computer_number_cheat_1))
            print("The second card I have is: " + str(computer_number_cheat_2))
            print("Push")
            print()
        elif (user_number_cheat_1 + user_number_cheat_2 >
              computer_number_cheat_1 + computer_number_cheat_2):
            print("The first card you have is: " + str(user_number_cheat_1))
            print("The second card you have is: " + str(user_number_cheat_2))
            print("The first card I have is: " + str(computer_number_cheat_1))
            print("The second card I have is: " + str(computer_number_cheat_2))
            print("You win")
            print()
            money = Play_money + money
        else:
            print("The first card you have is: " + str(user_number_cheat_1))
            print("The second card you have is: " + str(user_number_cheat_2))
            print("The first card I have is: " + str(computer_number_cheat_1))
            print("The second card I have is: " + str(computer_number_cheat_2))
            print("I win")
            print()
            money = money - Play_money
        play_count = play_count + 2
 



    else:
        user_number_hard_1 = random.randint(1, 8)
        user_number_hard_2 = random.randint(1, 9)
        computer_number_hard_1= random.randint(5, 10)
        computer_number_hard_2 = random.randint(5, 11)
  
        if (user_number_hard_1 + user_number_hard_2 ==
            computer_number_hard_1 + computer_number_hard_2):
            print("The first card you have is: " + str(user_number_hard_1))
            print("The second card you have is: " + str(user_number_hard_2))
            print("The first card I have is: " + str(computer_number_hard_1))
            print("The second card I have is: " + str(computer_number_hard_2))
            print("Push")
            print()
        elif (user_number_hard_1 + user_number_hard_2 >
              computer_number_hard_1 + computer_number_hard_2):
            print("The first card you have is: " + str(user_number_hard_1))
            print("The second card you have is: " + str(user_number_hard_2))
            print("The first card I have is: " + str(computer_number_hard_1))
            print("The second card I have is: " + str(computer_number_hard_2))
            print("You win")
            print()
            money = Play_money + money
        else:
            print("The first card you have is: " + str(user_number_hard_1))
            print("The second card you have is: " + str(user_number_hard_2))
            print("The first card I have is: " + str(computer_number_hard_1))
            print("The second card I have is: " + str(computer_number_hard_2))
            print("I win")
            print()
            money = money - Play_money
    print("Currently you have " + str(money) + " dollars")
    loop = input("Do you want to continue? Enter quit or anything else " )

