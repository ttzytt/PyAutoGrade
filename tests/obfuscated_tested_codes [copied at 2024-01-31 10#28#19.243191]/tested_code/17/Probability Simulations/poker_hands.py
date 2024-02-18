





import random
random.seed()


def make_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = [] 
    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit]) 
    return deck


    

def full_house_odds(num_trials):
    deck = make_deck()
    full_house_count = 0 

    for trial in range(num_trials): 
        random.shuffle(deck)
        hand = deck[:5]

        
        ranks = [card[0] for card in hand] 
        unique_ranks = set(ranks) 

        if len(unique_ranks) == 2: 
                                   

            for rank in unique_ranks:

                
                count_ranks = sum(card[0] == rank for card in hand) 
                if (count_ranks == 3 or count_ranks == 2): 

                    full_house_count += 1 
                    
                    break 
                          
                            

    if full_house_count == 0: 
        return 0
     
    chances = num_trials/full_house_count 
    return chances




def straight_flush_odds(num_trials):
    deck = make_deck()
    straight_flush_count = 0

    for trial in range(num_trials): 
        random.shuffle(deck)
        hand = deck[:5]

        
        ranks = [card[0] for card in hand] 
        ranks.sort() 
                     

        suits = [card[1] for card in hand]
        unique_suits = set(suits) 

        if len(unique_suits) == 1: 
            
            if ranks[0] == 1 and ranks[-1] == 13:
                ranks[0] = 14
                ranks.sort() 
                
            for i in range(len(ranks) - 1):
                straight_flush_count += 1 
                if ranks[i] != ranks[i + 1] - 1: 
                    straight_flush_count -= 1
                    break
                

    if straight_flush_count == 0: 
        return 0
     
    chances = num_trials/straight_flush_count 
    return chances 




def flush_odds(num_trials):
    deck = make_deck()
    flush_count = 0

    for i in range(num_trials): 
        random.shuffle(deck)
        hand = deck[:5]
        
      
        suits = [card[1] for card in hand]
        unique_suits = set(suits) 

        if len(unique_suits) == 1:
            flush_count += 1 
        
        
    if flush_count == 0: 
        return 0

    chances = num_trials / flush_count 
    return chances




def same_suit_odds(num_trials):
    same_suit_count = 0
    
    for trial in range(num_trials): 
        rolls = []
        
        for i in range(5):
            rolls.append(random.choice([1, 2, 3, 4])) 
        rolls.sort()
        
        if rolls[0] == rolls[4]: 
            same_suit_count += 1

        

    if same_suit_count == 0:  
        return 0
        

    chances = num_trials / same_suit_count 
    return chances
    

    



num_trials = int(input("Enter the number of trials: "))

chances_fho = full_house_odds(num_trials) 
print(f"The chances of getting a full house are approximately 1 in {chances_fho:.3f}")

chances_sfo = straight_flush_odds(num_trials) 
print(f"The chances of getting a straight flush are approximately 1 in {chances_sfo:.3f}")

chances_fo = flush_odds(num_trials) 
print(f"The chances of getting a flush are approximately 1 in {chances_fo:.3f}")

chances_sso = same_suit_odds(num_trials) 
print(f"The chances of getting all five die to roll the same suit are approximately 1 in {chances_sso:.3f}")








