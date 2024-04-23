

import random


"""
Reads the list of names of everyone in the class and makes a bracket, where the 1st and 2nd ,
names, 3rd and 4th names and so on go against each other, and a 'winner' is randomly chosen to
move on to the next round.
"""

file_name = 'Text files/names.txt'
with open(file_name, 'r') as my_file: 
    full_content = my_file.read()
    names = full_content.splitlines() 
    random.shuffle(names)

next_round_lists = []

for i in range(0, len(names), 2): 
    if i <= len(names) - 2:
        first_competitor = names[i] 
        second_competitor = names[i + 1] 
        
        winner = random.randint(1, 2) 
        
        if winner == 1:
            next_round_lists.append(first_competitor) 
            
        else: 
            next_round_lists.append(second_competitor)
    else:
        next_round_lists.append(names[i]) 

print(next_round_lists) 
    
