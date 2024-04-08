


import random

random.seed()


print("Hello, would you like to play a game of cards?")
print("You will start off with 100$")
print("Each time you win you will get 2x the money you put in.")
print()


response = 'yes'
original_amount = int(100)



while response == 'yes' or new_response == 'no':
    
    card_value = random.randint(1,13)
    player = card_value

    card_type = random.choice(['Hearts', 'Spades', 'Diamonds', 'Clubs'])
    new_response = 'yes'

    bet_amount = int(input("How much do you want to bet? "))

    print("Your card is the " + str(card_value) + " of " + card_type + "'s.")

    card_type = random.choice(['Hearts', 'Spades', 'Diamonds', 'Clubs'])
    card_value = random.randint(1,13)
    computer = card_value

    print("I choose the " + str(card_value) + " of " + card_type + "'s.")

    
    
    new_amount = int(bet_amount * 2) + int(original_amount - bet_amount)

    
    if player > computer:
        print("Nice! You won!")
        print("Your new total is " + str(new_amount) + "!")
        original_amount = new_amount

    elif player < computer:
        print("You lost, rip")
        if original_amount - bet_amount <= 0:
            print("I won.")
            print("Your broke bring more money next time.")
            win_lose = 1
        print("Your new total is " + str(original_amount - bet_amount) + ".")
        original_amount = original_amount - bet_amount
        

    elif player == computer:
        print("We tie, better luck next time.")
        print("Your amount is still " + str(original_amount) + ".")

    print()
    
    if original_amount - bet_amount >= 0:      
        response = input("Do you want to play again? Yes or no (all lowercase, no spaces) ")
    elif original_amount - bet_amount <= 0:
        response = 'no'
    
print("I'm sad to see you go, come back soon!")





