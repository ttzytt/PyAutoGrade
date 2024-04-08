





def item_moved_to_end(my_list, index):
    # R You can remove this quoted out part, does the same thing as code below
    
    new_list = my_list[:index] + my_list[index+1:] + [ my_list[index] ]
    return new_list
    #my_list = my_list[:index] + my_list[index+1:] + my_list[index:index+1]


# Part B
# This function assumes the ranges are correct and change the list
# so that the selected value is moved to the end

def move_item_to_end(my_list, index):
    moved = my_list[index]
    my_list[index:-1] = my_list[index+1:]
    my_list[-1] = moved
    #return my_list


# It returns a new list, but doesn't change the original list
my_list = [1,2,3,4,5,6]
item_moved_to_end(my_list,2)
print(my_list)
print(item_moved_to_end(my_list,2))
print()




ml = [1,2,3,4,5,6]
move_item_to_end(ml,2)
print(ml)
print(move_item_to_end(ml,2))
