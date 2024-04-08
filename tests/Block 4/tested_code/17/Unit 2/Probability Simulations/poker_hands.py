





import random
random.seed()


def build_deck(deck):
    for i in range(1,14):
        for j in range(1,5):
            deck.append([i,j])

def full_house(trials):
    num_full_houses=0
    deck=[]
    build_deck(deck)
    
    for _ in range(trials):
        
        random.shuffle(deck) 
        random_cards=[0,0,0,0,0]
        for i in range(5):
            random_cards[i] = deck[i][0] 
        
        random_cards.sort()
        if random_cards[0] == random_cards[1] == random_cards[2] and random_cards[3] == random_cards[4]:
            num_full_houses += 1
        if random_cards[2] == random_cards[3] == random_cards[4] and random_cards[0] == random_cards[1]:
            num_full_houses += 1
            
    return trials / num_full_houses * 1.0000 

def straight_flush(trials):
    num_straight_flushes = 0
    deck=[]
    build_deck(deck)

    for _ in range(trials):
        num_straight_flushes += check_straight_flush(deck)

    
    
    if num_straight_flushes == 0:
        while num_straight_flushes == 0:
            num_straight_flushes += check_straight_flush(deck)
            trials += 1

    return trials / num_straight_flushes * 1.0000 




def check_straight_flush(deck):
    random.shuffle(deck) 
    random_cards=[0,0,0,0,0]
    if not(deck[0][1]==deck[1][1]==deck[2][1]==deck[3][1]==deck[4][1]):
            return 0
    else:
        for i in range(5):
            random_cards[i] = deck[i][0]
                
        random_cards.sort()
            
        if random_cards[0] !=1:
            for i in range(4):
                if random_cards[i+1]-random_cards[i] != 1:
                    return 0
            return 1
        else:
            if random_cards[1]!=2:
                random_cards[0]=14
                random_cards.sort()
            for i in range(4):
                if random_cards[i+1]-random_cards[i] != 1:
                    return 0
            return 1
    return 0

def check_flush(deck):
    random.shuffle(deck) 
    random_cards=[0,0,0,0,0]
    if deck[0][1]==deck[1][1]==deck[2][1]==deck[3][1]==deck[4][1]:
        if check_straight_flush(deck)==0:
            return 1
    
    return 0

def flush(trials):
    num_flushes = 0
    deck = []
    build_deck(deck)

    for _ in range(trials):
        num_flushes += check_flush(deck)

    if num_flushes == 0:
        while num_flushes == 0:
            num_flushes += check_flush(deck)
            trials += 1

    return trials / num_flushes * 1.0000 



def flush_comparison(trials):
    num_diceflush = 0
    temp = trials
    for _ in range(trials):
        deck = [0, 0, 0, 0, 0]
        for i in range(5):
            deck[i] = random.randint(1,4)
        if deck[0] == deck[1] == deck[2] == deck[3] == deck[4]:
            num_diceflush += 1

    if num_diceflush == 0:
        while num_diceflush == 0:
            deck = []
            for _ in range(5):
                deck.append(random.randint(1,4))
            if deck[0] == deck[1] == deck[2] == deck[3] == deck[4]:
                num_diceflush += 1
            trials += 1
    
    return num_diceflush


type_poker = input("What type of simulation do you want to have? (Enter 'full house', 'straight flush','flush', or 'flush comparison') ")

if type_poker == "full house" or type_poker == "straight flush" or type_poker == "flush" :
    num_trials = int(input("How many trials do you want to have?"))
    if type_poker == "full house":
        odds = full_house(num_trials)
    if type_poker == "straight flush":
        odds = straight_flush(num_trials)
    if type_poker == "flush":
        odds = flush(num_trials)
    print("The odds of  being dealt a " + type_poker + " is 1 in " + str(odds))

elif type_poker == "flush comparison":
    num_trials = int(input("How many trials do you want to have? "))
    
    dice = flush_comparison(num_trials)
    pokers = num_trials/flush(num_trials) + num_trials/straight_flush(num_trials)
    
    print("The odds of all five dice to have the same suit is 1 in " + str(num_trials*1.0/dice))
    print("The odds of  being dealt all kinds of flushes is 1 in " + str(num_trials*1.0/pokers))
    if dice>pokers:
        print("As the result, the odds of all five dice to have the same suit is higher than the odds of  being dealt all kinds of flushes.")
    else:
        print("As the result, the odds of all five dice to have the same suit is lower than the odds of  being dealt all kinds of flushes.")

else:
    
    print("Please enter 'full house', 'straight flush','flush', or 'flush comparison'!")

 
