'''
Written by Alex
Reviewed by Ethan
I did not receive help from my classmates
I got some guidance from Dr.Deionno
'''




'''This function doesn't change the list'''
def item_moved_to_end(my_list, index):
    new_list = my_list[:index] + my_list[index+1:] + [ my_list[index] ]
    #new_list = my_list[:index] + my_list[index+1:] + my_list[index:index+1]
    return new_list

# Part B
# This function assumes the ranges are correct and change the list
# so that the selected value is moved to the end
'''This function changes the list'''
def move_item_to_end(my_list, index):
    moved = my_list[index]
    my_list[index:-1] = my_list[index+1:]
    my_list[-1] = moved
    # This function doesn't return anything



my_list = [1,2,3,4,5,6]
item_moved_to_end(my_list,2)
print(my_list)
print(item_moved_to_end(my_list,2))
print()



test_list = [1,2,3,4,5,6]
move_item_to_end(test_list,2)
print(test_list)
print(move_item_to_end(test_list,2))


'''
    moved_item = my_list[index]
    new_list = my_list[:index] + my_list[index+1:]
    new_list.append(moved_item)
'''
