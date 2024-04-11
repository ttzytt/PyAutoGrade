







def count_number_larger_than(target, numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > target:
            count += 1
    return count
    


def average(numbers):
    if len(numbers) == 0:
        return None
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    average = sum / len(numbers)
    return average


def largest_element(numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max_number:
            max_number = numbers[i]
    return max_number




def all_equal(my_list):
    if len(my_list) == 0:
        return None
    
    
    target_value = my_list[0]
    
    
    
    
    is_bool = type(my_list[0]) == bool
    for i in range(len(my_list)):
        
        if not (type(my_list[i]) == bool) == is_bool:
            return False
        if not my_list[i] == target_value:
            return False
    
    
    
    return True

    
    
    
    
    
    
    



def alternate_sum(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    
    for i in range(0,len(numbers),2):
        total += numbers[i]
    
    for i in range(1,len(numbers),2):
        total -= numbers[i]
    return total











def is_ordered(numbers, is_strict):
    if len(numbers) == 0:
        return True
    if is_strict:
        for i in range(1,len(numbers)):
            if not numbers[i] > numbers[i-1]:
                return False
        return True
    for i in range(1,len(numbers)):
        if not numbers[i] >= numbers[i-1]:
            return False
    return True



def rotate_right(my_list):
    if len(my_list) == 0:
        return my_list
    
    
    last_element = my_list[len(my_list)-1]
    rotated_list = [last_element]
    for i in range(len(my_list)-1): 
        rotated_list.append(my_list[i])
    return rotated_list


def weird_double(numbers):
    index = 0
    while index < len(numbers):
        if numbers[index] % 3 == 0: 
            index += 3
        else:
            numbers[index] *= 2
        index += 1
    return numbers



'''
Algorithm:
Say we had these two lists:
=> [ 1, 2, 3, 4, 5 ]
=> [ 2, 2, 4, 6, 7 ]
This algorithm takes the first element of each list...
=> 1, 2
... and compares them!
=> 1 < 2
As we can see, the first list's element was smaller.
So, we add it to the final list.
=> print(final_list): [1]
Then, we move on to the next element of the first list.
Remember: just because the index of an element is smaller, 
          it doesn't mean that it's necessarily less.
Our next comparison is a case of this:
=> 2, 2
Woah, these are equal!
If they weren't equal, we would only add the smaller element,
which is relying on the fact that the lists are already ordered.
However, since they're both equal, we can add both!

Note that we know that no other element (that we haven't already added)
is bigger, since the two lists are ordered.

So:
=> print(final_list): [2,2]

We then move on to the next comparison:
=> 3, 2
and repeat...

until we reach the end of one list:
=> 5 < 6
=> print(final_list): [1,2,2,2,3,4,4,5]

Oh no! We've finished going through List 1. There's no more numbers to compare...

Actually, this makes it easier for us :). Since we've already gone through all of
List 1 and determined that every element was smaller than what's left in List 2,
So, we can simply add the rest of List 2 to the end of the list :)
=> print(final_list): [1,2,2,2,3,4,4,5,6,7]

Voila! (All of these comparisons leading to behaviors for List 1 also work vice versa.)
'''

def merge_ordered_lists(ordered_numbers_1, ordered_numbers_2):
    
    
    if len(ordered_numbers_1) == 0:
        return ordered_numbers_2
    elif len(ordered_numbers_2) == 0:
        return ordered_numbers_1
    
    merged_ordered_list = []
    index_1 = 0
    index_2 = 0
    
    while index_1 != len(ordered_numbers_1) and index_2 != len(ordered_numbers_2): 
        if ordered_numbers_1[index_1] > ordered_numbers_2[index_2]: 
            merged_ordered_list.append(ordered_numbers_2[index_2])
            index_2 += 1
        elif ordered_numbers_2[index_2] > ordered_numbers_1[index_1]: 
             merged_ordered_list.append(ordered_numbers_1[index_1])
             index_1 += 1
        else: 
            merged_ordered_list.append(ordered_numbers_1)
            merged_ordered_list.append(ordered_numbers_2)
            index_1 += 1
            index_2 += 1
    
    if index_1 != len(ordered_numbers_1): 
        for i in range(index_1, len(ordered_numbers_1)):
            merged_ordered_list.append(ordered_numbers_1[i])
    elif index_2 != len(ordered_numbers_2): 
        for i in range(index_2, len(ordered_numbers_2)):
            merged_ordered_list.append(ordered_numbers_2[i])
    
    return merged_ordered_list

