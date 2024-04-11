


"""
This program lets the user input a number and the computer
responds with the factorial of that number
"""


number = int(input('Type any number greater than zero: '))


final_text =number

if number <= 0:
    print("Please enter a positive integer.")
else:
    
    factorial = 1
    
    while number > 0:
        factorial = number * factorial  
        number = number - 1  

    print(f'The factorial of {final_text} is {factorial}.')
