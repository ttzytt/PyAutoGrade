




def create_fruit_loop_dict():
    
    fruit_loop_dict = {
        "red": 6,
        "blue": 5,
        "yellow": 7,
        "orange": 7,
        "purple": 4,
        "green": 6
    }
    return fruit_loop_dict

def calculate_total_fruit_loops(colors, fruit_loop_dict):
    
    colors_list = colors.split()
    cereal_count = 0
    for color in colors_list:
        if color in fruit_loop_dict:
            cereal_count += fruit_loop_dict[color]
    return cereal_count

def main():
    fruit_loop_dict = create_fruit_loop_dict()
    print("Welcome to PRISMS cafeteria!")
    print("Here are the available fruit loop colors: red, blue, yellow, orange, purple, green")
    
    while True:
        user_input = input("Enter the combination of colors (or 'quit' to exit): ")
        
        if user_input == "quit":
            print("Thank you for visiting PRISMS cafeteria. Have a great day!")
            break 
        
        total_fruit_loops = calculate_total_fruit_loops(user_input, fruit_loop_dict)
        print("There are", total_fruit_loops, "fruit loops with those colors.")

if __name__ == "__main__":
    main()
