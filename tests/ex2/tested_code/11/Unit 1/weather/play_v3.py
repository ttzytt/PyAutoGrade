


import random
import time


hangman_words = ["silly","smelly","pneumonoultramicroscopicsilicovolcanoconiosis", "orange", "v"]


tempature_fahrenheit = int(input("What is the tempature today (in °F)? "))


def worthy(tempature):
    
    print("I see you're trying to foolishly go outside in these TERRIBLE conditions.")
    time.sleep(1)
    print("I can't stop you- it's a free country- but I can test if you're worthy.")
    time.sleep(1)
    print("Beat me in hangman.")
    time.sleep(1)

    

    hangman_win = False
    failed_attempts = 0
    target_word = hangman_words[random.randint(0,len(hangman_words)-1)]
    filled_in_word = ["_"] * len(target_word)

    
    print(" ".join(filled_in_word))
    
    while failed_attempts < 9:

        
        if "_" not in filled_in_word:
            hangman_win = True
            break

    
        guess = input("\nGuess a letter: ")
        
        if guess not in "abcdefghjiklmnopqrstuvwxyz" or len(guess) != 1:
            print("That's not a valid guess. +1 wrong guess.")
            failed_attempts += 1
        else:
            
            for i in range(len(target_word)):
                if target_word[i] == guess:
                    filled_in_word[i] = guess
            print(" ".join(filled_in_word))
            
            if guess not in target_word:
                print("\nNothing, huh. This isn't looking too good.")
                failed_attempts += 1
    
    time.sleep(1)
    
    if hangman_win:
        print("Wow! You actually did it.")
        time.sleep(1)
        print("Feel free to go to wherever you want I guess.")
        time.sleep(1)
        print("Because I'm sure that hangman is a great test of toughness in extreme climates.")
        time.sleep(1)
        print("Good job!")
        return True; 
    else:
        
        print("\n You aren't ready...")
        return False
    

    




if tempature_fahrenheit > 95 or tempature_fahrenheit <= 32:
    worthy(tempature_fahrenheit)
    
else:
    
    
    
    
    if tempature_fahrenheit > 50:
        jacket_needed = input("Is it raining? ")
    else:
        jacket_needed = "yes"

    
    if jacket_needed.lower() == "yes":
        
        jacket_response = input("Do you have a jacket? ")

        
        
        if jacket_response.lower() == "yes":
            print("You should play outside today.")
        else:
            worthy(tempature_fahrenheit)

    
    else:
        print("You should play outside today.")


