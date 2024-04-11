



def weird_double(nums):
    for i in range(len(nums)):
        print('banana')
        if nums[i]%3 != 0:
            nums[i] = nums[i] + nums[i]
    return nums
