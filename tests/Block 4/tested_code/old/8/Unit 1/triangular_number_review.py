


number = int(input("Enter a number: ")) 
triangular = number


while number>1:
    triangular = triangular + (number - 1)
    number = number - 1

print("The nth triangular number of your number(n) is: " + str(triangular))

