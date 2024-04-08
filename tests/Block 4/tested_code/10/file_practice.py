


file_name = 'Text files/greeneggs.txt'


def return_backwards():
    forward_list = []
    backwards_list = []

    with open(file_name, 'r') as my_file:
        
        
        list_of_lines = my_file.readlines()
        
    
    i = len(list_of_lines)
    while i > 0:
        backwards_list.append(list_of_lines[i - 1])
        i -= 1
        
    return backwards_list

return_backwards_list = return_backwards()

for i in range(len(return_backwards_list)):
    print(return_backwards_list[i])
