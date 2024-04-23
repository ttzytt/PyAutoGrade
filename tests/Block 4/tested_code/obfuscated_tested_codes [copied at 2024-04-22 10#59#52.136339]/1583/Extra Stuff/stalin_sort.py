def remove_from_list(list_input, remove_index):
    for i in range(remove_index, len(list_input) - 1):
        list_input[i] = list_input[i+1]
    del list_input[-1]

def sort_like_stalin(numbers):
    i = 0
    while i < len(numbers) - 1:
        while i < len(numbers) - 1 and numbers[i] >= numbers[i + 1]:

            remove_from_list(numbers, i+1)

        i += 1
        
    return numbers

numbers = input('What list would you like to stalin sort? ')
numbers = numbers.split(',')

numbers = list(map(int, numbers))

numbers = sort_like_stalin(numbers)

print(numbers)
