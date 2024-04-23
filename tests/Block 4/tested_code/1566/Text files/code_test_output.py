
def last_name_first(in_file, out_file):
    new_name = []
    for line in in_file:
        words = line.split()
        new_name = (words[1] + ', ' + words[0] +'\n')
        out_file.write(new_name)
