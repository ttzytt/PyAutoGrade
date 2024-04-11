



import random
random.seed


decks = []
for i in range(13):
    for j in range(4):
        decks.append([i,j])


def full_house(nums = 1000000):
    sums = 0
    for i in range(nums):
        random.shuffle(decks)
        cards = decks[0:5]
        cards.sort()
        if (cards[0][0] == cards[1][0] == cards[2][0] and cards[3][0] == cards[4][0]) or (cards[0][0]==cards[1][0]and cards[2][0]==cards[3][0]==cards[4][0]):
            sums += 1
        sums += 0
    if sums == 0:
        return 0
    return nums/sums


def flush(nums = 1000000):
    sums = 0
    for i in range(nums):
        random.shuffle(decks)
        cards = decks[0:5]
        cards.sort()
        if (cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]):
            sums += 1
        sums += 0
    if sums == 0:
        return 0
    return nums/sums


def straight_flush(nums = 1000000):
    sums = 0
    for i in range(nums):
        random.shuffle(decks)
        cards = decks[0:5]
        cards.sort()
        if ((cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1])
             and ((cards[1][0] + 1 == cards[2][0]) and (cards[3][0] + 1 == cards[4][0]))
            and(((cards[0][0] + 1 == cards[1][0]) and cards[1][0] + 1 == cards[2][0])
            or (cards[0][0] == 0 and cards[4][0] == 9))):
            sums += 1
        sums += 0
    if sums == 0:
        return 0
    return nums/sums


def calculate(nums=1000000):
    sum_ = 0
    for i in range(nums):
        dice = []
        for i in range(5):
            
            dice.append(random.randint(1,4))
        if dice[0] == dice[1] == dice[2] == dice[3]== dice[4]:
            
            sum_ += 1
    
    return nums/sum_


print(calculate())
print(full_house())
print(flush())
print(straight_flush())

