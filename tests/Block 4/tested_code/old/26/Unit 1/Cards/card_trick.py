


from card_functions import *
import random
random.seed()

Cards_total = ['2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♠','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♥','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♦','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♣']

Cards_21 = []

for i in range(0,21):
    j = random.randint(0,51)
    
    while Cards_total[j] in Cards_21:
        j = random.randint(0,51)
    Cards_21.append(Cards_total[j])

Cards_1 = deal_3_hands(Cards_21)

print("Here's 3 decks of cards.")
print("Choose a card from these three decks.")
print("Deck 1")
print(Cards_1[0])
print("Deck 2")
print(Cards_1[1])
print("Deck 3")
print(Cards_1[2])

signal_number_1 = int(input('Tell me which deck is your card in, (by typing 1,2 or 3): '))-1
print()



Cards_21 = Cards_1[0]+Cards_1[1]+Cards_1[2]

Cards_2 = deal_3_hands(Cards_21)

print("Here's 3 decks of cards.")
print("Deck 1")
print(Cards_2[0])
print("Deck 2")
print(Cards_2[1])
print("Deck 3")
print(Cards_2[2])

signal_number_2 = int(input('Tell me which deck is your card in, (by typing 1,2 or 3): '))-1
print()



Cards_21 = Cards_2[0]+Cards_2[1]+Cards_2[2]

Cards_3 = deal_3_hands(Cards_21)


print("Here's 3 decks of cards.")
print("Deck 1")
print(Cards_3[0])
print("Deck 2")
print(Cards_3[1])
print("Deck 3")
print(Cards_3[2])


signal_number_3 = int(input('Tell me which deck is your card in, (by typing 1,2 or 3): '))-1


for i in range(21):
    if Cards_21[i] in Cards_1[signal_number_1] and Cards_21[i] in Cards_2[signal_number_2] and Cards_21[i] in Cards_3[signal_number_3]:
        print(Cards_21[i])


