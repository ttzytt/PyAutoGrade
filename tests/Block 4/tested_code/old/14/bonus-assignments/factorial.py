









def validateInt(num):
    
    try:
        int(num)
    
    except:
        print("You didn't enter an integer >:(")
        return False
    else:
        
        if int(num) >= 1:
            return True
        
        else:
            print("That's not factorial-able >:OOO")
            print("Enter a positive integer...")
            return False


validInput = False
while not validInput:
    num = input("Enter a number you want to factorial: ")
    
    validInput = validateInt(num)



i = 1
product = 1
while i <= int(num):
    product *= i 
    i += 1 
print(f"{num}! is equal to {product}.")

