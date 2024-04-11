



information other than from the teacher and the course materials
def largest_element(numbers):
    """
    Sorts the list 'numbers' and returns its largest element, or None if the list is empty.
    """
    if not numbers:
        return None
    numbers.sort()
    return numbers[-1]



def alternate_sum(numbers):
    """
    Returns the sum of elements at even indices minus the sum of elements at odd indices in the 'numbers' list.
    """
    return sum(numbers[::2]) - sum(numbers[1::2])



def rotate_right(my_list):
    """
    Rotates elements of 'my_list' one position to the right, returning the modified list.
    """
    return [my_list[-1]] + my_list[:-1] if my_list else my_list



def deal_3_hands(deck):
    """
    Splits a 'deck' list into three parts, dealing every third card to each hand.
    """
    return deck[0::3], deck[1::3], deck[2::3]

