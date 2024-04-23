

def prefix_count(in_file,prefix_size = 3,num_to_print = 2):
    dcn = {}
    for text in in_file:
        split_text = text.split()
        for i in range(len(split_text)):
            word = split_text[i]
            prefix = word[:prefix_size]
            prefix = prefix.lower()
            
            if prefix not in dcn:
                 dcn[prefix] = 1
            
            else:
                 dcn[prefix] += 1
    return dcn


def sort_by_value(dictionary):
    
    result = []
    
    last_max_value = 0
    max_value = 1
    count = 0
    while max_value != 0:
        record = []
        max_value = 0
        
        for key in dictionary:
            if dictionary[key] > max_value and count == 0:
                max_value = dictionary[key]
            elif last_max_value > dictionary[key] > max_value and count != 0:
                max_value = dictionary[key]
        
        for key in dictionary:
            if dictionary[key] == max_value:
                record.append([key,dictionary[key]])
        
        last_max_value = max_value
        result.append(record)
        count = 1
    return result

def main():
    size = int(input('The size you want count: '))
    num = int(input('The number you want to print: '))
    with open('Text files/names.txt','r') as in_file:
        
        dic = prefix_count(in_file, size, num)
        rec = sort_by_value(dic)
        for i in range(num):
            print(str(i+1) + ' : ')
            for j in range(len(rec[i])):
                print(str(rec[i][j][0]) + ':   ' + str(rec[i][j][1]))
            print()

if __name__ == "__main__":
    main()
