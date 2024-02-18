


n = int(input('write a positive integer: '))


if n < 0:
    print('factorial is not defined for negative numbers.')
else:
    result = 1
    input_n = n


while n > 0:
    result *= n
    n -= 1


result = str(result)


print('the factorial of n is ' + result)
