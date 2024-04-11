


user_input = int(input('Choose a number '))
counter = 1
tri = 0
flag = False
while flag == False:
    tri = tri + counter
    
    if counter == user_input:
        flag = True
    counter = counter + 1   

print('Your n! number is ' + str(tri))
