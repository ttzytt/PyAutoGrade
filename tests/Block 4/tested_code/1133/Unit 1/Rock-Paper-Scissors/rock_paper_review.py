




import random


userchoice = input("Enter 'rock' or 'paper': ").lower()


ranchoice = random.choice(['rock', 'paper'])


print("I choose " + ranchoice + ".")


if userchoice == ranchoice:
    print("We tie.")  
elif (userchoice == 'rock' and ranchoice == 'paper'):
    print("You win")  
elif (userchoice == 'paper' and ranchoice == 'rock'):
    print("You win.")  
else:
    print("I win.")  
