
def count_characters(read_file):

    count = 0  

    for line in read_file:  

        count += len(line)

    return count



yes_or_no = input("Do you want to read the story? (y/n) ").lower()

if yes_or_no != 'no':

    

    print("Okay, you can read below!")

    print()

    file_name = 'Text files/greeneggs.txt'

    with open(file_name, 'r') as my_file:

            

            

        full_content = my_file.read()

    print(full_content[:])  

    print()



else:

    other = input("Okay, well do you want a list of addition problems? ").lower()

    if other != 'no':

        print("You can read below!")

        print()

        file_name = 'Text files/addition.txt'

        with open(file_name, 'r') as my_file:

            

            

            full_content = my_file.read()

        print(full_content[:])  



    else:

        print("Okay! Goodbye")



              
