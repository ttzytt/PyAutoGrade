



num = int(input('Enter in an integer: ')) 
num_factorial = 1 
count = num

while(count > 0):
    num_factorial = num_factorial * count
    count -= 1

print(str(num) + ' factorial is ' + str(num_factorial))
