





calculation = 0
 
limit = int(input('Enter a number: '))

if limit > 50000:
    print('Woah, that number is pretty big.')
    limit = int(input('Try using a smaller number.'))
    
while calculation < limit: 
    calculation = calculation + 1
    print('The result is: ' + str(calculation))
    




