



from card_functions import *
import random

random.seed()

card = []

user_choice = input('Choose a card  with number between 1 to 21 (included): ')
print("I'm going to guess the card you have just chosen!")
print()
for i in range(1, 22):
    card.append(i)
random.shuffle(card) 

for i in range(3):
    hands = deal_3_hands(card)

    
    print('First hand: ' + str(hands[0]))
    print('Second hand: ' + str(hands[1]))
    print('Third hand: ' + str(hands[2]))
    user_choice = input('In which hand stays the card you chose (Enter "First", "Second" or "Third"): ')
    print()
    
    if user_choice == 'First':
        temp_store = hands[1]
        hands[1] = hands[0]
        hands[0] = temp_store

    if user_choice == 'Third':
        temp_store = hands[1]
        hands[1] = hands[2]
        hands[2] = temp_store

    
    card = []
    for j in range(3):
        for _ in range(7):
            
            card.append((hands[j])[_])

if user_choice == card[10]:
    print('Aha! The card you chose is ' + str(card[10]) + '!') 
    
else: 
    print('I bet you have been lying just now!')
    
    
    
    

