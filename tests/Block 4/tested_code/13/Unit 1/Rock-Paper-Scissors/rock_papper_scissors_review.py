




import random


user_choise = input("Enter 'rock', 'paper', or 'scissors' in lower case: ")


random_chiose = random.choice(['rock', 'paper', 'scissors'])


print("I choose " + random_chiose + '.')


if user_choise == random_chiose:
    print("We tie.")  

elif (user_chiose == 'rock' and random_chiose == 'paper') or (user_choise == 'paper' and random_chiose == 'scissors') or (user_choise == 'scissors' and random_chiose == 'rock'):
    print("You win")  

else:
    print('I win')  
