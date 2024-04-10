



user_input = int(input('Input an integer n: '))
count = 1
result = 0


while count <= user_input: 
    result = result + count
    count = count + 1

print('The triangular number of ' + str(user_input)+ ' is '  + str(result) + '.')
    
