





def count_characters(read_file):
    """
    Returns the number of characters in the file.
    inputs
    """
    count = 0  
    for line in read_file:  
        count += len(line)
    return count

def count_lines(read_file):
    """
    Returns the number of lines in the file.
    inputs:
    """
    line_count = 0
    for _ in read_file:
        line_count += 1
    return line_count


def main():
    
    file_name = 'Text files/names.txt'

    
    my_file = open(file_name, 'r')


    
    full_content = my_file.read()

    
    with open(file_name, 'r') as my_file:
        num_characters = count_characters(my_file)

    print('The file ' + file_name + ' contains ' + str(num_characters) + ' characters.')

    
    with open(file_name, 'r') as my_file:
        num_lines = count_lines(my_file)

    print('The file ' + file_name + ' contains ' + str(num_lines) + ' lines.')


if __name__ == "__main__":

    main()
