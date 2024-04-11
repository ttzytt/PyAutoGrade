



in_file_name_1 = 'Text files/file_writing_copy.py'
out_file_name = 'Text files/file_writing_copy.py'

def comments_for_functions(in_file, out_file):
    for line in in_file:
        print(line)

with (open(in_file_name_1,'r') as in_file,
         open(out_file_name, 'w')as out_file): 
        comments_for_functions(in_file, out_file)
