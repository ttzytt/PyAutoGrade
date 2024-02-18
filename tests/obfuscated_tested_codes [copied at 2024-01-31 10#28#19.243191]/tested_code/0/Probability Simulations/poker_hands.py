


import random
random.seed()


def generate_deck():
    deck = []
    for rank in range(1, 14):
        for suit in ['♠', '♥', '♦', '♣']:
            deck.append([rank, suit])
    return deck


def generate_hand():
    hand = generate_deck()
    random.shuffle(hand)
    hand = hand[0:5]
    return hand



def full_house():
    hand_ranks = generate_hand()
    hand_ranks = [hand_ranks[0][0], hand_ranks[1][0], hand_ranks[2][0], hand_ranks[3][0], hand_ranks[4][0]]
    hand_ranks.sort()
    if hand_ranks[0] == hand_ranks[1]:
        
        if hand_ranks[1] == hand_ranks[2]:
            if hand_ranks[3] == hand_ranks[4]:
                return True
        
        elif hand_ranks[2] == hand_ranks[3]:
            if hand_ranks[3] == hand_ranks[4]:
                return True
    return False
    


def straight_flush():
    hand_suits = generate_hand()
    hand_suits.sort()
    if not hand_suits[0][1] == hand_suits[1][1] == hand_suits[2][1] == hand_suits[3][1] == hand_suits[4][1]:
            return False
    hand_ranks = hand_suits
    straight_flush_counter = 0
    
    for i in range(4):
        if hand_ranks[i][0] + 1 == hand_ranks[i + 1][0]:
            straight_flush_counter += 1
        
    if straight_flush_counter == 4:
        return True
        

def flush():
    flush_suits = generate_hand()
    flush_suits.sort()
    if not flush_suits[0][1] == flush_suits[1][1] == flush_suits[2][1] == flush_suits[3][1] == flush_suits[4][1]:
        return False
    flush_ranks = flush_suits
    flush_counter = 0
    for i in range(4):
        if flush_ranks[i][0] + 1 == flush_ranks[i + 1][0]:
            flush_counter += 1

    if flush_counter == 4:
        return False
    
    return True
    





def flush_comparison():
    dice = [random.choice(['♠', '♥', '♦', '♣']), random.choice(['♠', '♥', '♦', '♣']), random.choice(['♠', '♥', '♦', '♣']), random.choice(['♠', '♥', '♦', '♣']), random.choice(['♠', '♥', '♦', '♣'])]
    dice_counter = 0
    
    for i in range(4):
        if dice[i] == dice[i + 1]:
            dice_counter += 1
            
    if dice_counter == 4:
        return True
    
    return False


def average_finder(target):
    returned_true = False
    times_ran = 0
    while returned_true == False:
        if target():
            returned_true = True
        times_ran += 1
    print('It took ' + str(times_ran) + ' runs before a ' + function_selection + ' occured.')



print('This finds the amount of times a specified function has to run until it becomes true.')
print('')
print('Please input a number 0 - 4 ( 0 = quit, 1 = full house, 2 = straight flush, 3 = flush, 4 = flush comparison )')
end_program = False
while end_program == False:
    function_selection = int(input('Which function would you like to test?'))

    if function_selection == 0:
        end_program = True
        
    elif function_selection == 1:
        function_selection = 'full house'
        target = full_house
        average_finder(target)

    elif function_selection == 2:
        function_selection = 'straight flush'
        target = straight_flush
        average_finder(target)

    elif function_selection == 3:
        function_selection = 'flush'
        target = flush
        average_finder(target)

    elif function_selection == 4:
        function_selection = 'flush comparison'
        target = flush_comparison
        average_finder(target)








