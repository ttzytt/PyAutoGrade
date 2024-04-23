



num = int(input('Enter in an integer: ')) 
triangle_number = 0 
count = num

while(count > 0):
    triangle_number = triangle_number + count
    count -= 1

print('The triangle of ' + str(num) + ' is ' + str(triangle_number))
