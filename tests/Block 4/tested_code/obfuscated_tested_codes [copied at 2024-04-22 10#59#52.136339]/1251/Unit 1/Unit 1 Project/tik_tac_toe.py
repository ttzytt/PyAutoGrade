



import random
random.seed

print("In the game, you will use 'X' and computer is going to use 'X'")
print("To put an 'X' in, just type the coordinate,example: if you type (row 2, column 1), X will be put in the block showned below")
print("  1  2  3")
print("1 [] [] []")
print("2 [X] [] []")
print("3 [] [] []")
print()


def check_3(nums):
    return (3 in nums) or (-3 in nums)
    

X = [[0,0,0],
     [0,0,0],
     [0,0,0]]




judgement = False





while judgement == False:
    
    computer_1= random.randint(0,2)
    computer_2= random.randint(0,2)

    
    while X[computer_1][computer_2] != 0:
        computer_1= random.randint(0,2)
        computer_2= random.randint(0,2)
    X[computer_1][computer_2] = 1
    for i in range(0,3):
        print()
        for j in range(0,3):
            if X[i][j] == 1:
                print(" O ", end ="")
            elif X[i][j]== -1:
                print(" X ", end ="")
            else:
                print("[] ", end ="")
    
    print()
    
    
    row = int(input("Row: "))
    column = int(input("Column: "))
    X[row-1][column-1] = -1
    for i in range(0,3):
        print()
        for j in range(0,3):
            if X[i][j] == 1:
                print(" O ", end ="")
            elif X[i][j]== -1:
                print(" X ", end ="")
            else:
                print("[] ", end ="")
    

    
    sums = [0,0,0,0,0,0,0,0]
    
    for i in range(3):
        sums[i] = X[i][0]+X[i][1]+X[i][2]
    for i in range(3):
        sums[i+3] = X[0][i]+X[1][i]+X[2][i]
    sums[6] = X[0][0]+X[1][1]+X[2][2]
    sums[7] = X[0][2]+X[1][1]+X[2][0]

    
    judgement = check_3(sums)
    print()
print("The game is over")
    
    
    
       

    
    



