




def largest_element(numbers):
    numbers.sort()
    return numbers[-1]


def alternate_sum(numbers):
    return sum(numbers[::2])


def rotate_right(numbers):
    return [numbers[-1]] + numbers[0:-1]



def deal_3_hands(numbers):
    return numbers[0::3], numbers[1::3], numbers[2::3]
