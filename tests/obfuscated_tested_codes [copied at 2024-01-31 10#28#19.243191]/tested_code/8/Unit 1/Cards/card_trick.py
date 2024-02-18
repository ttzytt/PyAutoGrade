


from card_functions import *


deck = []

for i in range(1, 22):
    deck.append(i)
    i+= 1

user_num = input('Pick an integer between 1 and 21 inclusive: ')

columns = deal_3_hands(deck)
print(columns)

for i in range(3):
    column_num = int(input('Which group is your card in? 1: ' + str(columns[0]) +
                       ' 2: ' + str(columns[1]) +
                       ' or 3: ' + str(columns[2]) + ' - '))
    print()
    print(columns[abs(column_num - 2)])
    deck = []
    deck.append(columns[abs(column_num - 2)])
    
    deck.append(columns[column_num - 1])
    
    deck.append(columns[abs(column_num - 3)])
    print(deck)
    columns = deal_3_hands(deck)
    print(columns)

print('Your number is ' + str(columns[1][3]))
