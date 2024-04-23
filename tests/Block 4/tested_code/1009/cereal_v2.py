



fruit_loops = {"red": 6, 
              "blue": 5,
              "yellow": 7,
              "orange": 7,
              "purple": 4,
              "green": 6
}

def count_fruit_loops(colors):
    
    color_input = colors.split()
    
    total = 0

    for color in color_input:
        if color == "floor": 
            new_color = color_input[color_input.index(color)+1]
            
            fruit_loops[new_color] = fruit_loops.get(new_color, 0) + 1
        elif color in fruit_loops:
            
            total += fruit_loops[color]
        else:
            fruit_loops[color] = 1
    return total


input_colors = input("Enter the colors of fruit loops you want to know: ")
total_fruit_loops = count_fruit_loops(input_colors)
print(f"There are {total_fruit_loops} fruit loops with those colors.")
    
