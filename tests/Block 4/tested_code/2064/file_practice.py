






import random
random.seed()





def generate_ten(my_file):
    all_items = []
    item_numbers = []
    list_of_items = []
    
    for line in my_file:
        all_items.append(line)
    
    for i in range(10):
        item_numbers.append(random.randint(1, len(all_items) - 1))

    for number in item_numbers:
        list_of_items.append(all_items[number])

    for i in range(len(list_of_items)):
        print(list_of_items[i])



def longest_line(read_file):
    max_words = [''] 
    for line in read_file:
        if (len(line) > len(max_words[0])):
            max_words = [line]
        elif(len(line) == max_words):
            max_words.append(line)

    return max_words


file_name = 'Text files/greeneggs.txt'
with open(file_name, 'r') as my_file:
    print(longest_line(my_file))











