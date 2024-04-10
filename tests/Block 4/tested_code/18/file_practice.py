



file_name = 'Text files/commonwords.txt'


def read_lines():
    with open(file_name, 'r') as my_file:
        
        
        list_of_lines = my_file.readlines()
    return(list_of_lines[line_number]) 

line_number = int(input('Which line would you like to read?(enter number): '))
print("Line " + str(line_number) + " reads: " + read_lines())


def word_looking_read_lines():
    with open(file_name, 'r') as my_file:
        
        
        list_of_lines = my_file.readlines()

        count = 0

        for i in range(0, len(list_of_lines)):
            if list_of_lines[i][0] == initial:
                count += 1
        
    return(str(count))

initial = input("Which initial are you looking for?(enter lower case): ")
print("There are " + word_looking_read_lines() + " words starting with ")
print(initial + " in the commonwords list.")
