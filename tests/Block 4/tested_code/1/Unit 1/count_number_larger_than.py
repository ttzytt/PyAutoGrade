def centered_average(nums):
  if len(nums) < 1:
    return 0
  if nums[0] >= nums[1]:
      max_num = nums[0]
      min_num = nums[1]
  elif nums[1] > nums[0]:
      max_num = nums[1]
      min_num = nums[0]

  for i in range(len(nums)):
      if nums[i] >= max_num:
          max_num = nums[i]
      elif nums[i] <= min_num:
          min_num = nums[i]
  min_num = 0
  max_num = 0
  return nums
