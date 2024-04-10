



number = int(input("Write a random positive number 'n': ")) 
multi = 1 
num = number

while num > 1: 
    multi = multi * num
    num = num - 1 

print('The factorial of ' + str(number) + ' is ' + str(multi)) 


