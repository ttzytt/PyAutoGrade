






def largest_element(List):
    List.sort()
    return List[-1]


def alternate_sum(List): 
    return sum(List[ : :2])-sum(List[1: :2])


def rotate_right(List):
    return [List[-1]] + List[0:-1]


def deal_3_hands(cards_list):
    return [cards_list[ : :3]]+[cards_list[1: :3]]+[cards_list[2: :3]]
