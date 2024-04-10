


import random
random.seed()





def one_deal():
    deal = deck[0:5]
    deal.sort()
    
    if deal[0][0] == deal[1][0] and deal[3][0] == deal[4][0]:
        if deal[2][0] == deal[1][0] or deal[2][0] == deal[3][0]:
            count += 1


deck = []

for rank in range(1,14):
    for suit in ['♠', '♥', '♦', '♣']:
        deck.append([rank, suit])

random.shuffle(deck)

deal = []
count = 0

num_simulation = input('How many times of simulation would you like to do? ')

for i in range(int(num_simulation)):
    one_deal()

print('You did ' + str(num_simulation) + ' times of simulation.')
print('Full house appeared ' + str(count) + ' time(s).')
