




'''def merge_ordered_lists(numbers1,numbers2):
    # el stands for Empty List
    # Assume length equal & less than 5
    el = []
    c1 = 0
    c2 = 0
    while c1 < len(numbers1) and c2 < len(numbers2):
        if numbers1[c1] >= numbers2[c2]:
            el.append(numbers2[c2])
            c2 += 1
        elif numbers1[c1] < numbers2[c2]:
            el.append(numbers1[c1])
            c1 += 1
            
    if c1 == len(numbers1): # 1,2,5/3,6
        while c2 < len(numbers2):
            el.append(numbers2[c2])
            c2 += 1
            
    elif c2 == len(numbers2):
        while c1 < len(numbers1):
            el.append(numbers1[c1])
            c1 += 1

    return el
'''
        
    '''
if numbers1[0] >= numbers2[0]:
            el.append(numbers2[c2])
            c2 += 1
        elif numbers1[0] < numbers2[0]: # While
            el.append(numbers1[0])
            c1 += 1
            
elif numbers1[c1] < numbers2[c2]:
            el.append(numbers1[c1])
            c1 += 1
        el.append(numbers2[c2])
        c2 += 1
    '''
            
            
        

    
    '''if len(numbers1) <= 3 and len(numbers2) <= 3:
        if numbers1[0] <= numbers2[0]:
            el.append(numbers1[0])
            if numbers1[1] <= numbers2[0]:
                el.append(numbers1[1])
                if numbers1[2] <= numbers2[0]:
                    el.append((numbers1[2],numbers2[0],numbers2[1],numbers2[2]))
                elif numbers1[2] > numbers2[0]:
                    el.append(numbers2[0])
            elif numbers1[1] > numbers2[0]:
                el.append(numbers2[0]) #uf'''




'''
for count in range(len(numbers)):
        if is_strict == False: # Can be smaller or equal
            if numbers[count] <= numbers[count+1]:
                return True
            return False
        elif is_strict == True: # Must be smaller (can't be equal)
            if numbers[count] < numbers[count+1]:
                return True
            return False
'''

'''
if len(numbers) == 0:
        return None
    count = 0
    max = numbers[count]
    
    for count in range(len(numbers)-1):
        if numbers[count] >= numbers[count+1]:
         max = max
        elif numbers[count] < numbers[count+1]: 
         if max >= numbers[count+1]:
          max = max
         elif max < numbers[count+1]:
          max = numbers[count+1]
    return max
'''

'''
first = my_list[0]
    last = my_list[len(my_list)-1]
    
    for count in range(len(my_list)-1):
        my_list[count+1] = my_list[count]
        my_list[0] = last
        
        
    return my_list
'''


'''
Code for sum13
if len(nums) == 0:
    return 0
  for i in range(0, len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i+1 < len(nums): 
        nums[i+1] = 0
  return sum(nums)
'''

'''
while count < len(deck):
        h1.append(deck[count])
        count += 1
        h2.append(deck[count])
        count += 1
        h3.append(deck[count])
        count += 1
return h1,h2,h3
'''
    
'''
while count < len(deck):
        h1.append(deck[count])
        count += 1
        h2.append(deck[count])
        count += 1
        h3.append(deck[count])
        count += 1
    return h1,h2,h3
    
'''
'''
if card[count] == 'reverse':
            redin += 1
        elif card[count] != 'reverse':
            redin *= 1
'''
'''
def power_of_i(comnum,power):
    if comnum == 'i':
        if power == 1 or power % 4 == 1:
            return i
        elif power == 2 or power % 4 == 2:
            return -1
        elif power == 3 or power % 4 == 3:
            return -i
        elif power == 4 or power % 4 == 0:
            return 1

'''
'''
while count < len(deck) - (len(deck)%3): 
        hands[0].append(deck[count])
        hands[1].append(deck[count+1])
        hands[2].append(deck[count+2])
        count += 3
if count >= len(deck) - (len(deck)%3):
        if len(deck)%3 >= 1:
            hands[0].append(deck[len(deck) - (len(deck)%3)])
            if len(deck)%3 >= 2:
                hands[1].append(deck[len(deck) - (len(deck)%3) + 1])
'''
import random
    random.seed()
    automove = random.choice(['1A','2A','3A','1B','2B','3B','1C','2C','3C'])
    which_one_move = 1

    if which_one_move % 2 == 1: # User's turn
        if (move == '1A' or move == '2A' or move == '3A' or move == '1B' or move == '2B'
            or move == '3B' or move == '1C' or move == '2C' or move == '3C'):

            if (board[int(move[0])-1][ord(move[1])-ord('A')] == ''
                or board[int(move[0])-1][ord(move[1])-ord('A')] == ' '): 
            
                board[int(move[0])-1][ord(move[1])-ord('A')] = player
                which_one_move += 1
            
                return True
        
        return False

    elif which_one_move % 2 == 0: 
        move = automove
        while (board[int(move[0])-1][ord(move[1])-ord('A')] == ''
            or board[int(move[0])-1][ord(move[1])-ord('A')] == ' '): 
            move = random.choice(['1A','2A','3A','1B','2B','3B','1C','2C','3C'])
            
        if make_move(player,move,board) == True:
            board[int(move[0])-1][ord(move[1])-ord('A')] = player
            which_one_move += 1
            return True
        return False

