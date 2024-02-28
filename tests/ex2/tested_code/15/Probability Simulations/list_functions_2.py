



def largest_element(numbers):
    numbers.sort()
    return numbers[-1]


def alternate_sum(numbers):
    return sum(numbers[0:len(numbers):2])


def rotate_right(numbers):
    return ([numbers[-1]] + numbers[0:len(numbers)-1])


def deal_3_hands(deck):
    return deck[::3], deck[1::3], deck[2::3]
