






import random

random.seed()

money = 100 


print("Welcome to the gambling game!")
print("Game rule: You have 100 dollar at the start of the game."
      "In each time two dices with 30 sides will be thrown."
      "You will guess a number between 1 and 30."
      "If the number you guess is between the two numbers shown on the two dices,"
      "you win and get 10 dollar. Otherwize, you will lose 10 dollar. However,"
      "if the number you guess is the same with one of the numbers showed on the dices,"
      "you will lose 100 dollar at once.You will be out if you lose all your money."
      "You can quit the game at all time.")




whether_continue = 'Yes'

while whether_continue == 'Yes': 
    
    dice_1 = random.randint(1, 30)
    dice_2 = random.randint(1, 30)
    user_guess = input("Guess a number (Type 'quit' to end the game): ")

    if user_guess == 'quit':
        whether_continue = 'No'
        
    
    else:
        print ("Number showed on dice A: " + str(dice_1))
        print ("Number showed on dice B: " + str(dice_2))
        user_guess = int(user_guess)

        
        if user_guess < dice_1 and user_guess > dice_2:
            print('You win. You gain ten dollar!')
            money = money + 10
        
        elif user_guess > dice_1 and user_guess < dice_2:
            print('You win. You gain ten dollar!')
            money = money + 10
        
        elif user_guess == dice_1 or user_guess == dice_2:
            print('You are so unluky! You lose 100 dollar!')
            money = money - 100
        
        else:
            print('You lose. You lose ten dollar!')
            money = money - 10
        
    if money < 0:
        money = 0

    
    if money == 0:
        whether_continue = 'No'

    
    print('You now have ' + str(money) + ' dollar.')

    print() 


print('You are out!') 
print('End of the game.')
        
    
        


