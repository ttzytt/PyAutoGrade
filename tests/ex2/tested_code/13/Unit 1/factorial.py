


number = int(input('Give me a random integer! '))
print()

number_print = number


product = 1


while number > 0:
    product = product*number
    number = number - 1
    
print(str(number_print) + ' factorial is ' + str(product) + '.')
                                        
