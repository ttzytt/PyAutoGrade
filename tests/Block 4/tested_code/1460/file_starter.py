
out_file_name = input("out_file_name: ")

if out_file_name[-3:] != ".py":
    out_file_name += ".py"

with (open(out_file_name, 'w') as out_file):
    out_file.writelines(["# Written by: Albert Zhao\n",
                         "# Reviewed by:\n\n\n",
                         "def main():\n    \n    \n    \n    \n    \n    \n",
                         "if __name__ == '__main__':\n",
                         "    main()"])

print("Done.")
    
