


import random
random.seed()



def generate_deck():
    
    deck = []

    for number in range(1, 14):
        for suit in ['♦', '♣', '♥','♠']:
            deck.append([number, suit])
            
    random.shuffle(deck)
    return deck

def full_house():

    
    deck = generate_deck()
    hand = deck[0:5]
    
    
    rank = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    rank.sort()

    
    
    if rank[2] == rank[1] or rank[3]:
        if rank[0] == rank[1]:
            if rank[3] == rank[4]:
                return True
        elif rank[3] == rank[4]:
            if rank[0] == rank[1]:
                return True
        else:
            return False

def full_house_average(num_trials):
    
    count_full_house = 0
    
    for i in range(num_trials):
        if full_house():
            count_full_house += 1
            
    
    probability_full_house_average = count_full_house/num_trials

    
    
    return print("A full house is a one in " + str(round(1/probability_full_house_average)))

def straight_flush():

    
    deck = generate_deck()
    hand = deck[0:5]

    
    if not (hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]):
        return False

    
    rank = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    rank.sort()
    if rank[4] == rank[0] + 4:
        return True

def straight_flush_average(number_of_straight_flushes):
    
    count_straight_flush = 0
    count_tries = 0

    
    while count_straight_flush < number_of_straight_flushes:
        if straight_flush():
            count_straight_flush += 1
        
        count_tries += 1

    
    
    probability_straight_flush_average = number_of_straight_flushes/count_tries

    
    
    return print("A straight flush is a one in " + str(round(1/probability_straight_flush_average)))

def flush():

    
    deck = generate_deck()
    hand = deck[0:5]

    
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return True
    return False

def flush_average(num_trials):
    
    count_flush = 0

    
    for i in range(num_trials):
        if flush():
            count_flush += 1

    
    probability_flush_average =  count_flush/num_trials

    
    
    return print("A flush is a one in " + str(round(1/probability_flush_average)))

def flush_comparison():

    
    suit_values = [random.choice(['♦', '♣', '♥','♠']), random.choice(['♦', '♣', '♥','♠'])\
                  ,random.choice(['♦', '♣', '♥','♠']), random.choice(['♦', '♣', '♥','♠'])\
                  ,random.choice(['♦', '♣', '♥','♠'])]

    
    suit_values.sort()
    if suit_values[0] == suit_values[4]:
        return True
    return False

def flush_comparison_average(num_trials):
    
    count_flush_comparison = 0

    
    for i in range(num_trials):
        if flush_comparison():
            count_flush_comparison += 1

    
    probability_flush_comparison_average = count_flush_comparison/num_trials

    
    
    print('The odds of a flush on dice is ' + str(round(1/probability_flush_comparison_average)))


full_house_trials = input("How many tests do you want to do to determine the probability"\
                    + " of a full house?(Type'No' if you're not interested)?")
straight_flush_trials = input("How many times do you want to get a straight flush in order"\
                    + " to determine the probability of a straight flush?"\
                    + "(Type'No' if you're not interested?)")
flush_trials = input("How many tests do you want to do to determine the probability"\
                    + " of a flush?(Type'No' if you're not interested)?")
flush_comparison_trials = input("How many tests do you want to do to determine the probability"\
                    + " of a full house if the suits are on dice?(Type'No' if you're not interested)?")


if full_house_trials != "No":
    full_house_average(int(full_house_trials))

if straight_flush_trials != "No":
    straight_flush_average(int(straight_flush_trials))

if flush_trials != "No":
    flush_average(int(flush_trials))

if flush_comparison_trials != "No":
    flush_comparison_average(int(flush_comparison_trials))


