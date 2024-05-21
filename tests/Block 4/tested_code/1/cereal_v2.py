# cereal_v1.py

# Part A: Create a dictionary with the count of each color of fruit loop
fruit_loops_count = {
    "red": 6,
    "blue": 5,
    "yellow": 7,
    "orange": 7,
    "purple": 4,
    "green": 6
}
def count_fruit_loops(colors):
    total_count = 0
    for color in colors:
        if color in fruit_loops_count:
            total_count += fruit_loops_count[color]
    return total_count


while True:
    user_input = input("Enter fruit loop colors (or 'quit' to exit): ").lower().split()
    if user_input == ['quit']:
        print("Exiting program.")
        break
    elif user_input[0] == 'floor':
        # add new fruit into dict 
        new_fruit = user_input[1]
        if new_fruit not in fruit_loops_count:
            fruit_loops_count[new_fruit] = 1
        else: 
            fruit_loops_count[new_fruit] += 1
    total = count_fruit_loops(user_input)
    msg = "There are {} fruit loops with those colors.".format(total)
    print(msg)

