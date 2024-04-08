




def largest_element(nums):
    nums.sort()
    print(nums)
    return nums[len(nums)-1]


def alternate_sum(nums):
    even_sum = sum(nums[::2])
    odd_sum = sum(nums[1::2])
    alternate_sums = even_sum - odd_sum
    return alternate_sums



def rotate_right(nums):
    return [nums[len(nums)-1]] + nums[:-1]



def deal_3_hands(cards):
    hand_1 = cards[::3]
    hand_2 = cards[1::3]
    hand_3 = cards[2::3]
    return [hand_1,hand_2,hand_3]
