



from infection_functions import*


row = int(input("row:"))
col = int(input("col:"))
infection_probability = float(input("infection_probability: "))
heal_probability = float(input("heal_probability: "))
input_ = int(input("how many people are infected initially: "))
num = int(input("how many round:"))



M = create_list(row,col)
initialize (M,input_,row,col)



Y = [M]


for i in range(num):
    X = process(infection_probability,heal_probability,row,col,Y[i])
    Y.append(X)




for k in range(num):
    for i in range(1,row+1):  
        for j in range(1,col+1):
            if Y[k][i][j] == 0:
                print('·',end = '')
            else:
                print('x', end = '')
        print()
    print()


                  
