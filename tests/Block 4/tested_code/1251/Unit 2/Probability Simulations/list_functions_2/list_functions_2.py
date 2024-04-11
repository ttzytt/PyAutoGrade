

def largest_element(numbers):
    if len(numbers) != 0:
        numbers.sort()
        return numbers[-1]
    return None


def alternate_sum(numbers):
    if len(numbers) != 0:
        return sum(numbers[0:len(numbers):2])-sum(numbers[1:len(numbers):2])
    return None



def rotate_right(numbers):
    if len(numbers) != 0:
        return [numbers[-1]] + numbers[:-1]
    return []


def deal_3_hands(cards):
    return [cards[0:len(cards):3],cards[1:len(cards):3],cards[2:len(cards):3]]
