



from operator import itemgetter
import random

random.seed()

def create_deck():
    """
    Creates a standard deck of 52 playing cards.
    Each card is represented as a tuple [rank, suit].
    """
    deck = []
    for rank in range(1, 14):
        for suit in ['♠', '♥', '♦', '♣']:
            deck.append([suit, rank])
    return deck

def deal_hand(deck):
    
    
    random.shuffle(deck)
    
    return deck[:5]

'''
def is_full_house(hand):
    ranks = [0] * 15  # Initialize a list to store the count of each rank (Ace to King)
    
    for card in hand:
        ranks[card[0]] += 1
    
    flag1 = False
    flag2 = False
    for count in ranks:
        if count == 3:
            flag1 = True
        elif count == 2:
            flag2 = True
    
    return flag1 and flag2
'''
def is_full_house(hand):
    ranks=[]
    for i in range(20):
        ranks = ranks + [i]
    
    for i in range(0,14):
        ranks[i]=0
    
    for i in range(0,5):
        ranks[hand[i][1]]+=1
    flag1=False
    flag2=False
    for i in range(0,14):
        if ranks[i]==3:
            flag1=True
        if ranks[i]==2:
            flag2=True
    return (flag1 and flag2)

def full_house_simulation(num_simulations):
      
   
    
    full_house_count = 0
    deck = create_deck()
    for i in range(num_simulations):
        hand = deal_hand(deck)
        if is_full_house(hand):
            full_house_count += 1
    if full_house_count==0:
        print("The odds of being dealt a full house is 1 in {:.2f}".format(0))
        return
    odds = num_simulations / full_house_count
    print("The odds of being dealt a full house is 1 in {:.2f}".format(odds))

    
def is_straight_flush(hand):
    
   
    flag3 = True
    for i in range(0,4):
        if hand[i][0]!=hand[i+1][0]:
            flag3=False
    hand.sort()
    for i in range(0,4):
        if hand[i+1][1]!=hand[i][1]+1:
            
            flag3=False
            break
    return flag3            
            



def straight_flush_simulation(num_simulations):
    
    
    straight_flush_count = 0
    deck = create_deck()
    for i in range(num_simulations):
        hand = deal_hand(deck)
        if is_straight_flush(hand):
            straight_flush_count += 1

    odds = num_simulations *1.0 / straight_flush_count
    odds = str(odds)
    print("The odds of being dealt a straight flush is 1 in "+ odds)

def is_flush(hand):
    
    
    if is_straight_flush(hand):
        return False
    flag=True
    for i in range(0,4):
        if hand[i][0]!=hand[i+1][0]:
            flag=False
    return flag 

def flush_simulation(num_simulations):
    
    flush_count = 0
    deck = create_deck()
    for i in range(num_simulations):
        hand = deal_hand(deck)
        if is_flush(hand):
            flush_count += 1
    odds = num_simulations *1.0/flush_count
    odds = str(odds)
    print(f"The odds of being dealt a flush is 1 in "+ odds)

def flush_comparison_simulation(num_simulations):
    """
    Simulate rolling 5 four-sided dice and calculate the odds of getting the same suit on all five dice.
    Compare with the result from the Flush simulation.
    """
     
    flush_count = 0
    for _ in range(num_simulations):
        flag=True
        l=[1,2,3,4]
        random.shuffle(l)
        temp=l[0]
        for i in range(0,4):
            random.shuffle(l)
            if l[0]!=temp:
                flag=False
        if flag:
            flush_count += 1

    odds_flush_comparison =str( num_simulations*1.0 / flush_count)
     
    flush_count_flush_simulation = 0
    deck = create_deck()
    for i in range(num_simulations):
        hand = deal_hand(deck)
        if is_flush(hand):
            flush_count_flush_simulation += 1

    odds_flush_simulation =str( num_simulations *1.0 / flush_count_flush_simulation)

    print(f"The odds of rolling the same suit for all five dice is 1 in "+odds_flush_comparison)
    print(f"The odds of being dealt a flush is 1 in "+odds_flush_simulation)




