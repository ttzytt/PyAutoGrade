








import random
random.seed
def find_full_house(deck,trys):
	x = 0
	for i in range (trys):
		hand = []
		random.shuffle(deck)
		hand = deck[0:5]
		hand.sort()	
		if ((hand[0][0] == hand[1][0]) and (hand[3][0] == hand[4][0])): 
			if (hand[1][0] == hand[2][0]) or (hand[2][0] == hand[3][0]): 
				x += 1
	print ('The odds of being dealt a full house is 1 in',trys/x,)
	return (trys/x)


def find_straight_flush(deck,trys):
	x = 0
	for i in range (trys):
		hand = []
		random.shuffle(deck)
		hand = deck[0:5]
		hand.sort()
		
		if hand[0][1] == hand[1][1] == hand[2][1]== hand[3][1] == hand[4][1]:
                        
			if (hand[1][0] + 3) == ((hand[2][0])+2) == ((hand[3][0])+1) == (hand[4][0]):
                                
				if (((hand[0][0]) + 4) == ((hand[1][0]) + 3) or ((hand[0][0] == 1) and (hand[4][0] == 13))):
                                        
                                        
					x += 1		
	print ('The odds of being dealt a straight flush is 1 in', trys/x)
	return (trys/x)


def find_flush(deck,trys):
	x = 0
	for i in range(trys):
		hand = []
		random.shuffle(deck)
		hand = deck[0:5]
		hand.sort()
		if (hand[0][1] == hand[1][1] == hand[2][1]== hand[3][1] == hand[4][1]): 
			x += 1
	print ('The odds of being dealt a flush is 1 in ',trys/x)
	return (trys/x)


def flush_comparison(trys):
	dice = ['♠','♥','♦','♣']
	x = 0
	for i in range (trys):
		suits = []
		for i in range (5):
			random.shuffle(dice)
			suits.append(dice[0])
		if (suits[0] == suits[1] == suits[2]== suits[3] == suits[4]):
			x += 1
	print ('The odds of being dealt a flush comparison is 1 in',trys/x)
	return (trys/x)








deck = []
for rank in range(1, 14): 
        for suit in ['♠', '♥', '♦','♣']:
                deck.append([rank, suit])

trys = int(input('How many times you want to try: '))

find_full_house(deck,trys)
find_straight_flush(deck,trys)
find_flush(deck,trys)
flush_comparison(trys)

