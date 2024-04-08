





import random
def roll_dice():
    
    return random.randint(1, 6), random.randint(1, 6)

def play_board_game(target_value, max_turns):
    
    position = 0

    for turn in range(1, max_turns + 1):
        dice_rolls = roll_dice()
        total_roll = sum(dice_rolls)
        position += total_roll

        if position >= target_value:
            return True  

    return False  

def calculate_winning_probability(num_trials, target_value, max_turns):
    
    wins_count = 0
    for _ in range(num_trials):
        if play_board_game(target_value, max_turns):
            wins_count += 1
    return wins_count / num_trials

if __name__ == "__main__":
    
    target_value = int(input("Enter the target value: "))
    max_turns = int(input("Enter the maximum number of turns: "))
    num_trials = int(input("Enter the number of trials: "))
    result = calculate_winning_probability(num_trials, target_value, max_turns)
    print("Probability of winning the simplified dice-based board game:", result)
