


import random



def write_diamond_pattern(outfile, width):
    
    for i in range(1,width+1):
        
        outfile.write(' '*(abs(i-int((width+1)/2))) + '*'*(width-abs(2*i-width-1)) + '\n')



def last_name_first(in_file,out_file):
    for line in in_file:
        words = line.split()
        
        out_file.write(words[1] + ', ' + words[0]+'\n')
                   


def add_and_write(in_file, out_file):
    for line in in_file:
        words = line.split()
        
        numbers = []
        
        line = line[:-1]
        for i in range(0,len(words),2):
            numbers.append(int(words[i]))
        
        out_file.write(line+ ' = ' + str(sum(numbers)) + '\n')





def blah_blah_blah(in_file, out_file):
    for line in in_file:
        
        if len(line) <= 20:
            out_file.write(line)
        
        else:
            out_file.write(line[0:15] + ', blah blah blah' + '\n')



def main():
    with(open('Text files/T11.txt','w') as file):
        write_diamond_pattern(file, 15)
    with(open('Text files/T12.txt','w') as out_file, open('Text files/names.txt') as in_file):
        last_name_first(in_file,out_file)
    with(open('Text files/T13.txt','w') as out_file, open('Text files/addition.txt') as in_file):
        add_and_write(in_file,out_file)
    with(open('Text files/T14.txt','w') as out_file, open('Text files/greeneggs.txt') as in_file):
        blah_blah_blah(in_file,out_file)

if __name__ == "__main__":
    main()








