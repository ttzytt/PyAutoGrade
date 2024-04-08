import random
random.seed()





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
