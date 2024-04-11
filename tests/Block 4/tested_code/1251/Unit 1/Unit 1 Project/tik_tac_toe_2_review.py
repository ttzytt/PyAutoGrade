'''
Reviewed by Alex
'''
import random
random.seed






from tik_tac_toe_2_functions import*

size = int(input("How large the board you want to play: "))
length = int(input("How many symbols in a line is considered as win: "))

count = 1
signals = creat_list(size)
while (judgement(sums(signals,length),length) ==  False)and (judgement(sums(signals,length),-length) ==  False) and (size*size)/2 > (count-1):
    choice = 0
    index = 0
    
    if count == 1:
        signals[round((size-1)/2)][round((size-1)/2)] = 1
    
    else:
        
        
        for i in range(0,length):
            
            if len(move_check_computer(signals,size,length,length-i)) != 0:
                choice = move_check_computer(signals,size,length,length-i)
                randomness = random.randint(0,len(choice)-1)
                
                signals[choice[randomness][0]][choice[randomness][1]] = 1
                break
            
            elif len(move_check_human(signals,size,length,length-i)) != 0:
                choice = move_check_human(signals,size,length,length-i)
                randomness = random.randint(0,len(choice)-1)
                
                signals[choice[randomness][0]][choice[randomness][1]] = 1
                break
    print()
    
    for row in range(0, size):
        for col in range(0,size):
            print("┌───┐",  end = "")
        print(" ")
        for col in range (0,size):
            if signals[row][col] == -1:
                print("│ " + "X" + " │", end = "")
            elif signals[row][col] == 1:
                print("│ " + "O" + " │", end = "")
            else:
                print("│   │", end = "")
        print(" ")
        for col in range(0,size):
            print("└───┘",  end = "")
        print(" ")
    print()
    
    if judgement(sums(signals,length),length) ==  True:
        break
    if size % 2 == 1 and count == ((size*size)+1)/2:
        break
    
    row = int(input("Row: "))
    column = int(input("Column: "))
    while signals[row-1][column-1] != 0:
        print("This block is occupied")
        print()
        row = int(input("Row: "))
        column = int(input("Column: "))
        print()
    
    signals[row-1][column-1] = -1
    
    
    for row in range(0, size):
        for col in range(0,size):
            print("┌───┐",  end = "")
        print(" ")
        for col in range (0,size):
            if signals[row][col] == -1:
                print("│ " + "X" + " │", end = "")
            elif signals[row][col] == 1:
                print("│ " + "O" + " │", end = "")
            else:
                print("│   │", end = "")
        print(" ")
        for col in range(0,size):
            print("└───┘",  end = "")
        print(" ")
    print()
    count += 1


print("The game is over")
    



