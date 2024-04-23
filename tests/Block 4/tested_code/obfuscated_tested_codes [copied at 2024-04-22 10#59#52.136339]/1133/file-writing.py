







def write_diamond_pattern(out_file, width):
    space = (width - 1) // 2
    for i in range(1, width + 1, 2):
        line = ' ' * space + 'x' * i + '\n'
        out_file.write(line)
        space -= 1
    space = 1
    for i in range(width - 2, 0, -2):
        line = ' ' * space + 'x' * i + '\n'
        out_file.write(line)
        space += 1





def last_name_first(in_file, out_file):
    for line in in_file:
        names = line.strip().split() 
        if len(names) == 2:
            out_file.write(names[1] + ", " + names[0] + "\n")





def add_and_write(in_file, out_file):
    for line in in_file:
        parts = line.strip().split(" + ")
        total = sum(int(part) for part in parts)
        out_file.write(line.strip() + " = " + str(total) + '\n')





def blah_blah_blah(in_file, out_file):
    for line in in_file:
        if len(line) > 20:
            out_file.write(line[:15] + ", blah blah blah\n")
        else:
            out_file.write(line)

def main():
    with open('Text files/diamond.txt', 'w') as out_file:
        write_diamond_pattern(out_file, 5)  

    with open('Text files/names.txt', 'r') as in_file, open('Text files/last_name_first.txt', 'w') as out_file:
        last_name_first(in_file, out_file)

    with open('Text files/addition.txt', 'r') as in_file, open('Text files/addition_solved.txt', 'w') as out_file:
        add_and_write(in_file, out_file)

    with open('Text files/long_lines.txt', 'r') as in_file, open('Text files/shortened_lines.txt', 'w') as out_file:
        blah_blah_blah(in_file, out_file)

if __name__ == "__main__":
    main()
