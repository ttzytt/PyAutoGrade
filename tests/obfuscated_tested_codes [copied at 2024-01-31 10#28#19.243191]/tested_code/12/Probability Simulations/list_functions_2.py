



def largest(list):
    list.sort()
    
    return list[-1] 
    


def alternate_sum(list):
    return sum(list[::2]) - sum(list[1: :2])
    
    


def rotate_right(list):
    return list[-1:-2:-1] + list[0:-1]
    
    


def deal_3_hands(list):
    return list[0: :3],list[1: :3],list[2: :3]
    
    
