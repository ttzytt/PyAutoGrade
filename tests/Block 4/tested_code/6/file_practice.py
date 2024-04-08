
def count_content(read_file):
    word_count = 0
    line_count = 0
    character_count = 0
    
    for line in read_file:
        line_count += 1
        word_count += len(line.split())
        print(line.split())
        character_count += len(line)
        
    return line_count, word_count, character_count


file_name = 'Text files/Text_Example.txt'
with open(file_name, 'r') as read_file:
    num_line, num_word, num_character = count_content(read_file)

print('The file ' + file_name + ' contains '
      + str(num_character) + ' characters, '
      + str(num_line) + ' lines, '
      + str(num_word) + ' words.')
print()

