






 

integer = int(input('Enter a number: '))


n = 1
count = 1
value = 1
while n <= integer:
    factor = count
    count = 1
    while count <= n:
        count = count +1
        a = factor
        value = value + 1
    n = n + 1
    factor = count

value = value - 1
print(value)
