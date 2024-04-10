








def largest_element(nums):
    if len(nums) == 0:
        return None
    
    nums.sort()
    return nums[-1]



def alternate_sum(nums):
    if len(nums) == 0:
        return None
    
    return sum(nums[0:len(nums):2]) - sum(nums[1:len(nums):2])




def rotate_right(nums):
    if len(nums) == 0:
        return []

    
    
    return ([nums[-1]] + nums[:-1])




def deal_3_hands(deck):
    return [deck[:len(deck):3], deck[1:len(deck):3], deck[2:len(deck):3]]


