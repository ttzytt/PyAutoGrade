





import random
random.seed()


base_infect_rate = 0.01*int(input("what do you want the base infection rate to be(from 1 to 100)?"))
base_heal_rate = 0.01*int(input("what do you want the base healing chance to be(from 1 to 100)?"))



n = 6
array = [[0 for i in range(n)] for j in range(n)]

for i in range(1,n-1):
    for j in range(1,n-1):
        if random.random() < 0.2:
            array[i][j] = 1

print(array)

def infection_probability_percent(row, col, array): 
    a = 0
    if array[row][col-1] == 1:
            a += 1
    if array[row][col+1] == 1:
            a += 1
    if array[row-1][col] == 1:
            a += 1
    if array[row+1][col] == 1:
            a += 1
    return a*base_infect_rate


           
def to_get_them_infected(array): 
    array_new = [[0 for i in range(n)] for j in range(n)]
    for i in range(1,n-1):
        for j in range(1,n-1):
            if array[i][j] == 0:
                if random.random()<=infection_probability_percent(i,j,array):
                    array_new[i][j] = 1
                else:
                    array_new[i][j] = 0
            elif array[i][j] == 1:
                if random.random() < base_heal_rate:
                    array_new[i][j] = 0
                else:
                    array_new[i][j] = 1
    print(array)
    return array_new
    

    
b = 0 
years = int(input("How many years do you wanna run the simulation(plz enter interger # of years)?"))
while b < years:
    print("")
    print("year " + str(a+1) + ":")
    b += 1
    array = to_get_them_infected(array)
    
    

