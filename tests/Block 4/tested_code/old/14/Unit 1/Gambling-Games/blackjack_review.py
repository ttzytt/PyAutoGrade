




from random import choice, random
from time import sleep

disable_sleep = True

def toggle_sleep(time):
    if not disable_sleep:
        sleep(time)


card_values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def card_values_to_number(x):
    if x == 'A':
        return 11
    elif x in ['J','Q','K']:
        return 10
    else:
        return int(x)




def hit_sum(arr):
     
    player_cards_values = list(map(card_values_to_number, arr))
        
    while True:
        if sum(player_cards_values) > 22:
            if 'A' in arr:
                if not player_cards_values.index(11) == -1:
                    player_cards_values[player_cards_values.index(11)] = 1
                else:
                    return -1
            else: 
                return -1
        elif sum(player_cards_values) == 22:
            return 0
        else:
            return sum(player_cards_values)
            
def algorithim_andy():
    andy_cards = [choice(card_values),choice(card_values)]
    
    
    while True:
        andy_sum = hit_sum(andy_cards)
        if andy_sum == 0:
            return andy_cards
        elif andy_sum == -1:
            return andy_cards
        elif andy_sum <= 11:
            
            andy_cards.append(choice(card_values))
        else:
            if random() >= 0.09 * (andy_sum - 11):
                
                andy_cards.append(choice(card_values))
            else:
                return andy_cards


player_balance = 100
continue_playing = True



print()

toggle_sleep(3)

print()

toggle_sleep(7)

print()

toggle_sleep(7)

print()

toggle_sleep(5)


