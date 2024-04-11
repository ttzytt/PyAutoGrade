


from operator import itemgetter
import random
random.seed()


def random_hand():
    deck = []
    suits = ['♠', '♥', '♦', '♣']
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    for suit in suits:
        for rank in ranks:
            deck.append([rank, suit])

    random.shuffle(deck)
    
    return deck[:5:]
        
def tries_until_full_house():
    
    count = 0
    full_house = False

    
    while full_house == False:
        hands = random_hand()
        hands.sort()

        
        if (hands[0][0] == hands[1][0]
                and hands[2][0] == hands[3][0]
                and hands[2][0] == hands[4][0]):
            full_house = True
        
        elif (hands[0][0] == hands[1][0]
                and hands[0][0] == hands[2][0]
                and hands[3][0] == hands[4][0]):
            full_house = True
        else:
            full_house = False
        count += 1
    
    return count

def average_amount_of_tries_until_full_house(num_trials):
    total = 0
    for _ in range(1, num_trials):
        total += tries_until_full_house()
    return total/num_trials

def tries_until_straight_flush():
    count = 0
    straight_flush = False

    while straight_flush == False:
        hands = random_hand()
        hands.sort()

        
        
        
        if hands[0][0] == 1:
            if int(hands[0][0] + 1 != int(hands[1][0])):
                hands[0][0] = 14
        hands.sort()

        
        if (int(hands[0][0]) + 1 == int(hands[1][0])
                and int(hands[1][0]) + 1 == int(hands[2][0])
                and int(hands[2][0]) + 1 == int(hands[3][0])
                and int(hands[3][0]) + 1 == int(hands[4][0])):
            if (hands[0][1] == hands[1][1]
                    and hands[0][1] == hands[2][1]
                    and hands[0][1] == hands[3][1]
                    and hands[0][1] == hands[4][1]):
                straight_flush = True
        else:
            straight_flush = False
            
        count += 1
            
    return count


def average_amount_of_tries_until_straight_flush(num_trials):
    total = 0
    for _ in range(1, num_trials):
        total += tries_until_straight_flush()
    return total/num_trials

def tries_until_flush():
    count = 0
    flush = False
    
    
    while flush == False:
        hands = random_hand()
        hands.sort()

        
        
        
        if hands[0][0] == 1:
            if int(hands[0][0] + 1 != int(hands[1][0])):
                hands[0][0] = 14
        hands.sort()

        
        if (hands[0][1] == hands[1][1]
                and hands[0][1] == hands[2][1]
                and hands[0][1] == hands[3][1]
                and hands[0][1] == hands[4][1]):
            if (int(hands[0][0]) + 1 == int(hands[1][0])
                    and int(hands[1][0]) + 1 == int(hands[2][0])
                    and int(hands[2][0]) + 1 == int(hands[3][0])
                    and int(hands[3][0]) + 1 == int(hands[4][0])):
                flush = False
                
            else:
                flush = True
                
        count += 1

    return count


def average_amount_of_tries_until_flush(num_trials):
    total = 0
    for _ in range(1, num_trials):
        total += tries_until_flush()
    return total/num_trials


def dice_roll():
    dice = ['♠', '♥', '♦', '♣']
    random.shuffle(dice)
    
    return dice[0]



def dice_roll_until_flush():
    count = 0
    flush = False

    while flush == False:
        rolls = []
        roll_count = 0

        
        while roll_count <= 5:
            roll = dice_roll()
            rolls.append(roll)
            roll_count += 1
        
        count += 5

        
        if (rolls[0] == rolls[1]
                and rolls[0] == rolls[2]
                and rolls[0] == rolls[3]
                and rolls[0] == rolls[4]):
            flush = True
            
        else:
            flush = False
    return count/5


def average_tries_until_dice_flush(num_trials):
    total = 0
    for _ in range(1, num_trials):
        total += dice_roll_until_flush()
    return total/num_trials







input_valid = True
print("Which hand do you want to know the odds of getting?")

while input_valid == True:
    user_input = str(input("Straight Flush, Flush, Dice Flush, Full House or quit: "))
    if user_input == 'quit':
        print('See you next time.')
        break
    
    num_trials = int(input("How many trials do you want to go through? "))
    print("Give me one second... ")
    
    if user_input == 'Straight Flush':
        straight_flush = average_amount_of_tries_until_straight_flush(num_trials)
        print("The odds of being dealt a Straight Flush is 1 in " + str(straight_flush) + ".")
        print()
                           
    elif user_input == 'Flush':
        flush = average_amount_of_tries_until_flush(num_trials)
        print("The odds of being dealt a Flush is 1 in " + str(flush) + ".")
        print()

    elif user_input == 'Full House':
        Full_House = average_amount_of_tries_until_full_house(num_trials)
        print("The odds of being dealt a Full House is 1 in " + str(Full_House) + ".")
        print()

    elif user_input == 'Dice Flush':
        Dice_Flush = average_tries_until_dice_flush(num_trials)
        print("The odds of being dealt a Dice Flush is 1 in " + str(Dice_Flush) + ".")
        print()
        
    else:
        input_valid = False
        while input_valid == False:
            print("That input was invalid, please try again")
            print()
            input_valid = True
            

            








        
