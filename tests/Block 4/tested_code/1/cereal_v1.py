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

# Part B: Define a function to calculate the total number of fruit loops with given colors
def count_fruit_loops(colors):
    total_count = 0
    for color in colors:
        if color in fruit_loops_count:
            total_count += fruit_loops_count[color]
    return total_count

# Part C: Implement the program to run in a loop

while True:
    raw_print("start_await_input")
    user_input = input("Enter fruit loop colors (or 'quit' to exit): ").lower().split()
    raw_print("user_input: ", user_input)   
    if user_input == ['quit']:
        print("Exiting program.")
        break
    total = count_fruit_loops(user_input)
    msg = "There are {} fruit loops with those colors.".format(total)
    print(msg)

