


number = int(input("Please enter a number."))
trinumber = number 
triangle = trinumber

while number > 1:
    triangle = (number * (number + 1)) / 2
    number = 0  

print('The triangular number of ' + str(trinumber) + ' is ' + str(round(triangle)))


