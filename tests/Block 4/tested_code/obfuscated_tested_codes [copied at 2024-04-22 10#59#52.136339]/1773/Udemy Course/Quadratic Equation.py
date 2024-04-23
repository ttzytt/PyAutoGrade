
import math 


print (math.sqrt(9))
print (math.sqrt(25))
print (math.sqrt(16))









input_number = input("Plug in a ")
a = float(input_number)
print("Your number was: ")
print(input_number)

input_number = input("Plug in b ")
b = float(input_number)
print("Your number was: ")
print(input_number)

input_number = input("Plug in c ")
c = float(input_number) 
print("Your number was: ")
print(input_number)

       
square_root_part = math.sqrt(b * b - 4 * a * c)
x_solution_plus = (-b + square_root_part) / (2 * a)
x_solution_minus = (-b - square_root_part) / (2 * a)
print('the solutions for x are ' + str(x_solution_plus) + ' and ' + str(x_solution_minus))
