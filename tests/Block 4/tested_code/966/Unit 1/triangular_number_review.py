



n = int(input('Enter a positive integer n: '))


result = 0
i = 1


if n <= 0:
    print('Please enter a positive integer.')
else:
    while i <= n:
        result += i
        i += 1


result = str(result)


print('The nth triangle number is ' + result)


