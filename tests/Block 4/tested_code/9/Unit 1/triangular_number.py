



user_input_number = int(input(' Enter a number: '))
triangular_number = 1
number = user_input_number


while number > 1:
    triangular_number = triangular_number + number
    number =  number - 1
    
print(str('The triangular number of'  + ' ' + str(user_input_number) + ' is' + ' ' + str(triangular_number) + '. ')) 
            
            



