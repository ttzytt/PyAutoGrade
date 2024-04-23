






import random
random.seed()



n = 3
array = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if random.random() < 0.1:
            array[i][j] = 1

print(array)

def infection_probability_percent(array[i][j]):
    a = 0
    if array[i][j-1] == 1:
        a += 1
    if array[i][j+1] == 1:
        a += 1
    if array[i-1][j] == 1:
        a += 1
    if array[i+1][j] == 1:
        a += 1
    infection_probability = a*0.1
    return infection_probability

for i in range(n):
    for j in range(n):
        infection_probability_percent(array[i][j])
        if random.random() < infection_probability:
            array[i][j] == 1
for 


