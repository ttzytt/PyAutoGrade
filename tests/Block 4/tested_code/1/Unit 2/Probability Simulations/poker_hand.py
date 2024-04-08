

import random
random.seed()

possible_rank = ['1','2','3','4','5','6','7','8','9','a','b','c','d']
possible_suit = ['♠','♥','♦','♣']
deck = []



def is_full_house():
    
    
    for i in range(len(possible_rank)):
        for j in range(4):
            deck.append(possible_rank[i]+possible_suit[j])
    tool_num = 0 
    card_list = []
    
    
    for i in range(5):
        card = random.choice(deck)
        card_list.append(card)
    card_list.sort()

    
    for i in range(len(card_list)-2):
        if card_list[i][0] == card_list[i+1][0] == card_list[i+2][0]: 
            a = card_list[i][0]
            tool_num +=1
            for i in range(len(card_list)-1):
                if card_list[i][0] == card_list[i+1][0] != a: 
                    tool_num += 1
                    print(tool_num)
    return (tool_num == 2)


def odd_full_house(): 
    function_times = 1
    average_all = 0
    for i in range(10): 
        while is_full_house() != True:
            is_full_house
            function_times += 1
        print(function_times)
        average_all += function_times
    average_chance = average_all/10
    return average_chance





def is_s_flush():
    
    possible_rank = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    possible_suit = ['♠','♥','♦','♣']

    tool_num = 0
    card_list = []
    while len(card_list)<5: 
        rank = random.choice(possible_rank)
        suit = random.choice(possible_suit)
        card = [rank,suit]
        if card not in card_list: 
            card_list.append(card)
    card_list.sort()

    
    for i in range(1):
        if (card_list[i][0]+4 == card_list[i+1][0]+3 == card_list[i+2][0]+2 == card_list[i+3][0]+1 == card_list[i+4][0]) or (card_list[i][0] == 1 and card_list[i+1][0] == 10 and card_list[i+2][0] == 11 and card_list[i+3][0] == 12 and card_list[i+4][0] == 13):
            tool_num += 1 
            if card_list[i][1] == card_list[i+1][1] == card_list[i+2][1] == card_list[i+3][1] == card_list[i+4][1]:
                tool_num +=1 
    return (tool_num == 2)


def odd_s_flush(): 
    
    average_all = 0
    for i in range(10):
        function_times = 1
        while is_s_flush() != True:
            function_times += 1
        print(function_times)
        average_all += function_times
    average_chance = average_all/10
    return average_chance



def is_flush():
    
    possible_rank = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    possible_suit = ['♠','♥','♦','♣']

    tool_num = 0
    card_list = []
    while len(card_list)<5:
        rank = random.choice(possible_rank)
        suit = random.choice(possible_suit)
        card = [rank,suit]
        if card not in card_list:
            card_list.append(card)
    card_list.sort()
    
    for i in range(1):
        if card_list[i][1] == card_list[i+1][1] == card_list[i+2][1] == card_list[i+3][1] == card_list[i+4][1]:
            tool_num +=1

    return (tool_num == 1)

def odd_flush(): 
    average_all = 0
    for i in range(10):
        function_times = 1
        while is_flush() != True:
            function_times += 1
        print(function_times)
        average_all += function_times
       
    average_chance = average_all/10
    return average_chance


def is_flush_dice():
    
    possible_suit = ['♠','♥','♦','♣']
    tool_num = 0
    card_list = []
    while len(card_list)<5:
        suit = random.choice(possible_suit)
        card_list.append(suit)
    card_list.sort()
    print(card_list)
    for i in range(1):
        if card_list[i][1] == card_list[i+1][1] == card_list[i+2][1] == card_list[i+3][1] == card_list[i+4][1]:
            tool_num +=1

    return (tool_num == 1)


def odd_flush_dice():

    average_all = 0
    for i in range(10):
        function_times = 1
        while is_flush() != True:
            function_times += 1
        print(function_times)
        average_all += function_times
       
    average_chance = average_all/10
    return average_chance



