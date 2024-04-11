import random
random.seed()




def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i + 1] != a_list[i] + 1:
            return False
    for i in range(len(a_list) - 1):
        if a_list[i + 1] != a_list[i] - 1:
            return False
    return True


print(is_consecutive([5, 4, 3, 2, 1]))










    



