



integer = input(' Tell me a random integer ')
integer = int(integer)
triangle_number = 0


if integer % 2 == 0:
    number = 2
    while number <= integer: 
        triangle_number = triangle_number + number
        number = number + 2

if integer % 2 != 0:
    number = 1
    while number <= integer: 
        triangle_number = triangle_number + number
        number = number + 2



print(' The triangular number is ' + str(triangle_number))
