



import random
random.seed




def creat_list(num=3):
    
    X = []
    for i in range(num):
        X.append([])
        
        for j in range(num):
            X[i].append(0)
    return X




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




def judgement(list_1,num):
    for i in range(0,len(list_1)):
        if list_1[i] == num:
            return True
    return False






def move_check_human(signals,size,length,constant):
    result = []
    for row in range(size):
        for col in range(size):
             
            if signals[row][col] == 0:
                signals[row][col] = -1
                if judgement(sums(signals,length),-constant) ==  True:
                    signals[row][col] = 0
                    result.append([row,col])
                signals[row][col] = 0
    return result


def move_check_computer(signals,size,length,constant):
    result = []
    for row in range(size):
        for col in range(size):
            
            if signals[row][col] == 0:
                signals[row][col] = 1
                if judgement(sums(signals,length),constant) ==  True:
                    signals[row][col] = 0
                    result.append([row,col])
                signals[row][col] = 0
    return result



