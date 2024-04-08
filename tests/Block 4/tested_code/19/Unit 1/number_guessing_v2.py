




print("Let's play a guessing game")
print("You will guess how many apples and oranges there are")




range_of_count = random.randint(1,2)

if range_of_count == 1:
    orange_count = random.randint(1,10)
    apple_count = random.randint(1,10)
else:
    orange_count = random.randint(2,20)
    apple_count = random.randint(1,5)


print('There is a total of ' + str(orange_count + apple_count) + 'apples and oranges')


player_apple = 0
player_orange = 0

while player_apple != apple_count and player_orange != player_orange:
    print('Enter your guess')
    player_apple = int(input('apples: '))
    player_orange = int(input('oranges: '))

    if player_apple > apple_count:
        print('Not enough apples')
    if apple_count < orange_count:
        print('There are more apples than oranges')
    elif player_orange 



