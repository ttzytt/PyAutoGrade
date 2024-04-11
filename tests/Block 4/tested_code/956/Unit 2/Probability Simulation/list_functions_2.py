




def largest_element(lists):
    
    lists.sort()
    
    return lists[-1]

 


def alternate_sum(lists):
    return sum(lists[0:-1:2]) - sum(lists[1:-1:2])



def rotate_right(lists):
    return lists[-1]+lists[0:-2]



def deal_3_hands(lists):
    return [lists[0:-1:3],lists[1:-1,3],lists[2:3:-1]]
