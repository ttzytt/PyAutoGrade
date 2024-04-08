







from operator import itemgetter  
import random  
random.seed()



number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
color = ['♠', '♥', '♦', '♣']
deck = []
for rank in range(13):
    for suit in range(4):
        deck.append([number[rank], color[suit]])



def random_five_hand():
    random.shuffle(deck)
    hands = deck[:5]
    return hands




def full_house():
    count = 0
    tries = 200000
    
    for _ in range(tries):
        hand = random_five_hand()
        
        hand.sort(key = itemgetter(0))

        
        if hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0] and hand[0][0] != hand[4][0]:
            if hand[1][0] == hand[2][0] or hand[2][0] == hand[3][0]:
                count = count + 1
    
    result = round(tries / count)
    return result





def is_straight_flush(hand):

    
        hand.sort(key = itemgetter(1, 0))
        if hand[0][1] == hand[4][1]:

            
            if hand[4][0] - hand[0][0] == 4:
                return True
            
            elif hand[0][0] == 1 and hand[1][0] == 10 and hand[4][0] == 13:
                return True
            else:
                return False
        return False
    
def straight_flush():
    count = 0
    tries = 500000
    
    for _ in range(tries):
        hand = random_five_hand()
        
        if is_straight_flush(hand) == True:
                count = count + 1

    result = round(tries / count)
    return result




def flush():
    count = 0
    tries = 200000
    
    for _ in range(tries):
        hand = random_five_hand()

        
        hand.sort(key = itemgetter(1, 0))

        
        if hand[0][1] == hand[4][1]:
    
            
            if hand[4][0] - hand[0][0] != 4:
                
                if [hand[0][0], hand[1][0], hand[2][0]] != [1, 10, 13]:

                    count = count + 1
    
    result = round(tries / count)
    return result




 
def same_suit_dice():
    count = 0
    tries = 100000

    for _ in range(tries):
        
        dice = ['♠', '♥', '♦', '♣']
        dice_hand = []
    
        for _ in range(5):
            random.shuffle(dice)
            dice_hand.append(dice[0])

        
        dice_hand.sort()
        if dice_hand[0] == dice_hand[4]:
            count = count + 1

    result = round(tries / count)
    return result




check = input('You can check the odds of Full House, Straight Flush, Flush, and Five Dice'
              ' return the one you want to check (capitalize first letter of each word): ')
if check == 'Full House':
    odds = full_house()
elif check == 'Straight Flush':
    odds = straight_flush()
elif check == 'Flush':
    odds = flush()
else:
    odds = same_suit_dice()

print('The odds of being dealt a ' + str(check) + ' is 1 in ' + str(odds) + '.')


    








        
        


    
