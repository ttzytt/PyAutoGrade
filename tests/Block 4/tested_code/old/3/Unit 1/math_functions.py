





integer=int(input('Enter a integer: '))


factor=int(1)
number = integer

while number > 1:
        factor = factor * number
        number = number - 1
print(str(integer) + '! is ' + str(factor))



number = 1
helper = 1
time = 2
while time <= integer:
    helper = helper + number + 1
    number = number + 1
    time = time + 1
print('Triangular number: ' + str(helper))




if integer/2 != round(integer/2):
    number = (integer+1)/2
    factor = 1
    helper = 1
    while number > 1:
        factor = factor + 2
        helper = helper + factor
        number = number - 1
    print("'New' triangular number: " + str(helper))
else:
    number = integer/2
    factor = 2
    helper = 2
    while number > 1:
        factor = factor + 2
        helper = helper + factor
        number = number - 1
    print("'New' triangular number: " + str(helper))

