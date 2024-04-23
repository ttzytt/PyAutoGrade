



import random
random.seed


Cards_total = []
for i in range (1,14):
    Cards_total.append([i,'♠'])
    Cards_total.append([i,'♥'])
    Cards_total.append([i,'♦'])
    Cards_total.append([i,'♣'])



def all_equal(cards,index):
    for i in range(len(cards)-1):
        if cards[i][index] != cards[i+1][index]:
            return False
    return True



def consecutive(cards,index):
    satisified_total = [1,2,3,4,5,6,7,8,9,10,11,12,13,1]
    for i in range(13):
        judgement = 0
        for j in range (5):
            if cards[j][index] == satisified_total[i]+j:
                judgement += 1
            if judgement == 5:
                return True
    return False
                




def one_trial_full_house():
    random.shuffle(Cards_total)
    cards = Cards_total[:5]
    cards.sort()
    if ((all_equal(cards[:3],0) and all_equal(cards[3:],0))or
    (all_equal(cards[:2],0) and all_equal(cards[2:],0))):
        return 1
    return 0




def one_trial_straight_flush():
    random.shuffle(Cards_total)
    cards = Cards_total[:5]
    cards.sort()
    if all_equal(cards,1) and consecutive(cards,0):
        return 1
    return 0




def one_trial_flush():
    random.shuffle(Cards_total)
    cards = Cards_total[:5]
    cards.sort()
    if all_equal(cards,1) is True and consecutive(cards,0) is False:
        return 1
    return 0


def calculate_full_house(num_trials = 1000000, type_ = 0):
    records = []
    for i in range(num_trials):
        records.append(one_trial_full_house())
    if type_ == 0:
        return num_trials/sum(records)
    else:
        return sum(records)/num_trials


def calculate_straight_flush(num_trials = 100000, type_ = 0 ):
    sum_ = 0
    for i in range(num_trials):
        sum_ += one_trial_straight_flush()
    if type_ == 0:
        return num_trials/sum_
    else:
        return sum_/num_trials


def calculate_flush(num_trials = 1000000, type_ = 0):
    records = []
    for i in range(num_trials):
        records.append(one_trial_flush())
    if type_ == 0:
        return num_trials/sum(records)
    else:
        return sum(records)/num_trials



type_ = input("Which type you want to calculate? (Full_house, Straight_flush or Flush): ")


if (type_ == "Full_house"):
    print('The odds of being dealt a ' + type_ +  ' is 1 in ' + str(calculate_full_house()))
elif (type_ == "Straight_flush"):
    print('The odds of being dealt a ' + type_ +  ' is 1 in ' + str(calculate_straight_flush()))
elif (type_ == "Flush"):
    print('The odds of being dealt a ' + type_ +  ' is 1 in ' + str(calculate_flush()))

    






def one_trial():
    record = []
    for i in range(5):
        record.append(random.randint(1,4))
    for i in range(1,5):
        if record[i-1] != record[i]:
            return 0
    return 1


def calculate(nums):
    
    records = []

    
    for i in range(nums):
        records.append(one_trial())
    sum_ = 0
    
    for i in range(nums):
        sum_ += records[i]
    
    return nums/sum_

 
