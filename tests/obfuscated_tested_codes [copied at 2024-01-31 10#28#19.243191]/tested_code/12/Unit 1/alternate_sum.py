



def alternate_sum(numbers):
    sum = 0
    if len(numbers) < 1:
        return 0
    for count in range(numbers): 
        if count == 0 or count % 2 == 0: 
            sum += numbers[count]
        elif count % 2 == 1: 
            sum -= numbers[count]
        return sum

numbers = list(input('Enter: '))
