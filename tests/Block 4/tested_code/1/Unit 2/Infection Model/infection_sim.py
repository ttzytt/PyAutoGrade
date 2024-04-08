








import random
random.seed()



n = 5
array = [[0 for i in range(n)] for j in range(n)]

for i in range(1,n-1):
    for j in range(1,n-1):
        if random.random() < 0.5:
            array[i][j] = 1

print(array)
def infection_probability_percent(row, col, array):
    print(0)
    a = 0
    if array[row][col-1] == 1:
            a += 1
    if array[row][col+1] == 1:
            a += 1
    if array[row-1][col] == 1:
            a += 1
    if array[row+1][col] == 1:
            a += 1
    return a


           
def to_get_them_infected():
    array_new = []
    for i in range(n):
            array_new.append(array[i])
    print(array_new)
    print('yesbuddy')
    for i in range(1,n-1):
        for j in range(1,n-1):
            if array[i][j] == 0:
                if random.random()<=infection_probability_percent(i,j,array):
                    array_new[i][j] = 1
            elif array[i][j] == 1:
                if random.random() < 1:
                    array_new[i][j] = 0
                    print(1)
    print(array)
    print('')
    print(array_new)
            
            

