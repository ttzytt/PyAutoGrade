


"""
This program lets the user input a number greater than zero
and the computer prints out that triangular number
"""


input_number = int(input('Type any number greater than zero: '))


final_text = input_number

if input_number <= 0:
    print("Please enter a positive integer.")
else:
    
    triangle_number = 0 
    while input_number > 0:   
        triangle_number = input_number + triangle_number 
        input_number = input_number - 1  
    
    print(f'The number {final_text} triangle number is {triangle_number}.')
