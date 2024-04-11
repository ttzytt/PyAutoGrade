








def deal_3_hands(deck):

    
    hands = [[], [], []]
    
    for i in range(len(deck)):
        number = i % 3
        hands[number].append(deck[i])
    return hands




def uno_who_played_what(cards_played):
    
    hands = [[], [], [], []]
    hands_index = 0
    num_to_skip = 0  

    
    for i in range(len(cards_played)):
        hands[hands_index].append(cards_played[i])
        if cards_played[i] == 'skip':
            hands_index = (hands_index + 1) % 4
        hands_index = (hands_index + 1) % 4
    return hands

'''
# B5 Uno extension 1
def uno_who_played_what_Bonus(cards_played, num_players, starting_player):
    # Preparatory condition
    hands = []
    while num_players > 0:
        hands.append([])
        num_players -= 1
    #print(len(hands)) # check whether hands is correct. 
    hands_number = starting_player - 1
    num_to_skip = 0  # skip means to skip one person

    # Main code
    for i in range(len(cards_played)):

        if hands_number > num_players-1: # use properties of congruence
            hands_number = hands_number % (num_players - 1)
        hands[hands_number].append(cards_played[i])
        hands_number += 1
            
 '''   
'''     
        elif cards_played[i] == 'skip':
            hands[hands_index].append(cards_played[i])
            next_hands_index = (hands_index + 1) % len(hands)
            hands_index += 1

def next_index(hands, hands_index):
    next_hands_index = (hands_index + 1) % len(hands)
    return next_hands_index

'''
