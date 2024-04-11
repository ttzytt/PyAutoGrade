def write_diamond_pattern(outfile, width):
    with open(outfile, 'w') as file:
        for i in range(1,width+1):
            for j in range(abs(i - int((width+1)/2))):
                file.writelines(' ')
            for j in range(min((2*i-1),width-(2*i))):
                file.writelines('*')
            file.writelines('\n')
            
