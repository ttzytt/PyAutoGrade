import random
random.seed


'''
I understand this function
'''
def creat_list(num=3):
    
    X = []
    for i in range(num):
        X.append([])
        
        for j in range(num):
            X[i].append(0)
    return X

'''
I almost understand this function
'''


def sums(lists,num):
    results = []
    
    for row in range(0,len(lists)):
        for col in range(0,len(lists)-num+1):
            sum_1 = 0
            for i in range(num):
                sum_1 += lists[row][col+i]
            results.append(sum_1)
    
    for col in range(0,len(lists)):
        for row in range(0,len(lists)-num+1):
            sum_1 = 0
            for i in range(num):
                sum_1 += lists[row+i][col]
            results.append(sum_1)

    
    for row in range(len(lists)-num+1):
        for col in range(len(lists)-num+1):
            sum_1 = 0
            for i in range(num):
                sum_1 += lists[row+i][col+i]
            results.append(sum_1)
    
    for row in range(len(lists)-num,-1,-1):
        for col in range(num-1,len(lists)):
            sum_1 = 0
            for i in range(num):
                sum_1 += lists[row+i][col-i]
            results.append(sum_1)
    return results

'''
I hardly understand this function
'''


def judgement(list_1,num):
    for i in range(0,len(list_1)):
        if list_1[i] == num:
            return True
    return False

'''
I understand this function, but I didn't find it in your main code
'''
# Return a new lists after choosed a place that is marked 0 in lists
# and mark it as 1
def choose_random_place(lists):
    computer_1= random.randint(0,len(lists)-1)
    computer_2= random.randint(0,len(lists)-1)
    # If the spot has been occupied then the computer choose another one
    while lists[computer_1][computer_2] != 0:
        computer_1= random.randint(0,len(lists)-1)
        computer_2= random.randint(0,len(lists)-1)
    lists[computer_1][computer_2] = 1
    return lists
'''
I partly understand this function
'''
# Check is there any move for player to form a line with length constant and return all the moves
def move_check_human(signals,size,length,constant):
    result = []
    for row in range(size):
        for col in range(size):
             # if the block is not occupied and can form a line with length 'constant'
            if signals[row][col] == 0:
                signals[row][col] = -1
                if judgement(sums(signals,length),-constant) ==  True:
                    signals[row][col] = 0
                    result.append([row,col])
                signals[row][col] = 0
    return result
'''
I almost understand this function
'''
# Check is there any move for computer to form a line with length constant and return all the moves
def move_check_computer(signals,size,length,constant):
    result = []
    for row in range(size):
        for col in range(size):
            # if the block is not occupied and can form a line with length 'constant'
            if signals[row][col] == 0:
                signals[row][col] = 1
                if judgement(sums(signals,length),constant) ==  True:
                    signals[row][col] = 0
                    result.append([row,col])
                signals[row][col] = 0
    return result



