

in_file_name = 'Text files/file_writing_copy.py'
out_file_name = 'Text files/file_writing_copy.py'



def comment_function(in_file, out_file):
    lines = in_file.readlines()
    print(lines)
        

with (open(in_file_name,'r')as in_file,
      open(out_file_name, 'w')as out_file):
      comment_function(in_file, out_file)
    
