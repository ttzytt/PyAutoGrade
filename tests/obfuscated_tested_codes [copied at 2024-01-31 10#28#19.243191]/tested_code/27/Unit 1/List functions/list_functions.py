





def count_number_larger_than(target, nums):
    if nums == []:
        return 0
    nums_bigger = 0
    for i in range(nums[0], nums[len(nums)-1]):
        if nums[i] > target:
            nums_bigger += 1
    return nums_bigger



def average(nums):
    if nums == []:
        return 0
    average = sum(nums)/len(nums)
    return average 



def largest_element(nums):
    if nums == []:
        return 0
    max_now = nums[0]
    for i in range(nums[1], nums[len(nums)-1]):
        if nums[i] > max_now:
            max_now = nums[i]
    return max_now
  

def largest_element_2(nums):
    if nums == []:
        return 0
    max_2now = max(nums)
    return max_2now


def all_equal(my_list):
    if my_list == []:
        return False
    if len(my_list) == 1:
        return True
    first_num = my_list[0]
    i = 1
    while my_list[i] == first_num:
        i += 1
        if i == len(my_list):
            break
    if i == len(my_list):
        return True
    else:
        return False


def alternate_sum(nums):
    even_sum = 0
    odd_sum = 0
    if nums == []:
        return False
    for i in range(0, len(nums), 2):
        even_sum = even_sum + nums[i]
    for i in range(1,len(nums), 2):
        odd_sum = odd_sum + nums[i]
    alternate_sums = even_sum - odd_sum
    return alternate_sums



def ordered_list(nums):
    a = 1
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            a += 1
    if a == len(nums):
        return True
    else:
        return False

def is_ordered(nums, is_strict):
    if ordered_list(nums) == is_strict:
        return True
    else:
        return False
    

def rotate_right(nums):
    if nums == []:
        return False
    y = nums[len(nums)-1]
    x = len(nums)-1
    while x > 0:
        nums[x] = nums[x-1]
        x -= 1
    nums[0] = y
    return nums

 



def weird_double(nums):
    i = 0
    if nums == []:
        return False
    while i < len(nums):
        if nums[i]%3 != 0:
            nums[i] = 2*nums[i]
        elif nums[i]%3 == 0:
            nums[i] = 1*nums[i]
            i += 3
        i += 1
            
    return nums

new_list = []

def merge_ordered_list(num1, num2):
    b = 0
    a = 0
    while b < len(num1)-1 and a < len(num2)-1:
        if num1[b] < num2[a]:
            new_list.append(num1[b])
            b += 1
        elif num2[a] <= num1[b]:
            new_list.append(num2[a])
            a += 1
    if a == len(num2):
        for i in range(b, len(num2)-1):
            new_list.append(num2[i])
    if b == len(num1):
        for i in range(a, len(num1)-1):
            new_list.append(num1[i])
    return new_list


def deal_3_hands(deck):
    deck_index = 0
    hand_index = 0
    hands = [[],[],[]]
    while deck_index < len(deck):
        hands[hand_index].append(deck[deck_index])
        deck_index += 1
        hand_index = (hand_index + 1)%3
    return hands



def uno_who_played_what(cards_played):
    deck_index = 0
    hand_index = 0
    hands = [[],[],[],[]]
    while deck_index < len(cards_played):
        hands[hand_index].append(cards_played[deck_index])
        deck_index += 1
        hand_index = (hand_index + 1)%4
    return hands

            
        


                    
