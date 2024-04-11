






def count_number_larger_than(target, numbers):
      count = 0 
      for i in range(len(numbers)):
            if numbers[i] > target : 
                  count += 1 
      return count


def average(numbers):
      if len(numbers) == 0: 
            return 0
      else: 
            sum_function = 0 
            for i in numbers:
                  sum_function = i + sum_function
            return sum_function/len(numbers) 



def largest_element(numbers):
      if len(numbers) == 0: 
            return 0
      else: 
            max_value = numbers[0] 
            for i in numbers: 
                  if (i > max_value): 
                        max_value = i
            return max_value




def all_equal(my_list):
      if len(my_list) == 0: 
            return True
      else: 
            for i in  range(len(my_list) - 1): 
                return my_list[i] == my_list[i+1]
                     






