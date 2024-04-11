




integer = int(input('Enter a number: '))


number = 1
helper = 1
time = 2
while time <= integer:
    helper = helper + number + 1
    number = number + 1
    time = time + 1
print('The triangular number is ' + str(helper))
