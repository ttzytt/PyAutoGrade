







from random import random, randint
from time import sleep



















def loop_index(index, total_width, offset):
    expected_index = index + offset
    if expected_index < 0:
        actual_index = total_width - 1 + expected_index
    elif expected_index > total_width - 1:
        actual_index = expected_index - total_width
    else:
        actual_index = expected_index
    return actual_index








def stream(target_width,total_width, speed):
    
    stream = ["☆"] * total_width
    
    
    target_end = randint(target_width-1, total_width-1)
    for i in range(target_width):
        stream[target_end-i] = "★"

    current_index = 0
    
    try:
        
        
        
        while True:
            if current_index < total_width - 1:
                current_index += 1
            else:
                current_index = 0
            
            stored = f"""                            |{stream[loop_index(current_index, total_width, -5)]}|
                            |{stream[loop_index(current_index, total_width, -4)]}|
                            |{stream[loop_index(current_index, total_width, -3)]}|
                            |{stream[loop_index(current_index, total_width, -2)]}|
                            |{stream[loop_index(current_index, total_width, -1)]}|   /
                            |{stream[loop_index(current_index, total_width, 0)]}|  <
                            |{stream[loop_index(current_index, total_width, 1)]}|   \\
                            |{stream[loop_index(current_index, total_width, 2)]}|
                            |{stream[loop_index(current_index, total_width, 3)]}|
                            |{stream[loop_index(current_index, total_width, 4)]}|
                            |{stream[loop_index(current_index, total_width, 5)]}|"""
            print(stored)
            sleep(speed)

    
    
    
    except KeyboardInterrupt:
        if stream[current_index] == "★":
            return True
        else:
            return False




def play_game(player_wager):
    player_winnings = player_wager
    difficulty = 0

    
    while difficulty <= 2:
        
        result = stream(difficulty_levels[difficulty][0], difficulty_levels[difficulty][1], difficulty_levels[difficulty][2])
        
        if result and difficulty <= 1:
            print()
            print("Wow, you've won!")
            
            print(f""" 
Would you like to potentially earn double?
If you win, you'll earn DOUBLE (${player_winnings * 2}).
However, if you lose, you'll lose your original wager as well as any previous earnings.
                """)
            
            continue_response = input("'Yes' or 'No': ").lower()
            if continue_response not in ['yes', 'no']:
                print("That's not a valid input.")
                continue_response = input("'Yes' or 'No': ").lower()
            
            if continue_response == 'yes':
                difficulty += 1
                player_winnings *= 2
            else:
                return player_winnings
        
        elif result and difficulty == 2:
            print("WOW!")
            return player_winnings
        
        else:
            print("Oops...")
            print("You've Lost!")
            return -(player_wager)

    
    if result:
        player_balance += player_winnings
        print(f"Wowsers, you've won {player_winnings}!")



difficulty_levels = [[3,12,0.07],[2,18,0.05],[1,24,0.03]]

player_balance = 100
continue_playing = True




print("""
      Welcome to Time Out!
      """)
print("""
      
      The goal of this game is to precisely choose the correct symbol.
      A stream of symbols will be going across the screen, and it's your job to catch the right symbol.
      
      """)

print("""

      While playing, your screen will look like this:

      |☆|
      |☆|
      |☆|
      |☆|
      |☆|
      |☆| <
      |★|
      |★|
      |★|
      |☆|
      |☆|
""")
print("""
      This stream of stars will continue cycling, and it's your job to stop it when a filled star is on the arrow.
      To stop the cycle, press Ctrl + C. 

      Warning: If you have that flashing light seizure thing maybe don't play this!
""")

print("Your balance is " + str(player_balance))

player_wager = int(input("\nPlace your wager: "))
while player_balance > 0 and continue_playing == True:
    
    while not player_balance >= int(player_wager) >= 1:
        if player_wager < 1:
            print("That's too low...")
            sleep(1)
            print("Wager a minimum of 1 dollar.")
            sleep(1)
        else:
            print("Your card's been declined...")
            
            print(f"You only have {player_balance} dollars.")
            print("Wager less...")
        player_wager = int(input("\nPlace your wager: "))
    print("Let's begin:")
    print("Remember, press [ Ctrl + C ] to stop...")
    sleep(2.5)

    player_balance += play_game(player_wager)

    print(f"Your current balance is {player_balance}.")
    
    if player_balance > 0:
        player_wager = input("Place your wager or type 'quit' to quit: ")
        if player_wager == 'quit':
            continue_playing = False
        else:
            player_wager = int(player_wager)


print("See you later :)")


    
