


import random
random.seed()




like_this_game = str(input('Do you like this game?'))

like_this_game = like_this_game.lower()

if like_this_game == 'yes':
    print('Why? Theres literally no game.')
elif like_this_game == 'no':
    print('Are you serious right now bro?')
else:
    print('What is this gibberish? I thought you were going to give me a human this time.')



file_name = 'Text files/commonwords.txt'

with open(file_name, 'r') as my_file:
    list_full_content = my_file.readlines()

full_content = ' '.join(list_full_content)

print(full_content)

list_full_content.sort()

print(list_full_content)



file_name = 'Text files/greeneggs.txt'

with open(file_name, 'r') as my_file:
    green_eggs_list = my_file.readlines()
    
badly_written_story = []

for i in range(300):
    random_word = random.choice(green_eggs_list)
    
    badly_written_story.append(random_word)

print(badly_written_story)
    
    
