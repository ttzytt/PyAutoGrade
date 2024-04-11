


def largest_element(numbers):
    numbers.sort
    numbers[::-1]
    print(numbers[0])

    print()

def alternate_sum(numbers):
    even_index = numbers[::2]
    odd_index = numbers[1::2]
    
    alt_sum = sum(even_index) - sum(odd_index)
    
    print(alt_sum)

    print()

def rotate_right(my_list):
    sliced = my_list[:-1]
    my_list = my_list + sliced
    print(my_list)

def deal_3_hands(deck):
    deck_1 = deck[::3]
    deck_2 = deck[1::3]
    deck_3 = deck[2::3]

    full_deck = [[deck_1], [deck_2], [deck_3]]

    print(full_deck)

    
