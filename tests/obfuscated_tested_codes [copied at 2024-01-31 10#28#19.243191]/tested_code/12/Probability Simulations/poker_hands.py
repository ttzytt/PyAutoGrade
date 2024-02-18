




from poker_hands_functions import *



def full_house():
    times = 1
    hands = give_cards()
    while find_full_house(hands) == False: 
        times += 1
        hands = give_cards()
    return times


def average_full_house(num_trials):
    times = 0
    for count in range(num_trials):
        full_house()
        times += full_house()
    return times/num_trials



def straight_flush():
    times = 1
    hands = give_cards()
    while find_straight_flush(hands) == False: 
        times += 1
        hands = give_cards()
    return times


def average_straight_flush(num_trials):
    times = 0
    for count in range(num_trials):
        straight_flush()
        times += straight_flush()
    return times/num_trials



def flush(): 
    times = 1
    hands = give_cards()
    while find_flush(hands) == False: 
        times += 1
        hands = give_cards()
    return times


def average_flush(num_trials):
    times = 0
    for count in range(num_trials):
        flush()
        times += flush()
    return times/num_trials




def dices_flush():
    times = 1
    dices = give_dices()
    while find_dices_flush(dices) == False: 
        times += 1
        dices = give_dices()
    return times


def average_dices_flush(num_trials):
    times = 0
    for count in range(num_trials):
        dices_flush()
        times += dices_flush()
    return times/num_trials



def comparison():
    print('The odd of dices flush is one in')
    dices_flush = average_dices_flush(1000)
    print(str(dices_flush) + ' times')
    print('The odd of all flush (normal and straight) combined is one in')
    normal = average_flush(1000)
    straight = average_straight_flush(10)
    flush = 1/(1/normal+1/straight)
    print(str(flush) + ' times')
    
    print('The ratio of dices flush to poker flush is ' + str(flush/dices_flush))



types = input('Which type of simulation do you want to try? ')
print()
while types != 'quit':
    
    if types == 'flush' or types == 'straight flush' or types == 'full house' or types == 'dices':
        
        times_trial = int(input('How many times do you want to calculate to get the average? '))
        print()
        print('The average odds of being dealt a ' + types + ' is one in ')
        
        if types == 'flush':
            result = average_flush(times_trial)
        elif types == 'straight flush':
            result = average_straight_flush(times_trial)
        elif types == 'full house':
            result = average_full_house(times_trial)
        elif types == 'dices flush':
            result = average_dices_flush(times_trial)
        print(str(result) + ' times')
        
    elif types == 'comparison':
        comparison()
        
    else:
        print('Your input is invalid, please try again')
        
    print()
    types = input('Which type of simulation do you want to try? ')
    
if types == 'quit':
    print('See you next time')
               
          
