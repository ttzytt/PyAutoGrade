



number = int(input("Write a random positive integer 'n': ")) 
add = 0 
num = number

while num > 0: 
    add = add + num
    num = num - 1 

print('The triangular number of ' + str(number) + ' is ' + str(add)) 
