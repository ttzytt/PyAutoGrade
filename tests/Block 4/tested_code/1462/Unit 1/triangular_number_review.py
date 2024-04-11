




user_input = int(input('Input an integer n: ')) 
count = 1
result = 0

while count <= user_input: 
    result = result + count
    count = count + 1

if user_input == 1: 
    print('1 = 1')
else:
    print('1+...+' + str(user_input) + ' = '  + str(result))
    
    
