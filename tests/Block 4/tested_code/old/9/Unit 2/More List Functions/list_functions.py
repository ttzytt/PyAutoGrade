





def item_moved_to_end(my_list, index):
    new_list = my_list[:index] + my_list[index+1:] + [ my_list[index] ]
    #new_list = my_list[:index] + my_list[index+1:] + my_list[index:index+1]
    return new_list

# Part B
# This function assumes the ranges are correct and change the list
# so that the selected value is moved to the end

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



