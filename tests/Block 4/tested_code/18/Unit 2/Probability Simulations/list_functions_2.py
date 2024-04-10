


from operator import itemgetter



def largest_element(numbers):

    numbers.sort()

    return numbers[-1]



def alternate_sum(numbers):

    even_sum = sum(alternate_sum[::2])
    odd_sum = sum(alternate_sum[1::2])

    return (even_sum - odd_sum)
