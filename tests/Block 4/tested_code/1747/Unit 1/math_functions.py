



number = int(input("Enter a positive integer: ")) 
multi = 1 
add = 0 
jump_add = 0
num = number
ber = number
umb = number

while num > 0: 
    add = add + num
    num = num - 1 

while ber > 1: 
    multi = multi * ber
    ber = ber - 1 

while umb > 0: 
    jump_add = jump_add + umb
    umb = umb - 2 


print('The factorial of ' + str(number) + ' is ' + str(multi))
print('The triangular number of ' + str(number) + ' is ' + str(add))
print('The "new" triangular number of ' + str(number) + ' is ' + str(jump_add))