print(f"Your balance is {player_balance} dollars")
player_wager = int(input("\nPlace your wager: "))
while player_balance > 0 and continue_playing == True:
    
    while not player_balance >= int(player_wager) >= 1:
        if player_wager < 1:
            print("That's too low...")
            toggle_sleep(1)
            print("Wager a minimum of 1 dollar.")
            toggle_sleep(1)
        else:
            print(f"You only have {player_balance} dollars")
            print("Wager less")
        player_wager = int(input("\nPlace your wager: "))

    
    print("\n(o^▽^o) Welcome, welcome to a round of Baker's Blackjack!")
    toggle_sleep(2)
    print("<(￣︶￣)> Here are your cards: ")
    toggle_sleep(1.5)
    
    player_cards = [choice(card_values), choice(card_values)]
    print(f)
    toggle_sleep(1.5)
    print(f)
    toggle_sleep(1.25)
    print(choice([
        "(￣_￣)・・・ Those cards are... intresting.",
        "ヽ(°〇°)ﾉ WOW!",
        " ᕕ( ᐛ )ᕗ It's go time :)",
        "〣( ºΔº )〣 Whaa...",
        "(─‿‿─) niceu cards",
        "ヽ(´ー` )┌ Eh",
        "(シ_ _)シ My condolences",
        "|д･) WHAT IS THAT ???",
        " __〆(￣ー￣ ) I'm bored of writing these..."
        ]))
    
    gambling_response = input("Would you like to 'Hit' or 'Stand': ")
    while not gambling_response.lower() in ['hit','stand']:
        print("That's not an option...")
        gambling_response = input("Would you like to 'Hit' or 'Stand': ")
    
    
    if gambling_response.lower() == 'hit':
        hit_continue = 'yes'
        while hit_continue.lower() in ['yes', 'hit']:
            print("(b ᵔ▽ᵔ)b Alrighty! Your next card is:")
            toggle_sleep(1)
            player_cards.append(choice(card_values))
            print(f)
            
            
            
            
            
            continue_hits = hit_sum(player_cards)
            if continue_hits >= 1:
                
                toggle_sleep(1)
                print(f"(*°▽°*) Looks like your cards reach a max value of {continue_hits}!")
                hit_continue = input("Would you like to draw another card? ('yes' or 'no') ")
            elif continue_hits == 0:
                
                toggle_sleep(1)
                print("＼(≧▽≦)／ BAKER'S BLACKJACK!!!")
                toggle_sleep(0.25)
                print("＼(≧▽≦)／ BAKER'S BLACKJACK!!!")
                toggle_sleep(0.25)
                print("＼(≧▽≦)／ BAKER'S BLACKJACK!!!")
                toggle_sleep(0.25)
                break
            else:
                
                print("／(≧ x ≦)＼ Uh oh...")
                toggle_sleep(1)
                print("\n(シ_ _)シ You've busted...")
                break
            
    
    print("\n(✧ω✧) Now let's see what I have...")
    
    andy_cards = algorithim_andy()
    toggle_sleep(2)
    print("(￢‿￢ ) My first two cards were:")
    toggle_sleep(1)
    print(f)
    toggle_sleep(1.5)
    print(f)
    
    if len(andy_cards) > 2:
        for i in range(2,len(andy_cards)):
            toggle_sleep(0.75)
            print("(つ✧ω✧)つ Then, I 'Hit' and got: ")
            toggle_sleep(0.5)
            print(f)
    andy_sum = hit_sum(andy_cards)
    player_sum = hit_sum(player_cards)
    
    if andy_sum == -1:
        print()
        toggle_sleep(0.5)
        print("(つ . •́ _ʖ •̀ .)つ Oh... ")
        toggle_sleep(0.75)
        print("(づ◡﹏◡)づ I busted...")

        if player_sum == -1:
            result = 'Tie'
        else:
            result = 'Player'

    elif andy_sum == 0:
        print()
        toggle_sleep(1.5)
        print("☆⌒(≧▽​° ) BAKER'S BLACKJACK")

        if player_sum == 0:
            result = 'Tie'
        else:
            result = 'Andy'
    else: 
        print()
        toggle_sleep(0.5)
        print(f"( ° ∀ ° )ﾉﾞI got a total of {andy_sum}")

        if player_sum == -1:
            result = 'Andy'
        elif player_sum == 0 or player_sum > andy_sum:
            result = 'Player'     
        elif player_sum < andy_sum:
            result = 'Andy'
        else:
            result = 'Tie'

    
    if result == 'Player':
        player_balance += player_wager
        print("\n⊂( ´ ▽ ` )⊃ Wow! Nice job")
        toggle_sleep(0.75)
        print("\n(づ◡﹏◡)づ You've bested me...")
        toggle_sleep(1)
        print("\n(つ≧▽≦)つ But it's all good! I have infinite money, after all...")
        toggle_sleep(2)
        print(f"\n(￣ω￣)/ You've earned {player_wager} dollars!")
        toggle_sleep(1)
    elif result == 'Andy':
        player_balance -= player_wager
        print("\n(づ￣ ³￣)づ Good game!")
        toggle_sleep(0.5)
        print("\n┐(︶▽︶)┌  I guess I'm just the best...")
        toggle_sleep(0.75)
        print("\n(///￣ ￣///) Just kidding!")
        toggle_sleep(0.75)
        print("\n(･ω<)☆ Maybe you can beat me next time.")
        toggle_sleep(1.25)
        print(f"\n\nYour new balance is {player_balance} dollars")
        toggle_sleep(1)
    else:
        print("\n(ಠ_ಠ) Looks like we tied!")
        toggle_sleep(0.75)
        print("\n乁( • ω •乁) Maybe we're equally skilled.")
        toggle_sleep(1)
        print("\n(￣^￣)ゞ Let's settle this next time!")
        toggle_sleep(1)
        print(f"\n\nYour balance of {player_balance} dollars will stay the same.")
        toggle_sleep(1)
    
    player_wager = input("Place your wager or type 'quit' to quit: ")
    if player_wager == 'quit':
        continue_playing = False
    else:
        player_wager = int(player_wager)

print(f"Your final balance is: {player_balance}")
print("See you later!")
