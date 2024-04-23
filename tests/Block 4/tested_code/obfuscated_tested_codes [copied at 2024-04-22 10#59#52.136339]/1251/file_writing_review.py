







import random



def write_diamond_pattern(outfile, width):
    with open(outfile, 'w') as file:
        
        for i in range(1,width+1):
            
            
            for j in range(abs(i-int((width+1)/2))):
                file.writelines(' ')
            
            for j in range(width-abs(2*i-width-1)):
                file.writelines('*')
            file.writelines('\n')



def last_name_first(in_file,out_file):
    with (open(out_file,'w') as out_file, open(in_file) as in_file):
        for line in in_file:
            words = line.split()
            
            out_file.write(words[1] + ', ' + words[0]+'\n')
                   


def add_and_write(in_file, out_file):
    with (open(out_file,'w') as out_file, open(in_file) as in_file):
        for line in in_file:
            words = line.split()
            
            numbers = []
            
            
            line = line[:-1]
            for i in range(0,len(words),2):
                numbers.append(int(words[i]))
            
            out_file.write(line+ ' = ' + str(sum(numbers)) + '\n')





def blah_blah_blah(in_file, out_file):
    with (open(out_file,'w') as out_file, open(in_file) as in_file):
        for line in in_file:
            
            if len(line) <= 20:
                out_file.write(line)
            
            else:
                out_file.write(line[0:15] + ', blah blah blah' + '\n')



def main():
    write_diamond_pattern('Text files/T11.txt', 15)
    last_name_first('Text files/names.txt','Text files/T12.txt' )
    add_and_write('Text files/addition.txt','Text files/T13.txt')
    blah_blah_blah('Text files/greeneggs.txt','Text files/T14.txt' )

if __name__ == "__main__":
    main()








